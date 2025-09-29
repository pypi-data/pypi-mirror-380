"""
HLA-Compass CLI for module development
"""

import copy
import os
import sys
import json
import shutil
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Any
import importlib
import importlib.util

import click
from rich.console import Console
from rich.progress import (
    Progress,
    SpinnerColumn,
    TextColumn,
    BarColumn,
    TimeElapsedColumn,
)
from rich.prompt import Confirm, Prompt
from rich.syntax import Syntax
from rich.panel import Panel
from rich.table import Table
import logging

from . import __version__
from .testing import ModuleTester
from .auth import Auth
from .config import Config
from .signing import ModuleSigner
from .mcp import build_mcp_descriptor
from .client import APIClient

try:  # pragma: no cover - Python <3.8 compatibility
    import importlib.metadata as importlib_metadata
except Exception:  # pragma: no cover
    import importlib_metadata  # type: ignore


OPTIONAL_DEP_GROUPS = {
    "wizard": {
        "modules": ["questionary", "jinja2"],
        "extra": "wizard",
        "description": "Module wizard (interactive scaffolding)",
    },
    "devserver": {
        "modules": ["watchdog", "aiohttp"],
        "extra": "devserver",
        "description": "Hot-reload dev server",
    },
    "data": {
        "modules": ["pandas", "xlsxwriter"],
        "extra": "data",
        "description": "Data exports (CSV/Excel)",
    },
    "ml": {
        "modules": ["scikit-learn", "torch", "transformers"],
        "extra": "ml",
        "description": "ML inference helpers",
    },
}

console = Console()


VERBOSE_MODE = False
_VERBOSE_INITIALIZED = False


def _deprecated_compute_option(
    _ctx: click.Context, _param: click.Option, value: str | None
) -> None:
    """Warn when the legacy --compute flag is used."""

    if value is None:
        return

    if value and value.lower() != "docker":
        console.print(
            "[yellow]⚠️ The `--compute` option is no longer supported; modules now "
            "always build for Docker runtimes. Ignoring requested compute type "
            f"'{value}'.[/yellow]"
        )
    else:
        console.print(
            "[yellow]⚠️ The `--compute` option is deprecated; Docker is the "
            "default runtime and no extra flag is required.[/yellow]"
        )


def _enable_verbose(ctx: click.Context | None = None):
    """Turn on verbose logging globally and remember the state."""
    global VERBOSE_MODE, _VERBOSE_INITIALIZED
    VERBOSE_MODE = True
    if ctx is not None:
        ctx.ensure_object(dict)
        ctx.obj["verbose"] = True

    if not _VERBOSE_INITIALIZED:
        logging.basicConfig(level=logging.DEBUG)
        _VERBOSE_INITIALIZED = True
        console.log("Verbose mode enabled")

    logging.getLogger().setLevel(logging.DEBUG)


def _ensure_verbose(ctx: click.Context | None = None):
    """Apply verbose mode when previously enabled on the parent context."""
    if ctx is None:
        return
    ctx.ensure_object(dict)
    if ctx.obj.get("verbose"):
        _enable_verbose(ctx)


def _handle_command_verbose(ctx: click.Context, _param: click.Option, value: bool):
    if value:
        _enable_verbose(ctx)
    return value


def _parse_image_reference(image: str) -> tuple[str | None, str | None]:
    """Return (repository, tag) tuple from an OCI image reference."""

    if not image:
        return None, None

    reference = image.split("@", 1)[0]
    last_segment = reference.rsplit("/", 1)[-1]
    if ":" in last_segment:
        repo_candidate, tag_candidate = reference.rsplit(":", 1)
        if "/" in tag_candidate:
            return reference, None
        return repo_candidate, tag_candidate
    return reference, None


def verbose_option(command):
    """Decorator to add --verbose flag to commands."""
    return click.option(
        "--verbose",
        is_flag=True,
        expose_value=False,
        is_eager=True,
        help="Enable verbose logging output for troubleshooting",
        callback=_handle_command_verbose,
    )(command)


def load_sdk_config() -> dict | None:
    """Load SDK configuration from config file"""
    try:
        config_path = Config.get_config_path()
        if config_path.exists():
            with open(config_path) as f:
                return json.load(f)
    except Exception:
        pass
    return None


@click.group()
@click.option(
    "--verbose",
    is_flag=True,
    help="Enable verbose logging output for troubleshooting",
)
@click.version_option(version=__version__)
@click.pass_context
def cli(ctx: click.Context, verbose: bool):
    """HLA-Compass SDK - Module development tools"""
    ctx.ensure_object(dict)
    ctx.obj["verbose"] = bool(verbose)
    if verbose:
        _enable_verbose(ctx)
    else:
        logging.getLogger().setLevel(logging.INFO)


@cli.command()
@verbose_option
@click.option("--json", "output_json", is_flag=True, help="Emit diagnostics as JSON")
def doctor(output_json: bool):
    """Run environment diagnostics and suggest next steps."""
    results = _run_doctor_checks()

    if output_json:
        console.print(json.dumps(results, indent=2, default=str))
        return

    _render_doctor_results(results)


def _run_doctor_checks() -> dict[str, Any]:
    auth = Auth()
    config_dir = Config.get_config_dir()
    env = Config.get_environment()
    api = Config.get_api_endpoint()

    rate_limit_settings = Config.get_rate_limit_settings()
    rate_limit_env = {
        "HLA_RATE_LIMIT_MAX_REQUESTS": os.getenv("HLA_RATE_LIMIT_MAX_REQUESTS"),
        "HLA_RATE_LIMIT_TIME_WINDOW": os.getenv("HLA_RATE_LIMIT_TIME_WINDOW"),
    }

    auth_status = {
        "authenticated": auth.is_authenticated(),
        "credentials_path": str(Config.get_credentials_path()),
        "config_dir": str(config_dir),
    }

    tooling = {
        "docker": _command_available(["docker", "version"]),
        "node": _command_available(["node", "--version"]),
        "npm": _command_available(["npm", "--version"]),
    }

    optional_deps: list[dict[str, Any]] = []
    for group, data in OPTIONAL_DEP_GROUPS.items():
        modules_info = []
        available = True
        for module_name in data["modules"]:
            status = _inspect_dependency(module_name)
            modules_info.append(status)
            if not status["available"]:
                available = False
        optional_deps.append(
            {
                "group": group,
                "description": data["description"],
                "extra": data["extra"],
                "available": available,
                "modules": modules_info,
            }
        )

    next_steps: list[str] = []
    if not auth_status["authenticated"]:
        next_steps.append("Run 'hla-compass auth login' to authenticate with the platform.")

    if not tooling["docker"]["available"]:
        next_steps.append("Install and start Docker to build and run module containers.")

    for dep in optional_deps:
        if not dep["available"]:
            next_steps.append(
                f"Install missing {dep['description']} dependencies with: pip install 'hla-compass[{dep['extra']}]'"
            )

    if not any(rate_limit_env.values()):
        next_steps.append(
            "Set HLA_RATE_LIMIT_MAX_REQUESTS / HLA_RATE_LIMIT_TIME_WINDOW to tune client throughput (optional)."
        )

    return {
        "environment": {
            "sdk_version": __version__,
            "environment": env,
            "api_endpoint": api,
        },
        "auth": auth_status,
        "rate_limits": {
            "env": rate_limit_env,
            "effective": rate_limit_settings,
        },
        "tooling": tooling,
        "optional_dependencies": optional_deps,
        "next_steps": next_steps,
    }




def _command_available(cmd: list[str]) -> dict[str, Any]:
    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        available = result.returncode == 0
        version = result.stdout.strip() or result.stderr.strip()
        return {"available": available, "output": version}
    except FileNotFoundError:
        return {"available": False, "output": "not installed"}

