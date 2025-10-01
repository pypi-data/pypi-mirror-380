"""Simulation commands."""

from __future__ import annotations

import re
import time
from pathlib import Path
from typing import Annotated

import typer
import httpx
from rich import print as rprint
from rich.live import Live
from rich.text import Text

from veris_cli.config import load_config
from veris_cli.loaders import load_scenarios
from veris_cli.run_models import RunStatus
from veris_cli.runner import SimulationRunner
from veris_cli.runs import RunsStore
from veris_cli.errors import UpstreamServiceError, ConfigurationError
from veris_cli.api import ApiClient
from veris_cli.fs import ensure_veris_dir
from veris_cli.run_models import V3Run, V3SessionEntry, V3SessionStatus

sim_app = typer.Typer(add_completion=False, no_args_is_help=False)


def _select_scenarios(
    scenarios: list[dict],
    ids: list[str] | None = None,
    use_cases: list[str] | None = None,
) -> list[dict]:
    """Select scenarios."""
    selected = scenarios
    if use_cases:
        use_set = set(use_cases)
        selected = [
            s for s in selected if s.get("skeleton_metadata", {}).get("use_case_name") in use_set
        ]
    if ids:
        id_set = set(ids)
        selected = [s for s in selected if s.get("scenario_id") in id_set]
    return selected


def _colorize_status(text: str) -> str:
    """Add Rich markup colors to status keywords in a status string."""
    mapping = {
        "pending": "yellow",
        "running": "cyan",
        "completed": "green",
        "failed": "red",
    }

    def _repl(match: re.Match[str]) -> str:
        word = match.group(0)
        color = mapping.get(word.lower())
        return f"[{color}]{word}[/]" if color else word

    return re.sub(
        r"\b(pending|running|completed|failed)\b",
        _repl,
        text,
        flags=re.IGNORECASE,
    )


@sim_app.command("launch")
def launch(
    agent: Annotated[
        Path | None,
        typer.Option("--agent", help="Path to agent.json"),
    ] = None,
    scenarios: Annotated[
        list[str] | None,
        typer.Option("--scenarios", help="Scenario IDs to run"),
    ] = None,
    use_cases: Annotated[
        list[str] | None,
        typer.Option("--use-cases", help="Filter by use_case_name"),
    ] = None,
    watch: Annotated[
        bool,
        typer.Option(
            "--watch",
            help="Continuously poll status until simulations and evals complete",
        ),
    ] = False,
):
    """Launch a simulation."""
    project_dir = Path.cwd()
    veris_dir = project_dir / ".veris"
    scenarios_dir = veris_dir / "scenarios"

    all_scenarios = load_scenarios(scenarios_dir)
    selected_scenarios = _select_scenarios(all_scenarios, scenarios, use_cases)

    if not selected_scenarios:
        rprint("[red]No scenarios selected[/red]")
        raise typer.Exit(code=1)

    store = RunsStore(project_dir)
    runner = SimulationRunner(store)

    # Load agent configuration from .veris/config.json, if available
    cfg = load_config(project_dir)
    agent_payload = None
    if getattr(cfg, "agent", None) is None:
        # Provide actionable guidance if no agent connection configured
        raise ConfigurationError(
            message=(
                "Agent endpoint is not configured in .veris/config.json (missing 'agent' block)."
            ),
            hint=(
                "Run 'veris setup ...' to detect your public URL automatically, or set it manually "
                "with 'veris config public_url https://<your-ngrok>.ngrok.io'."
            ),
            file_path=str(veris_dir / "config.json"),
            command_suggestion="veris setup  # or: veris config public_url https://...",
        )
    else:
        # Validate MCP endpoint itself is reachable.
        # We treat 2xx–4xx as a signal that the server is up (e.g., 400/405 on GET),
        # and only fail on network errors/timeouts or 5xx.
        mcp_url = cfg.agent.mcp_url.rstrip("/")

        per_attempt_timeout = 5.0
        attempts = 3
        last_status_details: list[str] = []
        last_exception: Exception | None = None
        reachable = False

        for attempt in range(attempts):
            try:
                resp = httpx.get(mcp_url, timeout=per_attempt_timeout, follow_redirects=True)
                if resp.status_code < 500:
                    # 2xx–4xx considered OK for liveness
                    reachable = True
                    break
                else:
                    last_status_details.append(f"{mcp_url} -> {resp.status_code}")
            except httpx.RequestError as exc:
                last_exception = exc
                last_status_details.append(f"{mcp_url} -> request error: {exc.__class__.__name__}")
            time.sleep(0.4 * (attempt + 1))

        if not reachable:
            hint_lines = [
                f"Tried MCP endpoint: {mcp_url}.",
                "Ensure your FastAPI app is running and ngrok tunnel is active.",
                "Run 'veris setup ...' or set a working public URL.",
            ]
            if last_status_details:
                hint_lines.insert(1, "Checks: " + "; ".join(last_status_details))
            raise ConfigurationError(
                message="Unable to reach configured agent MCP URL.",
                hint=" ".join(hint_lines),
                file_path=str(veris_dir / "config.json"),
                command_suggestion="veris setup  # or: veris config public_url https://...",
            ) from last_exception

        # Convert Pydantic model to plain dict for payload
        agent_payload = cfg.agent.model_dump()  # type: ignore[assignment]

    run = runner.launch(selected_scenarios, agent=agent_payload)

    print("Run file: ", veris_dir.joinpath("runs", run.run_id + ".json"))

    if watch:
        try:
            with Live("", refresh_per_second=4, transient=False) as live:
                while True:
                    time.sleep(2.0)
                    try:
                        run = runner.poll_once(run)
                    except UpstreamServiceError as e:
                        rprint(f"[red]{str(e)}[/red]")
                        raise typer.Exit(code=1)
                    base = runner.format_status(run)
                    colored = _colorize_status(base)
                    header = "[cyan]Watching run status. Press Ctrl+C to stop.[/cyan]"
                    live.update(Text.from_markup(header + "\n" + colored))
                    # Done when all evals have reached a terminal state
                    all_evals_terminal = all(
                        getattr(sim, "evaluation_status", None)
                        in (
                            RunStatus.completed,
                            RunStatus.failed,
                        )
                        for sim in run.simulations
                    )
                    if all_evals_terminal:
                        live.update(
                            Text.from_markup(
                                header
                                + "\n"
                                + colored
                                + "\n[green]All simulations and evaluations are complete.[/green]"
                            )
                        )
                        break
        except KeyboardInterrupt:
            rprint(
                "[yellow]Stopped watching. Check later with: "
                f"veris sim status --run {run.run_id}[/yellow]"
            )
    else:
        rprint(runner.format_status(run))


