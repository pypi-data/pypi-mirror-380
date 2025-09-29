import logging
import os
from pathlib import Path
from typing import Literal

import click
import questionary
from llama_deploy.cli.commands.auth import validate_authenticated_profile
from llama_deploy.cli.config.env_service import service
from llama_deploy.cli.config.schema import Auth
from llama_deploy.cli.options import interactive_option
from llama_deploy.cli.styles import WARNING
from llama_deploy.core.config import DEFAULT_DEPLOYMENT_FILE_PATH
from llama_deploy.core.deployment_config import (
    read_deployment_config_from_git_root_or_cwd,
)
from rich import print as rprint

from ..app import app

logger = logging.getLogger(__name__)


@app.command(
    "serve",
    help="Serve a LlamaDeploy app locally for development and testing",
)
@click.argument(
    "deployment_file",
    required=False,
    default=DEFAULT_DEPLOYMENT_FILE_PATH,
    type=click.Path(dir_okay=True, resolve_path=True, path_type=Path),
)
@click.option(
    "--no-install", is_flag=True, help="Skip installing python and js dependencies"
)
@click.option(
    "--no-reload", is_flag=True, help="Skip reloading the API server on code changes"
)
@click.option("--no-open-browser", is_flag=True, help="Skip opening the browser")
@click.option(
    "--preview",
    is_flag=True,
    help="Preview mode pre-builds the UI to static files, like a production build",
)
@click.option("--port", type=int, help="The port to run the API server on")
@click.option("--ui-port", type=int, help="The port to run the UI proxy server on")
@click.option(
    "--log-level",
    type=click.Choice(
        ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], case_sensitive=False
    ),
    help="The log level to run the API server at",
)
@click.option(
    "--log-format",
    type=click.Choice(["console", "json"], case_sensitive=False),
    help="The format to use for logging",
)
@click.option(
    "--persistence",
    type=click.Choice(["memory", "local", "cloud"]),
    help="The persistence mode to use for the workflow server",
)
@click.option(
    "--local-persistence-path",
    type=click.Path(dir_okay=True, resolve_path=True, path_type=Path),
    help="The path to the sqlite database to use for the workflow server if using local persistence",
)
@interactive_option
def serve(
    deployment_file: Path,
    no_install: bool,
    no_reload: bool,
    no_open_browser: bool,
    preview: bool,
    port: int | None = None,
    ui_port: int | None = None,
    log_level: str | None = None,
    log_format: str | None = None,
    persistence: Literal["memory", "local", "cloud"] | None = None,
    local_persistence_path: Path | None = None,
    interactive: bool = False,
) -> None:
    """Run llama_deploy API Server in the foreground. Reads the deployment configuration from the current directory. Can optionally specify a deployment file path."""
    if not deployment_file.exists():
        rprint(f"[red]Deployment file '{deployment_file}' not found[/red]")
        raise click.Abort()

    try:
        # Pre-check: if the template requires llama cloud access, ensure credentials
        _maybe_inject_llama_cloud_credentials(
            deployment_file, interactive, require_cloud=persistence == "cloud"
        )

        # Defer heavy appserver imports until the `serve` command is actually invoked
        from llama_deploy.appserver.app import (
            prepare_server,
            start_server_in_target_venv,
        )
        from llama_deploy.appserver.deployment_config_parser import (
            get_deployment_config,
        )

        prepare_server(
            deployment_file=deployment_file,
            install=not no_install,
            build=preview,
        )
        deployment_config = get_deployment_config()
        start_server_in_target_venv(
            cwd=Path.cwd(),
            deployment_file=deployment_file,
            proxy_ui=not preview,
            reload=not no_reload,
            open_browser=not no_open_browser,
            port=port,
            ui_port=ui_port,
            log_level=log_level.upper() if log_level else None,
            log_format=log_format.lower() if log_format else None,
            persistence=persistence if persistence else "local",
            local_persistence_path=str(local_persistence_path)
            if local_persistence_path and persistence == "local"
            else None,
            cloud_persistence_name=f"_public:serve_workflows_{deployment_config.name}"
            if persistence == "cloud"
            else None,
        )

    except KeyboardInterrupt:
        logger.debug("Shutting down...")

    except Exception as e:
        rprint(f"[red]Error: {e}[/red]")
        raise click.Abort()