def _inspect_dependency(module_name: str) -> dict[str, Any]:
    spec = importlib.util.find_spec(module_name)
    available = spec is not None
    version = None
    if available:
        try:
            version = importlib_metadata.version(module_name)
        except importlib_metadata.PackageNotFoundError:
            version = "unknown"
    return {
        "module": module_name,
        "available": available,
        "version": version,
    }


def _render_doctor_results(results: dict[str, Any]) -> None:
    env = results["environment"]
    auth = results["auth"]
    rate_limits = results["rate_limits"]
    deps = results["optional_dependencies"]
    next_steps = results.get("next_steps", [])

    console.print(
        Panel.fit(
            f"[bold]Environment[/bold]\n"
            f"SDK Version: [cyan]{env['sdk_version']}[/cyan]\n"
            f"Environment: [cyan]{env['environment']}[/cyan]\n"
            f"API Endpoint: [cyan]{env['api_endpoint']}[/cyan]",
            title="hla-compass doctor",
            border_style="bright_cyan",
        )
    )

    auth_msg = (
        "Authenticated ✅" if auth["authenticated"] else "Not authenticated ❌"
    )
    console.print(
        Panel.fit(
            f"[bold]Authentication[/bold]\n"
            f"Status: {auth_msg}\n"
            f"Config dir: {auth['config_dir']}\n"
            f"Credentials file: {auth['credentials_path']}",
            border_style="green" if auth["authenticated"] else "red",
        )
    )

    rate_table = Table(title="Rate Limit Settings", show_header=True, header_style="bold")
    rate_table.add_column("Variable")
    rate_table.add_column("Value")
    for key, value in rate_limits["env"].items():
        rate_table.add_row(key, str(value) if value else "<not set>")
    rate_table.add_row(
        "effective.max_requests",
        str(rate_limits["effective"].get("max_requests", "default")),
    )
    rate_table.add_row(
        "effective.time_window",
        str(rate_limits["effective"].get("time_window", "default")),
    )
    console.print(rate_table)

    tooling = results["tooling"]
    tooling_table = Table(title="Tooling", show_header=True, header_style="bold")
    tooling_table.add_column("Tool")
    tooling_table.add_column("Status")
    tooling_table.add_column("Details")
    for name, info in tooling.items():
        status = "✅" if info["available"] else "⚠️"
        details = info.get("output") or ""
        tooling_table.add_row(name, status, details)
    console.print(tooling_table)

    dep_table = Table(title="Optional Dependencies", show_header=True, header_style="bold")
    dep_table.add_column("Group")
    dep_table.add_column("Status")
    dep_table.add_column("Modules")
    dep_table.add_column("Install Hint")

    for dep in deps:
        status = "✅" if dep["available"] else "⚠️"
        modules = ", ".join(
            f"{m['module']}({m['version']})" if m["available"] else f"{m['module']} (missing)"
            for m in dep["modules"]
        )
        hint = "—" if dep["available"] else f"pip install 'hla-compass[{dep['extra']}]'"
        dep_table.add_row(dep["description"], status, modules, hint)

    console.print(dep_table)

    if next_steps:
        console.print("\n[bold]Next steps:[/bold]")
        for step in next_steps:
            console.print(f"  • {step}")
    else:
        console.print("\n[bold green]All checks passed. You're ready to build![/bold green]")


ALITHEA_BANNER = """
        [bold bright_magenta]█████╗[/bold bright_magenta] [bold bright_cyan]██╗[/bold bright_cyan]     [bold bright_green]██╗[/bold bright_green][bold bright_yellow]████████╗[/bold bright_yellow][bold bright_red]██╗  ██╗[/bold bright_red][bold bright_magenta]███████╗[/bold bright_magenta] [bold bright_cyan]█████╗[/bold bright_cyan]
       [bold bright_magenta]██╔══██╗[/bold bright_magenta][bold bright_cyan]██║[/bold bright_cyan]     [bold bright_green]██║[/bold bright_green][bold bright_yellow]╚══██╔══╝[/bold bright_yellow][bold bright_red]██║  ██║[/bold bright_red][bold bright_magenta]██╔════╝[/bold bright_magenta][bold bright_cyan]██╔══██╗[/bold bright_cyan]
       [bold bright_magenta]███████║[/bold bright_magenta][bold bright_cyan]██║[/bold bright_cyan]     [bold bright_green]██║[/bold bright_green][bold bright_yellow]   ██║[/bold bright_yellow]   [bold bright_red]███████║[/bold bright_red][bold bright_magenta]█████╗[/bold bright_magenta]  [bold bright_cyan]███████║[/bold bright_cyan]
       [bold bright_magenta]██╔══██║[/bold bright_magenta][bold bright_cyan]██║[/bold bright_cyan]     [bold bright_green]██║[/bold bright_green][bold bright_yellow]   ██║[/bold bright_yellow]   [bold bright_red]██╔══██║[/bold bright_red][bold bright_magenta]██╔══╝[/bold bright_magenta]  [bold bright_cyan]██╔══██║[/bold bright_cyan]
       [bold bright_magenta]██║  ██║[/bold bright_magenta][bold bright_cyan]███████╗[/bold bright_cyan][bold bright_green]██║[/bold bright_green][bold bright_yellow]   ██║[/bold bright_yellow]   [bold bright_red]██║  ██║[/bold bright_red][bold bright_magenta]███████╗[/bold bright_magenta][bold bright_cyan]██║  ██║[/bold bright_cyan]
       [bold bright_magenta]╚═╝  ╚═╝[/bold bright_magenta][bold bright_cyan]╚══════╝[/bold bright_cyan][bold bright_green]╚═╝[/bold bright_green][bold bright_yellow]   ╚═╝[/bold bright_yellow]   [bold bright_red]╚═╝  ╚═╝[/bold bright_red][bold bright_magenta]╚══════╝[/bold bright_magenta][bold bright_cyan]╚═╝  ╚═╝[/bold bright_cyan]

                  [bold bright_white]🧬  B I O I N F O R M A T I C S  🧬[/bold bright_white]
"""


def show_banner():
    """Display the Alithea banner with helpful context"""
    console.print(ALITHEA_BANNER)
    env = Config.get_environment()
    api = Config.get_api_endpoint()

    # Color-coded environment indicator
    env_color = {"dev": "green", "staging": "yellow", "prod": "red"}.get(env, "cyan")

    info = (
        f"[bold bright_white]HLA-Compass Platform SDK[/bold bright_white]\n"
        f"[dim white]Version[/dim white] [bold bright_cyan]{__version__}[/bold bright_cyan]   "
        f"[dim white]Environment[/dim white] [bold {env_color}]{env.upper()}[/bold {env_color}]\n"
        f"[dim white]API Endpoint[/dim white] [bright_blue]{api}[/bright_blue]\n"
        f"[bright_magenta]✨[/bright_magenta] [italic]Immuno-Peptidomics • Module Development • AI-Powered Analysis[/italic] [bright_magenta]✨[/bright_magenta]"
    )
    console.print(
        Panel.fit(
            info,
            title="[bold bright_cyan]🔬 Alithea Bio[/bold bright_cyan]",
            subtitle="[bright_blue]https://alithea.bio[/bright_blue]",
            border_style="bright_cyan",
            padding=(1, 2),
        )
    )