@sim_app.command("status")
def status(
    run_id: str = typer.Option(..., "--run", help="Run ID"),
):
    """Get the status of a simulation."""
    store = RunsStore(Path.cwd())
    runner = SimulationRunner(store)
    try:
        run = store.load_run(run_id)
    except ConfigurationError as e:
        rprint(f"[red]{str(e)}[/red]")
        raise typer.Exit(code=1)
    try:
        run = runner.poll_once(run)
    except UpstreamServiceError as e:
        rprint(f"[red]{str(e)}[/red]")
        raise typer.Exit(code=1)
    rprint(runner.format_status(run))


@sim_app.command("results")
def results(
    run_id: Annotated[str, typer.Option("--run", help="Run ID")],
    json_out: Annotated[bool, typer.Option("--json", help="Output JSON")] = False,
):
    """Print evaluation_results for all sessions in the run."""
    store = RunsStore(Path.cwd())
    try:
        run = store.load_run(run_id)
    except ConfigurationError as e:
        rprint(f"[red]{str(e)}[/red]")
        raise typer.Exit(code=1)

    simulations = [
        {
            "scenario_id": sim.scenario_id,
            "simulation_id": sim.simulation_id,
            "eval_id": sim.eval_id,
            "evaluation_results": sim.evaluation_results or {},
        }
        for sim in run.simulations
    ]

    if json_out:
        import json as _json

        rprint(
            _json.dumps(
                {"run_id": run.run_id, "simulations": simulations},
                indent=2,
                ensure_ascii=False,
            )
        )
        return

    # Default human-readable output
    rprint(f"[bold]Run[/bold] {run.run_id}")
    for item in simulations:
        scen = item["scenario_id"]
        sid = item["simulation_id"]
        rprint(f"- [cyan]{scen}[/cyan] ({sid})")
        rprint(item["evaluation_results"])  # prints dict or empty