def _set_env_vars_from_profile(profile: Auth):
    if profile.api_key:
        _set_env_vars(profile.api_key, profile.api_url)
    _set_project_id_from_profile(profile)


def _set_env_vars_from_env(env_vars: dict[str, str]):
    key = env_vars.get("LLAMA_CLOUD_API_KEY")
    url = env_vars.get("LLAMA_CLOUD_BASE_URL", "https://api.cloud.llamaindex.ai")
    # Also propagate project id if present in the environment
    _set_project_id_from_env(env_vars)
    if key:
        _set_env_vars(key, url)


def _set_env_vars(key: str, url: str):
    os.environ["LLAMA_CLOUD_API_KEY"] = key
    os.environ["LLAMA_CLOUD_BASE_URL"] = url
    # kludge for common web servers to inject local auth key
    for prefix in ["VITE_", "NEXT_PUBLIC_"]:
        os.environ[f"{prefix}LLAMA_CLOUD_API_KEY"] = key
        os.environ[f"{prefix}LLAMA_CLOUD_BASE_URL"] = url


def _set_project_id_from_env(env_vars: dict[str, str]):
    project_id = env_vars.get("LLAMA_DEPLOY_PROJECT_ID")
    if project_id:
        os.environ["LLAMA_DEPLOY_PROJECT_ID"] = project_id


def _set_project_id_from_profile(profile: Auth):
    if profile.project_id:
        os.environ["LLAMA_DEPLOY_PROJECT_ID"] = profile.project_id


def _maybe_inject_llama_cloud_credentials(
    deployment_file: Path, interactive: bool, require_cloud: bool
) -> None:
    """If the deployment config indicates Llama Cloud usage, ensure LLAMA_CLOUD_API_KEY is set.

    Behavior:
    - If LLAMA_CLOUD_API_KEY is already set, do nothing.
    - Else, try to read current profile's api_key and inject.
    - If no profile/api_key and session is interactive, prompt to log in and inject afterward.
    - If user declines or session is non-interactive, warn that deployment may not work.
    """
    # Read config directly to avoid cached global settings
    try:
        config = read_deployment_config_from_git_root_or_cwd(
            Path.cwd(), deployment_file
        )
    except Exception:
        rprint(
            "[red]Error: Could not read a deployment config. This doesn't appear to be a valid llama-deploy project.[/red]"
        )
        raise click.Abort()

    if not config.llama_cloud and not require_cloud:
        return

    # Import lazily to avoid loading appserver dependencies on general CLI startup
    from llama_deploy.appserver.workflow_loader import parse_environment_variables

    vars = parse_environment_variables(
        config, deployment_file.parent if deployment_file.is_file() else deployment_file
    )

    # Ensure project id is available to the app and UI processes
    _set_project_id_from_env({**os.environ, **vars})

    existing = os.environ.get("LLAMA_CLOUD_API_KEY") or vars.get("LLAMA_CLOUD_API_KEY")
    if existing:
        _set_env_vars_from_env({**os.environ, **vars})
        return

    env = service.get_current_environment()
    if not env.requires_auth:
        rprint(
            f"[{WARNING}]Warning: This app requires Llama Cloud authentication, and no LLAMA_CLOUD_API_KEY is present. The app may not work.[/]"
        )
        return

    auth_svc = service.current_auth_service()
    profile = auth_svc.get_current_profile()
    if profile and profile.api_key:
        _set_env_vars_from_profile(profile)
        return

    # No key available; consider prompting if interactive
    if interactive:
        should_login = questionary.confirm(
            "This deployment requires Llama Cloud. Login now to inject credentials? Otherwise the app may not work.",
            default=True,
        ).ask()
        if should_login:
            authed = validate_authenticated_profile(True)
            if authed.api_key:
                _set_env_vars_from_profile(authed)
                return
        rprint(
            f"[{WARNING}]Warning: No Llama Cloud credentials configured. The app may not work.[/]"
        )
        return

    # Non-interactive session
    rprint(
        f"[{WARNING}]Warning: LLAMA_CLOUD_API_KEY is not set and no logged-in profile was found. The app may not work.[/]"
    )