@cli.command()
@verbose_option
@click.option("--force", is_flag=True, help="Overwrite existing configuration and keys")
@click.option(
    "--env",
    type=click.Choice(["dev", "staging", "prod"]),
    default="dev",
    help="Default environment",
)
@click.option(
    "--api-endpoint", help="Custom API endpoint (overrides environment default)"
)
@click.option("--organization", help="Your organization name")
@click.option("--author-name", help="Your name for module authorship")
@click.option("--author-email", help="Your email for module authorship")
@click.pass_context
def configure(
    ctx: click.Context,
    force: bool,
    env: str,
    api_endpoint: str | None,
    organization: str | None,
    author_name: str | None,
    author_email: str | None,
):
    """Set up initial SDK configuration and generate RSA keypair for signing"""
    _ensure_verbose(ctx)
    console.print("[bold blue]HLA-Compass SDK Configuration[/bold blue]\n")

    # Get configuration directory
    config_path = Config.get_config_path()

    # Check if configuration already exists
    if config_path.exists() and not force:
        console.print(f"[yellow]Configuration already exists at {config_path}[/yellow]")
        if not Confirm.ask("Do you want to update the existing configuration?"):
            console.print("Configuration cancelled.")
            return
        force = True

    try:
        # Initialize module signer
        signer = ModuleSigner()

        # Check for existing keys
        keys_exist = (
            signer.private_key_path.exists() and signer.public_key_path.exists()
        )

        if keys_exist and not force:
            console.print(
                f"[yellow]RSA keypair already exists at {signer.keys_dir}[/yellow]"
            )
            regenerate_keys = Confirm.ask("Do you want to regenerate the RSA keypair?")
        else:
            regenerate_keys = True

        # Generate or regenerate keys if needed
        if regenerate_keys:
            console.print("🔐 Generating RSA keypair for module signing...")
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                console=console,
            ) as progress:
                task = progress.add_task(
                    "Generating 4096-bit RSA keypair...", total=None
                )

                try:
                    private_path, public_path = signer.generate_keys(force=force)
                    progress.update(task, description="Keys generated successfully!")
                    console.print(f"  ✓ Private key: {private_path}")
                    console.print(f"  ✓ Public key: {public_path}")
                    console.print(
                        f"  ✓ Key fingerprint: {signer.get_key_fingerprint()}"
                    )
                except Exception as e:
                    console.print(f"[red]Error generating keys: {e}[/red]")
                    sys.exit(1)
        else:
            console.print(f"✓ Using existing RSA keypair at {signer.keys_dir}")
            console.print(f"  Key fingerprint: {signer.get_key_fingerprint()}")

        # Collect configuration parameters
        console.print("\n[bold]Configuration Setup[/bold]")

        # Use provided values or prompt for input
        if not api_endpoint:
            api_endpoint = Config.API_ENDPOINTS.get(env)

        if not organization:
            organization = Prompt.ask(
                "Organization name",
                default=os.environ.get("HLA_AUTHOR_ORG", "Independent"),
            )

        if not author_name:
            author_name = Prompt.ask(
                "Your name (for module authorship)",
                default=os.environ.get(
                    "HLA_AUTHOR_NAME", os.environ.get("USER", "Developer")
                ),
            )

        if not author_email:
            author_email = Prompt.ask(
                "Your email (for module authorship)",
                default=os.environ.get(
                    "HLA_AUTHOR_EMAIL",
                    f"{author_name.lower().replace(' ', '.')}@example.com",
                ),
            )

        # Create configuration
        config_data = {
            "version": "1.0",
            "environment": env,
            "api_endpoint": api_endpoint,
            "organization": organization,
            "author": {"name": author_name, "email": author_email},
            "signing": {
                "algorithm": signer.ALGORITHM,
                "hash_algorithm": signer.HASH_ALGORITHM,
                "key_fingerprint": signer.get_key_fingerprint(),
                "private_key_path": str(signer.private_key_path),
                "public_key_path": str(signer.public_key_path),
            },
        }

        # Add timestamp
        import datetime

        config_data["created_at"] = datetime.datetime.now().isoformat()

        # Save configuration
        with open(config_path, "w") as f:
            json.dump(config_data, f, indent=2)

        console.print(f"\n[green]✓ Configuration saved to {config_path}[/green]\n")

        # Display configuration summary
        config_table = Table(title="SDK Configuration Summary")
        config_table.add_column("Setting", style="cyan")
        config_table.add_column("Value", style="white")

        config_table.add_row("Environment", env)
        config_table.add_row("API Endpoint", api_endpoint)
        config_table.add_row("Organization", organization)
        config_table.add_row("Author", f"{author_name} <{author_email}>")
        config_table.add_row("Keys Directory", str(signer.keys_dir))
        config_table.add_row(
            "Signing Algorithm", f"{signer.ALGORITHM} with {signer.HASH_ALGORITHM}"
        )

        console.print(config_table)

        console.print("\n[bold]Next Steps:[/bold]")
        console.print("• Create a module: [cyan]hla-compass init my-module[/cyan]")
        console.print("• Build and sign: [cyan]hla-compass build[/cyan]")
        console.print("• Publish to platform: [cyan]hla-compass publish[/cyan]")

    except Exception as e:
        console.print(f"[red]Configuration failed: {e}[/red]")
        sys.exit(1)