@sim_app.command("kill")
def kill(simulation_id: str):
    """Kill a simulation."""
    from veris_cli.api import ApiClient

    api = ApiClient()
    api.kill_simulation(simulation_id)
    rprint(f"[yellow]Requested kill for simulation {simulation_id}[/yellow]")


@sim_app.command("eval-kill")
def eval_kill(eval_id: str):
    """Kill an evaluation."""
    from veris_cli.api import ApiClient

    api = ApiClient()
    api.kill_evaluation(eval_id)
    rprint(f"[yellow]Requested kill for evaluation {eval_id}[/yellow]")


@sim_app.command("v3launch")
def v3launch(
    agent_id: Annotated[
        str | None,
        typer.Option("--agent-id", help="Agent ID"),
    ] = None,
    generate_scenario_set: Annotated[
        bool,
        typer.Option("--generate-scenario-set", help="Generate new scenario set"),
    ] = False,
    watch: Annotated[
        bool,
        typer.Option(
            "--watch",
            help="Continuously poll status until simulations complete",
        ),
    ] = False,
):
    """Launch full V3 flow rooted on agent_id.

    Flow:
    - If agent_id not provided: create new agent using .veris/agent.json and config MCP values
    - Sleep 0.5s, then fetch agent via v3_get_agent
    - If --generate-scenario-set: create, poll until ready; then sleep 0.5s
    - Fetch latest scenario set and continue with simulation
    """
    project_dir = Path.cwd()
    veris_dir = ensure_veris_dir(project_dir)
    scenarios_dir = veris_dir / "scenarios"
    scenarios_dir.mkdir(exist_ok=True)

    import json as _json

    api = ApiClient()

    # Load agent spec from .veris/agent.json if needed to create
    agent_spec: dict | None = None
    agent_json = veris_dir / "agent.json"
    if agent_json.exists():
        try:
            agent_spec = _json.loads(agent_json.read_text(encoding="utf-8"))
        except Exception as e:
            rprint(f"[yellow]Ignoring local agent.json (invalid): {e}[/yellow]")

    # =========================
    # V3: AGENT (create if needed, then fetch authoritative)
    # =========================
    if not agent_id:
        with Live("[cyan]Creating agent...[/cyan]", refresh_per_second=4, transient=False) as live:
            if agent_spec is None:
                rprint("[red]No agent_id provided and .veris/agent.json missing[/red]")
                raise typer.Exit(code=1)
            cfg = load_config(project_dir)
            if getattr(cfg, "agent", None) is not None:
                conn = cfg.agent  # type: ignore[assignment]
                ac = agent_spec.setdefault("agent_config", {})
                if isinstance(ac, dict):
                    if getattr(conn, "mcp_url", None):
                        ac["mcp_url"] = conn.mcp_url
                    if getattr(conn, "mcp_transport", None):
                        ac["mcp_transport"] = conn.mcp_transport
            created = api.v3_create_agent(agent_spec, version=agent_spec.get("version", "v1.0.0"))
            agent_id = created.get("agent_id")
            if not agent_id:
                rprint("[red]Agent creation did not return agent_id[/red]")
                raise typer.Exit(code=1)
            live.update(Text.from_markup(f"[green]Agent created[/green] {agent_id}"))
        time.sleep(0.5)

    with Live("[cyan]Fetching agent...[/cyan]", refresh_per_second=4, transient=False) as live:
        agent_full = api.v3_get_agent(agent_id)  # type: ignore[arg-type]
        version_id = agent_full.get("version")
        if not version_id:
            rprint("[red]Fetched agent missing version[/red]")
            raise typer.Exit(code=1)
        live.update(Text.from_markup(f"[green]Agent ready[/green] {agent_id} {version_id}"))

    # =========================
    # V3: SCENARIO SET (optionally generate, then fetch latest)
    # =========================
    scenario_set_id: str | None = None
    scenario_sets = api.v3_get_latest_scenario_sets(agent_id)  # type: ignore[arg-type]

    if generate_scenario_set:
        body = {"version_id": version_id, "dimensions": {}, "num_scenarios": 3}  # type: ignore[arg-type]
        with Live(
            "[cyan]Creating scenario set...[/cyan]", refresh_per_second=4, transient=False
        ) as live:
            ss = api.v3_create_scenario_set(agent_id, body)  # type: ignore[arg-type]
            time.sleep(0.5)
            scenario_set_id = ss.get("scenario_set_id")
            if not scenario_set_id:
                rprint("[red]Scenario set creation failed[/red]")
                raise typer.Exit(code=1)
            live.update(Text.from_markup(f"[green]Scenario set[/green] {scenario_set_id}"))
        with Live(
            "[cyan]Waiting for scenarios to generate...[/cyan]",
            refresh_per_second=4,
            transient=False,
        ) as live:
            status = "IN_PROGRESS"
            gen_start = time.time()
            for _ in range(120):
                details = api.v3_get_scenario_set(agent_id, scenario_set_id)  # type: ignore[arg-type]
                status = details.get("status", status)
                elapsed = int(time.time() - gen_start)
                live.update(
                    Text.from_markup(
                        f"Scenario set status: [bold]{status}[/bold] (elapsed: {elapsed}s)"
                    )
                )
                if status != "IN_PROGRESS":
                    break
                time.sleep(2.0)
            elapsed = int(time.time() - gen_start)
            if status == "IN_PROGRESS":
                rprint(
                    f"[red]Scenario set generation failed after {elapsed}s: still IN_PROGRESS[/red]"
                )
                raise typer.Exit(code=1)
        time.sleep(0.5)
        scenario_sets = api.v3_get_latest_scenario_sets(agent_id)  # type: ignore[arg-type]

    with Live(
        "[cyan]Fetching latest scenario set...[/cyan]", refresh_per_second=4, transient=False
    ) as live:
        if len(scenario_sets) == 0:
            rprint(
                "[red]No scenario sets found for agent, please add the --generate-scenario-set flag[/red]"
            )
            raise typer.Exit(code=1)
        latest_ss = scenario_sets[0]
        scenario_set_id = latest_ss.get("scenario_set_id")
        if not scenario_set_id:
            rprint("[red]No scenario set found for agent[/red]")
            raise typer.Exit(code=1)
        status = latest_ss.get("status")
        if status == "IN_PROGRESS":
            rprint("[red]Latest scenario set is still IN_PROGRESS[/red]")
            raise typer.Exit(code=1)
        live.update(Text.from_markup(f"[green]Scenario set ready[/green] {scenario_set_id}"))

    # Clear scenarios directory
    for file in scenarios_dir.glob("*.json"):
        file.unlink()

    # Save scenarios locally
    scenarios = api.v3_list_scenarios(agent_id, scenario_set_id)  # type: ignore[arg-type]
    for sc in scenarios:
        sid = sc.get("scenario_id")
        if not sid:
            continue
        (scenarios_dir / f"{sid}.json").write_text(_json.dumps(sc, indent=2), encoding="utf-8")

    # =========================
    # V3: START SIMULATION
    # =========================
    with Live(
        "[cyan]Starting simulation run...[/cyan]", refresh_per_second=4, transient=False
    ) as live:
        sim = api.v3_start_simulation(
            agent_id,
            {"version_id": version_id, "scenario_set_id": scenario_set_id},  # type: ignore[arg-type]
        )
        run_id = sim.get("run_id")
        if not run_id:
            rprint("[red]Failed to start simulation run[/red]")
            raise typer.Exit(code=1)
        live.update(Text.from_markup(f"[green]Run created[/green] {run_id}"))

    run = V3Run(
        run_id=run_id,
        created_at=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        status=V3SessionStatus.in_progress,
        agent_id=agent_id,  # type: ignore[arg-type]
        version_id=version_id,  # type: ignore[arg-type]
        scenario_set_id=scenario_set_id,  # type: ignore[arg-type]
        sessions=[],
    )
    store = RunsStore(project_dir)
    store.save_run(run)  # type: ignore[arg-type]
    print("Run file: ", veris_dir.joinpath("runs", run.run_id + ".json"))

    # =========================
    # V3: POLL SESSIONS & EVALUATE
    # =========================
    if watch:
        try:
            with Live("", refresh_per_second=4, transient=False) as live:
                sim_start = time.time()

                def _fmt_secs(total: int) -> str:
                    mins, secs = divmod(total, 60)
                    hours, mins = divmod(mins, 60)
                    return f"{hours:d}:{mins:02d}:{secs:02d}"

                while True:
                    time.sleep(2.0)
                    sessions = api.v3_list_sessions(agent_id, run_id)  # type: ignore[arg-type]
                    session_map = {s.session_id: s for s in run.sessions}
                    for s in sessions:
                        sess_id = s.get("session_id")
                        if not sess_id:
                            continue
                        entry = session_map.get(sess_id)
                        status_str = s.get("status", "FAILED")
                        status_enum = V3SessionStatus(status_str)
                        if entry is None:
                            entry = V3SessionEntry(
                                session_id=sess_id,
                                scenario_id=s.get("scenario_id", ""),
                                status=status_enum,
                            )
                            run.sessions.append(entry)
                            session_map[sess_id] = entry
                        else:
                            entry.status = status_enum

                        try:
                            logs = api.v3_get_session_logs(agent_id, run_id, sess_id)  # type: ignore[arg-type]
                            if isinstance(logs, list):
                                entry.logs = logs
                        except UpstreamServiceError:
                            pass

                        try:
                            details = api.v3_get_session_details(agent_id, run_id, sess_id)  # type: ignore[arg-type]
                            if isinstance(details, dict):
                                entry.details = details
                        except UpstreamServiceError:
                            pass

                        # Grade once terminal using agent_full.evaluation_config
                        graders_dict = (
                            agent_full.get("evaluation_config")
                            if isinstance(agent_full, dict)
                            else None
                        )
                        grader = (
                            next(iter(graders_dict.values()))
                            if isinstance(graders_dict, dict) and graders_dict
                            else None
                        )
                        if entry.status in (V3SessionStatus.completed, V3SessionStatus.failed):
                            has_eval = False
                            if isinstance(entry.details, dict):
                                ev = entry.details.get("evaluation")
                                if isinstance(ev, dict) and ("results" in ev or "error" in ev):
                                    has_eval = True
                            if not has_eval and grader and isinstance(entry.logs, list):
                                try:
                                    result = api.grade(grader, entry.logs)
                                    entry.details.setdefault("evaluation", {})["results"] = result
                                except Exception as e:
                                    entry.details.setdefault("evaluation", {})["error"] = str(e)

                    all_terminal = (
                        all(
                            s.status in (V3SessionStatus.completed, V3SessionStatus.failed)
                            for s in run.sessions
                        )
                        and len(run.sessions) > 0
                    )
                    run.status = (
                        V3SessionStatus.completed if all_terminal else V3SessionStatus.in_progress
                    )

                    store.save_run(run)

                    header = "[cyan]v3 flow: agent -> scenario_set -> simulation[/cyan]"
                    parts = [f"Run {run.run_id} - {run.status.value}"]

                    by_scenario: dict[str, list[V3SessionEntry]] = {}
                    for entry in run.sessions:
                        key = entry.scenario_id or "unknown"
                        by_scenario.setdefault(key, []).append(entry)

                    def _color_status(s: V3SessionStatus) -> str:
                        mapping = {
                            V3SessionStatus.pending: "yellow",
                            V3SessionStatus.in_progress: "cyan",
                            V3SessionStatus.completed: "green",
                            V3SessionStatus.failed: "red",
                        }
                        color = mapping.get(s)
                        return f"[{color}]{s.value}[/]" if color else s.value

                    for scen_id, entries in by_scenario.items():
                        parts.append(f"  [bold cyan]Scenario[/bold cyan] [bold]{scen_id}[/bold]")
                        for entry in entries:
                            parts.append(
                                f"    Session {entry.session_id}: {_color_status(entry.status)} ({len(entry.logs)} logs)"
                            )
                            ev = (
                                entry.details.get("evaluation")
                                if isinstance(entry.details, dict)
                                else None
                            )
                            if isinstance(ev, dict):
                                if "results" in ev:
                                    parts.append("      [green]eval: completed[/green]")
                                elif "error" in ev:
                                    parts.append("      [red]eval: error[/red]")

                    elapsed = int(time.time() - sim_start)
                    parts.append(f"Elapsed: {_fmt_secs(elapsed)}")
                    live.update(Text.from_markup("\n".join([header] + parts)))
                    if all_terminal:
                        total = int(time.time() - sim_start)
                        parts.append(f"[green]All sessions completed in {_fmt_secs(total)}[/green]")
                        live.update(Text.from_markup("\n".join([header] + parts)))
                        break
        except KeyboardInterrupt:
            rprint(
                "[yellow]Stopped watching. Check later with: "
                f"veris sim status --run {run.run_id}[/yellow]"
            )
    else:
        rprint(f"Run {run.run_id} - {run.status.value}")
