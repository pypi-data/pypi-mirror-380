"""CLI for the Veris CLI."""

from importlib.metadata import PackageNotFoundError, version as pkg_version
from pathlib import Path
import typer
import tomllib
from dotenv import load_dotenv

from veris_cli.commands.config import config_app
from veris_cli.commands.init import init_app
from veris_cli.commands.scenario import scenario_app
from veris_cli.commands.setup import setup_app
from veris_cli.commands.sim import sim_app

load_dotenv()


app = typer.Typer(help="Veris CLI")
app.add_typer(init_app, name="init", help="Initialize .veris project files")
app.add_typer(setup_app, name="setup", help="Run local FastAPI and expose via ngrok")
app.add_typer(sim_app, name="sim", help="Run simulations (launch/status/kill)")
app.add_typer(scenario_app, name="scenario", help="Scenario generation (generate/status/get)")
app.add_typer(config_app, name="config", help="Get/set CLI configuration values")


def _resolve_version() -> str:
    """Return the package version using installed metadata, or pyproject.toml as fallback."""
    try:
        return pkg_version("veris-cli")
    # Fallback to pyproject.toml if installed metadata is not available
    except PackageNotFoundError:
        try:
            cur = Path(__file__).resolve()
            for parent in cur.parents:
                candidate = parent / "pyproject.toml"
                if candidate.exists():
                    data = tomllib.loads(candidate.read_text(encoding="utf-8"))
                    proj = data.get("project", {})
                    ver = proj.get("version")
                    if isinstance(ver, str) and ver:
                        return ver
                    break
        except Exception:
            pass
    return "unknown"


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(_resolve_version())
        raise typer.Exit(code=0)


@app.callback()
def _root_options(
    version: bool = typer.Option(
        False,
        "--version",
        help="Show the Veris CLI version and exit",
        is_eager=True,
        callback=_version_callback,
    ),
):
    # Root-level options only; commands continue as usual
    return


def main():
    """Main entry point."""
    app()


if __name__ == "__main__":
    main()