@cli.command()
@verbose_option
@click.argument("name", required=False)
@click.option(
    "--template",
    type=click.Choice(["ui", "no-ui"]),
    default="no-ui",
    help="Module template: 'ui' for modules with user interface, 'no-ui' for backend-only (default: no-ui)"
)
@click.option(
    "--interactive", "-i",
    is_flag=True,
    help="Use interactive wizard to create module with custom configuration"
)
@click.option(
    "--compute",
    hidden=True,
    callback=_deprecated_compute_option,
    expose_value=False,
)
@click.option("--no-banner", is_flag=True, help="Skip the Alithea banner display")
@click.option(
    "--yes", is_flag=True, help="Assume yes for all prompts (non-interactive mode)"
)
@click.pass_context
def init(
    ctx: click.Context,
    name: str | None,
    template: str,
    interactive: bool,
    no_banner: bool,
    yes: bool,
):
    """Create a new HLA-Compass module

    Examples:
        hla-compass init my-module # Backend-only module (no UI)
        hla-compass init my-module --template ui # Module with user interface
        hla-compass init --interactive                # Interactive wizard (recommended)
        hla-compass init my-module -i # Interactive wizard with name
    """
    _ensure_verbose(ctx)

    # Show the beautiful Alithea banner only during module creation
    if not no_banner:
        show_banner()
    
    # Use an interactive wizard if requested
    if interactive:
        try:
            from .wizard import run_wizard
            from .generators import CodeGenerator
        except ModuleNotFoundError as exc:
            if exc.name in {"questionary", "jinja2"}:
                console.print(
                    "[red]Interactive wizard dependencies are not installed.[/red] "
                    "Install them with `[bold]pip install 'hla-compass[wizard]'[/bold]` "
                    "or `pip install questionary jinja2` and re-run `hla-compass init -i`."
                )
                return
            raise
        
        console.print("[bold cyan]🎯 Starting Interactive Module Wizard[/bold cyan]\n")
        
        # Run the wizard
        config = run_wizard()
        if not config:
            console.print("[yellow]Module creation cancelled[/yellow]")
            return
        
        # Use the provided name if given, otherwise use wizard name
        if name:
            config['name'] = name
        module_name = config['name']
        
        # Create module directory
        module_dir = Path(module_name)
        if module_dir.exists() and not yes:
            if not Confirm.ask(f"Directory '{module_name}' already exists. Continue?"):
                return
        
        # Generate module from wizard configuration
        generator = CodeGenerator()
        success = generator.generate_module(config, module_dir)
        
        if success:
            console.print(Panel.fit(
                f"[green]✓ Module '{module_name}' created successfully![/green]\n\n"
                f"[bold]Generated from wizard configuration:[/bold]\n"
                f"• Type: {'UI Module' if config.get('has_ui') else 'Backend Module'}\n"
                f"• Inputs: {len(config.get('inputs', {}))} parameters\n"
                f"• Outputs: {len(config.get('outputs', {}))} fields\n"
                f"• Dependencies: {len(config.get('dependencies', []))} packages\n\n"
                f"[bold]Next steps:[/bold]\n"
                f"1. cd {module_name}\n"
                f"2. pip install -r backend/requirements.txt\n"
                f"3. hla-compass dev  # Start hot-reload server\n\n"
                f"[dim]The wizard has generated working code based on your specifications.\n"
                f"Edit backend/main.py to customize the processing logic.[/dim]",
                title="Module Created with Wizard",
                border_style="green",
                width=100
            ))
        else:
            console.print("[red]Failed to generate module from wizard configuration[/red]")
        return
    
    # Standard template-based creation (non-interactive)
    if not name:
        console.print("[red]Module name is required when not using --interactive[/red]")
        console.print("Usage: hla-compass init MODULE_NAME")
        console.print("   Or: hla-compass init --interactive")
        return

    # Determine a module type from the template
    module_type = "with-ui" if template == "ui" else "no-ui"
    
    # Map template names to actual template directories
    template_dir_name = f"{template}-template"

    console.print(
        f"[bold green]🧬 Creating HLA-Compass Module: [white]{name}[/white] 🧬[/bold green]"
    )
    console.print(
        f"[dim]Template: {template} • Type: {module_type} • Runtime: Docker container[/dim]\n"
    )

    # Check if the directory already exists
    module_dir = Path(name)
    if module_dir.exists():
        if not yes and not Confirm.ask(f"Directory '{name}' already exists. Continue?"):
            return

    # Find template directory
    pkg_templates_dir = Path(__file__).parent / "templates" / template_dir_name
    
    if not pkg_templates_dir.exists():
        console.print(f"[red]Template '{template}' not found[/red]")
        console.print("[yellow]Available templates:[/yellow]")
        console.print("  • no-ui - Backend-only module without user interface")
        console.print("  • ui    - Module with React/TypeScript user interface")
        return
    
    template_dir = pkg_templates_dir

    # Copy template
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("Copying template files...", total=None)

        shutil.copytree(template_dir, module_dir, dirs_exist_ok=True)

        progress.update(task, description="Updating manifest...")

        # Update manifest.json
        manifest_path = module_dir / "manifest.json"
        with open(manifest_path, "r") as f:
            manifest = json.load(f)

        manifest["name"] = name
        manifest["type"] = module_type
        manifest["computeType"] = "docker"

        # Load author information from SDK config, then environment, then defaults
        sdk_config = load_sdk_config()
        author_info = sdk_config.get("author", {}) if sdk_config else {}

        manifest["author"]["name"] = (
            author_info.get("name") or
            os.environ.get("HLA_AUTHOR_NAME") or
            os.environ.get("USER", "Unknown")
        )
        manifest["author"]["email"] = author_info.get("email") or os.environ.get(
            "HLA_AUTHOR_EMAIL", "developer@example.com"
        )
        manifest["author"]["organization"] = (
            sdk_config.get("organization") if sdk_config else None
        ) or os.environ.get("HLA_AUTHOR_ORG", "Independent")
        manifest["description"] = os.environ.get(
            "HLA_MODULE_DESC", f"HLA-Compass module: {name}"
        )

        # Show what was set
        console.print(f"  Author: {manifest['author']['name']}")
        console.print(f"  Email: {manifest['author']['email']}")
        console.print(f"  Organization: {manifest['author']['organization']}")

        with open(manifest_path, "w") as f:
            json.dump(manifest, f, indent=2)

        # Remove the frontend directory if no-ui
        if module_type == "no-ui":
            frontend_dir = module_dir / "frontend"
            if frontend_dir.exists():
                shutil.rmtree(frontend_dir)

        # Create a virtual environment only if not already in one
        if hasattr(sys, "real_prefix") or (
            hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix
        ):
            progress.update(
                task, description="Skipping venv (already in virtual environment)..."
            )
        else:
            progress.update(task, description="Creating virtual environment...")
            result = subprocess.run(
                [sys.executable, "-m", "venv", str(module_dir / "venv")],
                capture_output=True,
                text=True,
            )
            if result.returncode != 0:
                console.print(
                    f"[red]Failed to create virtual environment.[/red]\n"
                    f"stdout: {result.stdout or '<<empty>>'}"
                )
                if result.stderr:
                    console.print(f"[red]stderr:[/red] {result.stderr}")
                console.print(
                    "[yellow]Resolve the venv issue (ensure 'venv' module is available) and rerun 'hla-compass init'.[/yellow]"
                )
                sys.exit(result.returncode)

        progress.update(task, description="Module created!", completed=True)

    # Display a comprehensive success message with full workflow
    ui_specific = ""
    if module_type == "with-ui":
        ui_specific = (
            f"• Edit frontend/index.tsx for UI components\n"
            f"• Install frontend deps: cd frontend && npm install\n"
        )
    
    console.print(
        Panel.fit(
            f"[green]✓ Module '{name}' created successfully![/green]\n\n"
            f"[bold]Template Type:[/bold] {template.upper()} ({'With UI' if module_type == 'with-ui' else 'Backend-only'})\n\n"
            f"[bold]Quick Start:[/bold]\n"
            f"1. cd {name}\n"
            f"2. pip install -r backend/requirements.txt  # Install Python dependencies\n"
            f"3. hla-compass test                         # Test locally\n\n"
            f"[bold]Development:[/bold]\n"
            f"• Edit backend/main.py to implement your logic\n"
            f"{ui_specific}"
            f"• Add test data to examples/sample_input.json\n"
            f"• Test: hla-compass test --input examples/sample_input.json\n\n"
            f"[bold]Deployment:[/bold]\n"
            f"• Configure: hla-compass configure\n"
            f"• Build: hla-compass build\n"
            f"• Publish: hla-compass publish --env dev\n\n"
            f"[bold]Documentation:[/bold]\n"
            f"• Templates guide: sdk/python/hla_compass/templates/README.md\n"
            f"• SDK docs: https://docs.alithea.bio",
            title=f"Module Created - {'UI' if module_type == 'with-ui' else 'No-UI'} Template",
            width=100,
        )
    )


@cli.command()
@verbose_option
@click.option("--manifest", default="manifest.json", help="Path to manifest.json")
@click.option(
    "--json", "output_json", is_flag=True, help="Output as JSON for automation"
)
@click.pass_context
def validate(ctx: click.Context, manifest: str, output_json: bool):
    """Validate module structure and manifest"""
    _ensure_verbose(ctx)

    if not output_json:
        console.print("[bold]Validating module...[/bold]")

    errors = []
    warnings = []

    # Check manifest exists
    manifest_path = Path(manifest)
    if not manifest_path.exists():
        if output_json:
            result = {
                "valid": False,
                "errors": ["manifest.json not found"],
                "warnings": [],
            }
            print(json.dumps(result))
        else:
            console.print("[red]✗ manifest.json not found[/red]")
        sys.exit(1)

    # Load and validate manifest
    try:
        with open(manifest_path, "r") as f:
            manifest_data = json.load(f)
    except json.JSONDecodeError as e:
        if output_json:
            result = {
                "valid": False,
                "errors": [f"Invalid JSON in manifest.json: {e}"],
                "warnings": [],
            }
            print(json.dumps(result))
        else:
            console.print(f"[red]✗ Invalid JSON in manifest.json: {e}[/red]")
        sys.exit(1)

    # Required fields
    required_fields = [
        "name",
        "version",
        "type",
        "computeType",
        "author",
        "inputs",
        "outputs",
    ]
    for field in required_fields:
        if field not in manifest_data:
            errors.append(f"Missing required field: {field}")

    # Check backend structure
    module_dir = manifest_path.parent
    backend_dir = module_dir / "backend"

    if not backend_dir.exists():
        errors.append("backend/ directory not found")
    else:
        if not (backend_dir / "main.py").exists():
            errors.append("backend/main.py not found")
        if not (backend_dir / "requirements.txt").exists():
            warnings.append("backend/requirements.txt not found")

    # Check frontend for with-ui modules
    if manifest_data.get("type") == "with-ui":
        frontend_dir = module_dir / "frontend"
        if not frontend_dir.exists():
            errors.append("frontend/ directory required for with-ui modules")
        elif not (frontend_dir / "index.tsx").exists():
            errors.append("frontend/index.tsx not found")

    # Display results
    if output_json:
        result = {"valid": len(errors) == 0, "errors": errors, "warnings": warnings}
        print(json.dumps(result, indent=2))
        sys.exit(0 if result["valid"] else 1)
    else:
        if errors:
            console.print("[red]✗ Validation failed with errors:[/red]")
            for error in errors:
                console.print(f"  • {error}")
            console.print(
                "\n[yellow]Fix the errors above, then run 'hla-compass validate' again[/yellow]"
            )
            sys.exit(1)
        else:
            console.print("[green]✓ Module structure valid[/green]")
            if warnings:
                console.print("\n[yellow]Warnings:[/yellow]")
                for warning in warnings:
                    console.print(f"  • {warning}")
            console.print("\n[bold]Ready for next steps:[/bold]")
            console.print("  • Test: hla-compass test")
            console.print("  • Build: hla-compass build")
            console.print("  • Publish: hla-compass publish --env dev")
            console.print("  • Register existing image: hla-compass deploy <image> --env dev")
            sys.exit(0)




def _sanitize_tag_component(value: str, fallback: str) -> str:
    normalized = []
    for char in value.lower():
        if char.isalnum() or char in {"-", "_", "."}:
            normalized.append(char)
        else:
            normalized.append("-")
    slug = "".join(normalized).strip("-.")
    return slug or fallback


def _default_image_tag(manifest: dict[str, Any]) -> str:
    name = manifest.get("name") or "module"
    version = manifest.get("version") or datetime.utcnow().strftime("%Y%m%d%H%M")
    return f"{_sanitize_tag_component(name, 'module')}:{_sanitize_tag_component(version, 'latest')}"


def _compose_registry_tag(base_tag: str, registry: str | None) -> tuple[str, str | None]:
    if not registry:
        return base_tag, None

    registry = registry.rstrip("/")
    if "//" in base_tag:
        return base_tag, base_tag
    repo = base_tag.split(":", 1)[0]
    if "/" in repo:
        return base_tag, base_tag
    return base_tag, f"{registry}/{base_tag}"


def _docker_image_metadata(image_ref: str) -> dict[str, Any]:
    try:
        result = subprocess.run(
            [
                "docker",
                "image",
                "inspect",
                image_ref,
                "--format",
                "{{json .}}",
            ],
            capture_output=True,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError:
        return {}

    payload = result.stdout.strip()
    if not payload:
        return {}

    try:
        return json.loads(payload)
    except json.JSONDecodeError:
        return {}


def _write_dist_manifest(manifest: dict[str, Any], dist_dir: Path) -> Path:
    manifest_path = dist_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return manifest_path


@cli.command()
@verbose_option
@click.option("--tag", help="Docker image tag to build (defaults to <name>:<version>)")
@click.option(
    "--registry",
    help="Registry prefix used when tagging/pushing (e.g. 1234567890.dkr.ecr.us-east-1.amazonaws.com/modules)",
)
@click.option("--push", is_flag=True, help="Push the built image after docker build")
@click.option(
    "--platform",
    multiple=True,
    help="Optional target platform(s) passed to docker build --platform",
)
@click.option("--no-sign", is_flag=True, help="Skip manifest signing (useful for local iteration)")
@click.option("--no-cache", is_flag=True, help="Disable Docker build cache")
@click.pass_context
def build(
    ctx: click.Context,
    tag: str | None,
    registry: str | None,
    push: bool,
    platform: tuple[str, ...],
    no_sign: bool,
    no_cache: bool,
):
    """Build a container image for the current module and emit MCP descriptors."""

    _ensure_verbose(ctx)
    _ensure_docker_available()

    manifest_path = Path("manifest.json")
    if not manifest_path.exists():
        console.print("[red]manifest.json not found. Run this command from your module directory.")
        sys.exit(1)

    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        console.print(f"[red]Invalid manifest.json: {exc}[/red]")
        sys.exit(1)

    working_manifest = copy.deepcopy(manifest)
    image_tag = tag or _default_image_tag(working_manifest)
    local_tag, registry_tag = _compose_registry_tag(image_tag, registry)

    dist_dir = Path("dist")
    dist_dir.mkdir(parents=True, exist_ok=True)
    mcp_dir = dist_dir / "mcp"

    descriptor_path = build_mcp_descriptor(working_manifest, mcp_dir)
    dockerfile_path = dist_dir / "Dockerfile.hla"
    dockerfile_path.write_text(
        _generate_dockerfile_content(working_manifest, descriptor_path),
        encoding="utf-8",
    )

    execution = working_manifest.setdefault("execution", {})
    execution.setdefault(
        "entrypoint",
        execution.get("entrypoint")
        or working_manifest.get("entrypoint")
        or "backend.main:Module",
    )
    execution.setdefault("supports", ["interactive", "async", "workflow"])
    execution.setdefault("defaultMode", "interactive")
    execution["image"] = registry_tag or local_tag

    signature_details: dict[str, Any] | None = None
    if no_sign:
        for field in ("signature", "publicKey", "signatureAlgorithm", "hashAlgorithm", "keyFingerprint"):
            working_manifest.pop(field, None)
    else:
        try:
            signer = ModuleSigner()
            signature = signer.sign_manifest(working_manifest)
            working_manifest["signature"] = signature
            working_manifest["publicKey"] = signer.get_public_key_string()
            working_manifest["signatureAlgorithm"] = signer.ALGORITHM
            working_manifest["hashAlgorithm"] = signer.HASH_ALGORITHM
            working_manifest["keyFingerprint"] = signer.get_key_fingerprint()
            signature_details = {
                "fingerprint": working_manifest["keyFingerprint"],
                "algorithm": working_manifest["signatureAlgorithm"],
            }
        except FileNotFoundError:
            console.print(
                "[red]Signing keys not found. Run 'hla-compass configure' or pass --no-sign.[/red]"
            )
            sys.exit(1)

    manifest_artifact = _write_dist_manifest(working_manifest, dist_dir)

    console.print("[cyan]Building Docker image...[/cyan]")
    build_cmd = ["docker", "build"]
    if platform:
        build_cmd.extend(["--platform", ",".join(platform)])
    if no_cache:
        build_cmd.append("--no-cache")
    build_cmd.extend(["-f", str(dockerfile_path), "-t", local_tag, "."])

    result = subprocess.run(build_cmd)
    if result.returncode != 0:
        console.print("[red]Docker build failed[/red]")
        sys.exit(result.returncode)

    published_tag = local_tag
    if registry_tag and registry_tag != local_tag:
        tag_cmd = ["docker", "tag", local_tag, registry_tag]
        tag_result = subprocess.run(tag_cmd)
        if tag_result.returncode != 0:
            console.print("[red]Failed to tag image for registry push[/red]")
            sys.exit(tag_result.returncode)
        published_tag = registry_tag

    pushed = False
    if push:
        console.print(f"[cyan]Pushing image {published_tag}...[/cyan]")
        push_result = subprocess.run(["docker", "push", published_tag])
        if push_result.returncode != 0:
            console.print("[red]Docker push failed[/red]")
            sys.exit(push_result.returncode)
        pushed = True

    image_meta = _docker_image_metadata(published_tag)
    digest = None
    if image_meta:
        repo_digests = image_meta.get("RepoDigests") or []
        digest = repo_digests[0] if repo_digests else image_meta.get("Id")

    build_report = {
        "image_tag": local_tag,
        "published_tag": published_tag,
        "pushed": pushed,
        "descriptor": str(descriptor_path),
        "manifest": str(manifest_artifact),
        "digest": digest,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "signature": signature_details,
    }
    (dist_dir / "build.json").write_text(json.dumps(build_report, indent=2), encoding="utf-8")

    summary = Table(title="Build Summary")
    summary.add_column("Item", style="cyan")
    summary.add_column("Value", overflow="fold")
    summary.add_row("Image", published_tag)
    summary.add_row("Local Tag", local_tag)
    summary.add_row("Descriptor", str(descriptor_path))
    summary.add_row("Manifest", str(manifest_artifact))
    summary.add_row("Pushed", "Yes" if pushed else "No")
    if digest:
        summary.add_row("Digest", digest)
    if signature_details:
        summary.add_row(
            "Signature",
            f"{signature_details['algorithm']} ({signature_details['fingerprint'][:32]}...)",
        )

    console.print(summary)

    return {
        "manifest": working_manifest,
        "manifest_path": manifest_artifact,
        "descriptor_path": descriptor_path,
        "image_tag": local_tag,
        "published_tag": published_tag,
        "pushed": pushed,
        "digest": digest,
    }


@cli.command()
@verbose_option
@click.option("--mode", type=click.Choice(["interactive", "async", "workflow"]), default="interactive", help="Execution mode to simulate")
@click.option("--image-tag", help="Custom image tag to run (defaults to {name}:dev)")
@click.option("--payload", type=click.Path(path_type=Path), help="Path to payload JSON file (defaults to generated manifest defaults)")
@click.pass_context
def dev(ctx: click.Context, mode: str, image_tag: str | None, payload: Path | None):
    """Run the module container locally with live mounts for rapid iteration."""

    _ensure_verbose(ctx)
    _ensure_docker_available()

    manifest_path = Path("manifest.json")
    if not manifest_path.exists():
        console.print("[red]manifest.json not found. Run this command from your module directory.")
        sys.exit(1)

    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        console.print(f"[red]Invalid manifest.json: {exc}[/red]")
        sys.exit(1)

    module_name = manifest.get("name", "unknown")
    default_tag = f"{module_name}:dev"

    build_result = ctx.invoke(
        build,
        tag=image_tag or default_tag,
        registry=None,
        push=False,
        platform=(),
        no_sign=True,
        no_cache=False,
    )

    dist_dir = Path("dist")
    dist_dir.mkdir(exist_ok=True)

    payload_path = payload or dist_dir / "dev-input.json"
    if payload is None:
        payload_path.write_text(
            json.dumps(_manifest_defaults(manifest), indent=2),
            encoding="utf-8",
        )

    context_path = dist_dir / "dev-context.json"
    context_payload = {
        "job_id": "dev-job",
        "user_id": "dev-user",
        "organization_id": "dev-org",
        "mode": mode,
        "tier": "foundational",
        "execution_time": datetime.utcnow().isoformat() + "Z",
    }
    context_path.write_text(json.dumps(context_payload, indent=2), encoding="utf-8")

    output_dir = dist_dir / "dev-output"
    output_dir.mkdir(exist_ok=True)

    console.print(
        Panel.fit(
            "Development run configuration",
            border_style="bright_blue",
            title="hla-compass dev",
        )
    )
    console.print(f"Payload: [cyan]{payload_path}[/cyan]")
    console.print(f"Mode: [cyan]{mode}[/cyan]")
    console.print("Edit the payload file and press Enter to re-run. Press Ctrl+C to exit.\n")

    image = (build_result or {}).get("image_tag") or image_tag or default_tag

    try:
        while True:
            _run_module_container(image, manifest_path, payload_path, context_path, output_dir)
            output_file = output_dir / "output.json"
            summary_file = output_dir / "summary.json"
            if output_file.exists():
                console.print("\n[bold green]Execution output:[/bold green]")
                console.print(output_file.read_text())
            if summary_file.exists():
                console.print("\n[bold]Summary:[/bold]")
                console.print(summary_file.read_text())
            input("\nPress Enter to re-run (Ctrl+C to exit)...")
    except KeyboardInterrupt:
        console.print("\nExiting dev loop.")




def _ensure_docker_available() -> None:
    try:
        subprocess.run(
            ["docker", "version"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
        )
    except FileNotFoundError:
        console.print("[red]Docker CLI not found. Install Docker to continue.[/red]")
        sys.exit(1)
    except subprocess.CalledProcessError as exc:
        console.print("[red]Docker is not available:[/red]")
        console.print(exc.stderr)
        sys.exit(exc.returncode)


def _generate_dockerfile_content(manifest: dict[str, Any], descriptor_path: Path) -> str:
    entrypoint = _resolve_entrypoint(manifest)
    try:
        descriptor_rel = descriptor_path.resolve().relative_to(Path.cwd())
    except ValueError:
        descriptor_rel = descriptor_path.resolve()

    frontend_dir = Path("frontend")
    has_frontend = (frontend_dir / "package.json").exists()
    frontend_lock = (frontend_dir / "package-lock.json").exists()
    frontend_yarn = (frontend_dir / "yarn.lock").exists()

    lines: list[str] = ["# syntax=docker/dockerfile:1"]

    if has_frontend:
        lines.extend(
            [
                "FROM node:20-alpine AS ui",
                "WORKDIR /ui",
                "COPY frontend/package*.json ./",
            ]
        )
        if frontend_yarn:
            lines.append("COPY frontend/yarn.lock ./")
        install_cmd = "npm ci --legacy-peer-deps" if frontend_lock else "npm install --legacy-peer-deps"
        lines.extend(
            [
                f"RUN {install_cmd}",
                "COPY frontend/ ./",
                "RUN npm run build",
            ]
        )

    lines.extend(
        [
            "FROM python:3.11-slim AS runtime",
            "ENV PYTHONDONTWRITEBYTECODE=1",
            "ENV PYTHONUNBUFFERED=1",
            "WORKDIR /app",
            "RUN pip install --no-cache-dir hla-compass",
            "COPY manifest.json /app/manifest.json",
            f"COPY {descriptor_rel.as_posix()} /app/mcp/tool.json",
        ]
    )

    backend_requirements = Path("backend/requirements.txt")
    if backend_requirements.exists():
        lines.extend(
            [
                "COPY backend/requirements.txt /tmp/backend-requirements.txt",
                "RUN pip install --no-cache-dir -r /tmp/backend-requirements.txt",
            ]
        )

    if Path("backend").exists():
        lines.append("COPY backend/ /app/backend/")
    else:
        lines.append("RUN mkdir -p /app/backend")

    if has_frontend:
        lines.extend(
            [
                "RUN mkdir -p /app/ui",
                "COPY --from=ui /ui/dist /app/ui/dist",
            ]
        )

    lines.extend(
        [
            "ENV PYTHONPATH=/app/backend:$PYTHONPATH",
            f"ENV HLA_COMPASS_MODULE={entrypoint}",
            'ENTRYPOINT ["module-runner"]',
        ]
    )

    return "\n".join(lines) + "\n"


def _resolve_entrypoint(manifest: dict[str, Any]) -> str:
    execution = manifest.get("execution", {})
    entry = execution.get("entrypoint") or manifest.get("entrypoint")
    return entry or "backend.main:Module"


def _run_module_container(
    image_tag: str,
    manifest_path: Path,
    payload_path: Path,
    context_path: Path,
    output_dir: Path,
) -> None:
    if output_dir.exists():
        for artifact in output_dir.iterdir():
            if artifact.is_file():
                artifact.unlink()

    cmd = [
        "docker",
        "run",
        "--rm",
        "-v",
        f"{payload_path.resolve()}:/var/input.json:ro",
        "-v",
        f"{context_path.resolve()}:/var/context.json:ro",
        "-v",
        f"{output_dir.resolve()}:/var/dev-out",
        "-v",
        f"{manifest_path.resolve()}:/app/manifest.json:ro",
        "-v",
        f"{(Path.cwd() / 'backend').resolve()}:/app/backend",
        "-e",
        "HLA_COMPASS_OUTPUT=/var/dev-out/output.json",
        "-e",
        "HLA_COMPASS_SUMMARY=/var/dev-out/summary.json",
        image_tag,
    ]

    result = subprocess.run(cmd)
    if result.returncode != 0:
        console.print("[red]Container run failed[/red]")
        sys.exit(result.returncode)


def _manifest_defaults(manifest: dict[str, Any]) -> dict[str, Any]:
    inputs = manifest.get("inputs", {})
    defaults: dict[str, Any] = {}

    if isinstance(inputs, dict):
        if inputs.get("type") == "object" and "properties" in inputs:
            for name, schema in inputs.get("properties", {}).items():
                if isinstance(schema, dict) and "default" in schema:
                    defaults[name] = schema["default"]
        else:
            for name, schema in inputs.items():
                if isinstance(schema, dict) and "default" in schema:
                    defaults[name] = schema["default"]

    return defaults

@cli.command()
@verbose_option
@click.argument("package_file")
@click.pass_context
def sign(ctx: click.Context, package_file: str):
    """Sign a module package"""
    _ensure_verbose(ctx)
    console.print("[bold blue]Module Signing[/bold blue]\n")

    package_path = Path(package_file)
    if not package_path.exists():
        console.print(f"[red]Error: Package file not found: {package_file}[/red]")
        sys.exit(1)

    try:
        # Check if it's a zip file (built package) or directory (module source)
        if package_path.is_file() and package_path.suffix == ".zip":
            console.print("[red]Error: Cannot sign built package directly[/red]")
            console.print("Signing must be done during the build process.")
            console.print(
                "Use 'hla-compass build' to build and sign, or use --no-sign to skip signing"
            )
            sys.exit(1)
        elif package_path.is_dir():
            # Sign module directory manifest
            from .signing import sign_module_package

            console.print(f"📦 Signing module at: {package_path}")

            signer = ModuleSigner()

            # Check if keys exist
            if not (
                signer.private_key_path.exists() and signer.public_key_path.exists()
            ):
                console.print("[red]Error: RSA keys not found[/red]")
                console.print("Run 'hla-compass configure' to generate signing keys")
                sys.exit(1)

            # Sign the module package
            updated_manifest = sign_module_package(package_path, signer)

            console.print("[green]✓ Module manifest signed successfully![/green]")
            console.print(
                f"  Algorithm: {updated_manifest.get('signatureAlgorithm', 'RSA-PSS')}"
            )
            console.print(f"  Hash: {updated_manifest.get('hashAlgorithm', 'SHA-256')}")
            console.print(
                f"  Key Fingerprint: {updated_manifest.get('keyFingerprint', 'N/A')[:32]}..."
            )

            console.print("\n[cyan]Next Steps:[/cyan]")
            console.print("• Build signed package: [cyan]hla-compass build[/cyan]")
            console.print("• Publish to platform: [cyan]hla-compass publish[/cyan]")

        else:
            console.print(f"[red]Error: Invalid package file: {package_file}[/red]")
            console.print(
                "Provide either a module directory or use 'hla-compass build' to build and sign"
            )
            sys.exit(1)

    except Exception as e:
        console.print(f"[red]Signing failed: {e}[/red]")
        sys.exit(1)



@cli.command()
@verbose_option
@click.option(
    "--env",
    type=click.Choice(["dev", "staging", "prod"]),
    default="dev",
    help="Target environment",
)
@click.option("--tag", help="Docker image tag to build (defaults to <name>:<version>)")
@click.option("--image", help="Use an existing image reference instead of building")
@click.option(
    "--registry",
    help="Registry prefix used when tagging/pushing (e.g. 1234567890.dkr.ecr.us-east-1.amazonaws.com/modules)",
)
@click.option("--push/--no-push", default=True, help="Push the image to the registry before registering")
@click.option("--no-build", is_flag=True, help="Skip build step and reuse --image")
@click.option(
    "--descriptor",
    type=click.Path(path_type=Path),
    help="Path to MCP descriptor (defaults to dist/mcp/tool.json)",
)
@click.option("--no-sign", is_flag=True, help="Skip manifest signing when building or packaging")
@click.pass_context
def publish(
    ctx: click.Context,
    env: str,
    tag: str | None,
    image: str | None,
    registry: str | None,
    push: bool,
    no_build: bool,
    descriptor: Path | None,
    no_sign: bool,
):
    """Publish a containerised module to the HLA-Compass platform."""

    _ensure_verbose(ctx)
    _ensure_docker_available()

    console.print(f"[bold blue]Publishing Module to {env.upper()}[/bold blue]\n")

    auth = Auth()
    if not auth.is_authenticated():
        console.print("[red]Error: Not authenticated. Run 'hla-compass auth login' first.[/red]")
        sys.exit(1)

    build_result: dict[str, Any] | None = None
    manifest_payload: dict[str, Any]
    descriptor_path: Path
    final_image: str
    digest: str | None = None

    if not no_build:
        build_result = ctx.invoke(
            build,
            tag=tag,
            registry=registry,
            push=push,
            platform=(),
            no_sign=no_sign,
            no_cache=False,
        )
        manifest_payload = build_result["manifest"]
        descriptor_path = Path(build_result["descriptor_path"])
        final_image = build_result["published_tag"] if push else build_result["image_tag"]
        digest = build_result.get("digest")
    else:
        if not image:
            console.print("[red]--image is required when using --no-build[/red]")
            sys.exit(1)

        manifest_path = Path("manifest.json")
        if not manifest_path.exists():
            console.print("[red]manifest.json not found. Run this command from your module directory.[/red]")
            sys.exit(1)

        try:
            manifest_payload = json.loads(manifest_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            console.print(f"[red]Invalid manifest.json: {exc}[/red]")
            sys.exit(1)

        execution = manifest_payload.setdefault("execution", {})
        execution.setdefault("supports", ["interactive", "async", "workflow"])
        execution.setdefault("defaultMode", "interactive")
        execution["image"] = image

        if not no_sign:
            try:
                signer = ModuleSigner()
                signature = signer.sign_manifest(manifest_payload)
                manifest_payload["signature"] = signature
                manifest_payload["publicKey"] = signer.get_public_key_string()
                manifest_payload["signatureAlgorithm"] = signer.ALGORITHM
                manifest_payload["hashAlgorithm"] = signer.HASH_ALGORITHM
                manifest_payload["keyFingerprint"] = signer.get_key_fingerprint()
            except FileNotFoundError:
                console.print(
                    "[yellow]Signing keys not found; continuing without signature (use --no-sign to suppress).[/yellow]"
                )
        else:
            for field in ("signature", "publicKey", "signatureAlgorithm", "hashAlgorithm", "keyFingerprint"):
                manifest_payload.pop(field, None)

        dist_dir = Path("dist")
        dist_dir.mkdir(parents=True, exist_ok=True)
        _write_dist_manifest(manifest_payload, dist_dir)

        if descriptor is not None:
            descriptor_path = descriptor
        else:
            descriptor_path = dist_dir / "mcp" / "tool.json"

        descriptor_path.parent.mkdir(parents=True, exist_ok=True)
        if not descriptor_path.exists():
            descriptor_path = build_mcp_descriptor(manifest_payload, descriptor_path.parent)

        final_image = image
        if registry:
            _, registry_tag = _compose_registry_tag(final_image, registry)
            if registry_tag and registry_tag != final_image:
                tag_result = subprocess.run(["docker", "tag", final_image, registry_tag])
                if tag_result.returncode != 0:
                    console.print("[red]Failed to tag image for registry push[/red]")
                    sys.exit(tag_result.returncode)
                final_image = registry_tag

        if push:
            console.print(f"[cyan]Pushing image {final_image}...[/cyan]")
            push_result = subprocess.run(["docker", "push", final_image])
            if push_result.returncode != 0:
                console.print("[red]Docker push failed[/red]")
                sys.exit(push_result.returncode)

        image_meta = _docker_image_metadata(final_image)
        digest = image_meta.get("RepoDigests", [None])[0] or image_meta.get("Id")

    descriptor_path_obj = Path(descriptor_path)
    if not descriptor_path_obj.exists():
        console.print(f"[red]Descriptor file not found: {descriptor_path_obj}[/red]")
        sys.exit(1)

    try:
        descriptor_payload = json.loads(descriptor_path_obj.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        console.print(f"[red]Invalid MCP descriptor: {exc}[/red]")
        sys.exit(1)

    module_name = manifest_payload.get("name", "unknown")
    module_version = manifest_payload.get("version", "0.0.0")

    client = APIClient()

    execution_block = manifest_payload.get("execution", {}) if isinstance(manifest_payload, dict) else {}
    default_mode = execution_block.get("defaultMode", "interactive")
    if isinstance(default_mode, str):
        default_mode = default_mode.lower()
    runtime_profile = execution_block.get("defaultProfile")
    if not isinstance(runtime_profile, str) or not runtime_profile:
        runtime_profile = {
            "interactive": "interactive-small",
            "async": "async-medium",
            "workflow": "workflow-large",
        }.get(default_mode, "interactive-small")

    image_repository, image_tag = _parse_image_reference(final_image)

    payload = {
        "environment": env,
        "image": final_image,
        "image_digest": digest,
        "manifest": manifest_payload,
        "descriptor": descriptor_payload,
        "runtimeProfile": runtime_profile,
    }

    if image_repository:
        payload["image_repository"] = image_repository
    if image_tag:
        payload["image_tag"] = image_tag

    try:
        response = client.register_container_module(payload)
    except Exception as exc:
        console.print(f"[red]Publication failed: {exc}[/red]")
        sys.exit(1)

    module_id = response.get("moduleId") or response.get("module_id")
    publish_notes = (
        manifest_payload.get("releaseNotes")
        or manifest_payload.get("changelog")
        or f"Published via hla-compass CLI ({datetime.utcnow().isoformat()}Z)"
    )

    if module_id:
        try:
            client.register_module(
                module_id,
                {"version": module_version, "description": publish_notes},
            )
        except Exception as exc:
            console.print(
                "[yellow]Registered container metadata but failed to mark version as published:[/yellow] "
                f"{exc}"
            )
            console.print(
                "[yellow]Run 'hla-compass publish' again or publish from the platform UI once resolved.[/yellow]"
            )
        else:
            response["published"] = True
    else:
        console.print(
            "[yellow]Module ID not returned from registry. Skipping auto-publish; please verify in platform.[/yellow]"
        )

    console.print("\n[green]🎉 Module published successfully![/green]\n")

    summary = Table(title="Publication Summary")
    summary.add_column("Item", style="cyan")
    summary.add_column("Value", overflow="fold")
    summary.add_row("Module", module_name)
    summary.add_row("Version", module_version)
    summary.add_row("Environment", env)
    summary.add_row("Image", final_image)
    if digest:
        summary.add_row("Digest", digest)
    summary.add_row("Descriptor", str(descriptor_path_obj))
    if isinstance(response, dict) and response.get("published"):
        summary.add_row("Published", "yes")

    module_id = None
    if isinstance(response, dict):
        module_id = response.get("module_id") or response.get("id")
        if module_id:
            summary.add_row("Module ID", str(module_id))

    console.print(summary)

    console.print("\n[bold]Next Steps:[/bold]")
    console.print("  • Run smoke tests: hla-compass test")
    if module_id:
        console.print(f"  • Monitor in platform: https://alithea.bio/modules/{module_id}")
    else:
        console.print("  • Monitor module telemetry in the platform UI")


@cli.command()
@verbose_option
@click.argument("image")
@click.option(
    "--env",
    type=click.Choice(["dev", "staging", "prod"]),
    default="dev",
    help="Target environment",
)
@click.option(
    "--descriptor",
    type=click.Path(path_type=Path),
    help="Path to MCP descriptor (defaults to dist/mcp/tool.json)",
)
@click.option("--push/--no-push", default=False, help="Push the image before registering")
@click.option("--registry", help="Optional registry prefix when retagging before push")
@click.option("--no-sign", is_flag=True, help="Skip manifest signing while packaging metadata")
@click.pass_context
def deploy(
    ctx: click.Context,
    image: str,
    env: str,
    descriptor: Path | None,
    push: bool,
    registry: str | None,
    no_sign: bool,
):
    """Register an already built container image."""

    ctx.invoke(
        publish,
        env=env,
        tag=None,
        image=image,
        registry=registry,
        push=push,
        no_build=True,
        descriptor=descriptor,
        no_sign=no_sign,
    )



@cli.command()
@verbose_option
@click.option(
    "--env",
    type=click.Choice(["dev", "staging", "prod"]),
    default="dev",
    help="Environment to list from",
)
@click.pass_context
def list(ctx: click.Context, env: str):
    """List deployed modules"""
    from .auth import Auth
    _ensure_verbose(ctx)

    console.print(f"[bold blue]Available Modules ({env})[/bold blue]\n")

    # Check authentication
    auth = Auth()
    if not auth.is_authenticated():
        console.print(
            "[red]Error: Not authenticated. Please run 'hla-compass auth login' first[/red]"
        )
        sys.exit(1)

    # Initialize API client
    client = APIClient()

    try:
        modules = client.list_modules()

        if not modules:
            console.print("[yellow]No modules found[/yellow]")
            console.print("Deploy a module with: hla-compass deploy <package>")
            return

        # Display modules in a table

        table = Table(show_header=True, header_style="bold cyan")
        table.add_column("Module ID", style="dim")
        table.add_column("Name")
        table.add_column("Version")
        table.add_column("Runtime")
        table.add_column("Status")

        for module in modules:
            table.add_row(
                module.get("id", "N/A"),
                module.get("name", "N/A"),
                module.get("version", "N/A"),
                module.get("compute_type", "docker"),
                module.get("status", "active"),
            )

        console.print(table)
        console.print(f"\nTotal: {len(modules)} module(s)")

    except Exception as e:
        console.print(f"[red]Error listing modules: {e}[/red]")
        sys.exit(1)








def main():
    """Main entry point for CLI"""
    cli()


if __name__ == "__main__":
    main()
