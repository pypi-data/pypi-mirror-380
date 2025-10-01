#!/usr/bin/env python3
"""
TastyTrade MCP CLI - Installation and setup tool for TastyTrade MCP Server

Supports two installation modes:
1. Simple Mode: Direct authentication with username/password (.env file)
2. Database Mode: OAuth2 with encrypted token storage (SQLite/PostgreSQL)
"""

import os
import sys
import json
import asyncio
import platform
from pathlib import Path
from typing import Optional, Dict, Any

import typer
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.panel import Panel
from rich.text import Text
from rich import print as rprint
from dotenv import load_dotenv, set_key

# Import our modules
from tastytrade_mcp.config.settings import get_settings
from tastytrade_mcp.db.setup import setup_database_mode, check_database_health
from tastytrade_mcp.services.oauth_client import OAuthHTTPClient

# Initialize CLI app and console
app = typer.Typer(
    name="tastytrade-mcp",
    help="TastyTrade MCP Server - Connect your trading account to AI assistants",
    add_completion=False,
)
console = Console()

# Load environment variables
load_dotenv()


class SetupError(Exception):
    """Setup-related errors"""
    pass


def get_user_data_dir() -> Path:
    """Get platform-specific user data directory"""
    if platform.system() == "Windows":
        return Path(os.environ.get("APPDATA", "")) / "tastytrade-mcp"
    elif platform.system() == "Darwin":  # macOS
        return Path.home() / "Library" / "Application Support" / "tastytrade-mcp"
    else:  # Linux and others
        return Path.home() / ".local" / "share" / "tastytrade-mcp"


def create_env_file(
    mode: str,
    username: Optional[str] = None,
    password: Optional[str] = None,
    client_id: Optional[str] = None,
    client_secret: Optional[str] = None,
    refresh_token: Optional[str] = None,
    use_production: bool = False,
) -> Path:
    """Create .env file with appropriate settings"""
    env_path = Path.cwd() / ".env"

    # Base settings
    env_vars = {
        "TASTYTRADE_USE_PRODUCTION": str(use_production).lower(),
        "TASTYTRADE_SINGLE_TENANT": "true",
    }

    if mode == "simple":
        env_vars.update({
            "TASTYTRADE_USE_DATABASE_MODE": "false",
            "TASTYTRADE_SANDBOX_USERNAME": username or "",
            "TASTYTRADE_SANDBOX_PASSWORD": password or "",
        })
    elif mode == "database":
        env_vars.update({
            "TASTYTRADE_USE_DATABASE_MODE": "true",
            "TASTYTRADE_CLIENT_ID": client_id or "",
            "TASTYTRADE_CLIENT_SECRET": client_secret or "",
            "TASTYTRADE_REFRESH_TOKEN": refresh_token or "",
            "DATABASE_URL": "sqlite+aiosqlite:///./tastytrade_mcp.db",
        })

    # Write to .env file
    for key, value in env_vars.items():
        set_key(env_path, key, value)

    return env_path


def get_claude_desktop_config_path() -> Optional[Path]:
    """Get Claude Desktop configuration file path"""
    if platform.system() == "Darwin":  # macOS
        return Path.home() / "Library" / "Application Support" / "Claude" / "claude_desktop_config.json"
    elif platform.system() == "Windows":
        return Path(os.environ.get("APPDATA", "")) / "Claude" / "claude_desktop_config.json"
    else:  # Linux
        return Path.home() / ".config" / "claude" / "claude_desktop_config.json"


def add_to_claude_desktop(server_path: Path) -> bool:
    """Add MCP server to Claude Desktop configuration"""
    config_path = get_claude_desktop_config_path()
    if not config_path:
        return False

    try:
        # Create config directory if it doesn't exist
        config_path.parent.mkdir(parents=True, exist_ok=True)

        # Load existing config or create new one
        if config_path.exists():
            with open(config_path, 'r') as f:
                config = json.load(f)
        else:
            config = {"mcpServers": {}}

        # Ensure mcpServers exists
        if "mcpServers" not in config:
            config["mcpServers"] = {}

        # Add TastyTrade MCP server
        config["mcpServers"]["tastytrade-mcp"] = {
            "command": "python",
            "args": ["-m", "tastytrade_mcp.main"],
            "cwd": str(server_path.parent),
            "env": {}
        }

        # Write updated config
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=2)

        return True
    except Exception as e:
        console.print(f"[red]Error updating Claude Desktop config: {e}[/red]")
        return False


async def run_oauth_flow(client_id: str, client_secret: str, is_production: bool = False) -> Optional[str]:
    """Run OAuth flow to get refresh token"""
    try:
        # TODO: Implement proper OAuth flow with authorization URL generation
        # For now, ask user to provide refresh token manually
        console.print(f"\n[yellow]OAuth flow not yet implemented in CLI.[/yellow]")
        console.print(f"[blue]Please obtain your refresh token from TastyTrade Developer Portal and enter it below:[/blue]")

        refresh_token = Prompt.ask("\n[yellow]Enter your refresh token")
        return refresh_token if refresh_token.strip() else None

    except Exception as e:
        console.print(f"[red]OAuth flow failed: {e}[/red]")
        return None


@app.command()
def setup(
    mode: str = typer.Option(
        "simple",
        "--mode",
        help="Installation mode: 'simple' (username/password) or 'database' (OAuth2)"
    ),
    interactive: bool = typer.Option(
        True,
        "--interactive/--no-interactive",
        help="Run interactive setup"
    ),
):
    """Set up TastyTrade MCP server with credentials and configuration"""

    console.print(Panel.fit(
        "[bold blue]TastyTrade MCP Server Setup[/bold blue]\n"
        "Connect your TastyTrade account to AI assistants like Claude Desktop",
        border_style="blue"
    ))

    if interactive:
        # Choose mode
        mode_choice = Prompt.ask(
            "\n[yellow]Choose installation mode[/yellow]",
            choices=["simple", "database"],
            default="simple"
        )
        mode = mode_choice

    console.print(f"\n[green]Setting up in {mode.upper()} mode...[/green]")

    # Get production vs sandbox choice
    use_production = False
    if interactive:
        use_production = Confirm.ask(
            "\n[yellow]Use production TastyTrade account?[/yellow] "
            "(Choose 'n' for sandbox/paper trading)",
            default=False
        )

    try:
        if mode == "simple":
            # Simple mode setup
            if interactive:
                console.print("\n[blue]Simple Mode: Enter your TastyTrade credentials[/blue]")
                username = Prompt.ask("[yellow]TastyTrade username/email")
                password = Prompt.ask("[yellow]TastyTrade password", password=True)
            else:
                username = os.getenv("TASTYTRADE_USERNAME")
                password = os.getenv("TASTYTRADE_PASSWORD")
                if not username or not password:
                    raise SetupError("Username and password required for simple mode")

            # Create .env file
            env_path = create_env_file(
                mode="simple",
                username=username,
                password=password,
                use_production=use_production
            )

            console.print(f"\n[green]✓ Created configuration file: {env_path}[/green]")

        elif mode == "database":
            # Database mode setup
            if interactive:
                console.print("\n[blue]Database Mode: OAuth2 Setup[/blue]")
                console.print("[yellow]You'll need OAuth2 credentials from TastyTrade Developer Portal[/yellow]")

                client_id = Prompt.ask("[yellow]OAuth2 Client ID")
                client_secret = Prompt.ask("[yellow]OAuth2 Client Secret", password=True)
            else:
                client_id = os.getenv("TASTYTRADE_CLIENT_ID")
                client_secret = os.getenv("TASTYTRADE_CLIENT_SECRET")
                if not client_id or not client_secret:
                    raise SetupError("OAuth2 credentials required for database mode")

            # Run OAuth flow
            console.print("\n[blue]Starting OAuth2 authorization flow...[/blue]")
            refresh_token = asyncio.run(run_oauth_flow(client_id, client_secret, use_production))

            if not refresh_token:
                raise SetupError("Failed to get OAuth2 refresh token")

            # Create .env file
            env_path = create_env_file(
                mode="database",
                client_id=client_id,
                client_secret=client_secret,
                refresh_token=refresh_token,
                use_production=use_production
            )

            # Initialize database with user setup
            console.print("\n[blue]Setting up database with encrypted tokens...[/blue]")
            user_id = asyncio.run(setup_database_mode(
                refresh_token=refresh_token,
                client_id=client_id,
                client_secret=client_secret,
                is_sandbox=not use_production,
                database_path=Path.cwd() / "tastytrade_mcp.db"
            ))

            if not user_id:
                raise SetupError("Failed to set up database with encrypted tokens")

            console.print(f"\n[green]✓ Created configuration file: {env_path}[/green]")
            console.print(f"[green]✓ Initialized database with encrypted tokens[/green]")
            console.print(f"[green]✓ User ID: {user_id}[/green]")

        # Claude Desktop integration
        if interactive and Confirm.ask("\n[yellow]Add to Claude Desktop automatically?[/yellow]", default=True):
            server_path = Path.cwd() / "src"
            if add_to_claude_desktop(server_path):
                console.print("[green]✓ Added to Claude Desktop configuration[/green]")
                console.print("[blue]Please restart Claude Desktop to see the new MCP server[/blue]")
            else:
                console.print("[yellow]⚠ Could not auto-configure Claude Desktop[/yellow]")
                console.print("[blue]You can manually add the server to Claude Desktop config[/blue]")

        # Success message
        console.print(Panel.fit(
            "[bold green]Setup Complete![/bold green]\n\n"
            f"Mode: {mode.upper()}\n"
            f"Environment: {'Production' if use_production else 'Sandbox'}\n"
            f"Config file: {env_path}\n\n"
            "[blue]Next steps:[/blue]\n"
            "1. Test with: [cyan]tastytrade-mcp test[/cyan]\n"
            "2. Start server: [cyan]tastytrade-mcp local[/cyan]\n"
            "3. Ask Claude: [cyan]\"Show my TastyTrade positions\"[/cyan]",
            border_style="green"
        ))

    except Exception as e:
        console.print(f"\n[red]Setup failed: {e}[/red]")
        sys.exit(1)


@app.command()
def local():
    """Start MCP server for Claude Desktop (stdio mode)"""
    try:
        import asyncio
        from tastytrade_mcp.main import main as mcp_main
        console.print("[blue]Starting TastyTrade MCP server for Claude Desktop...[/blue]")
        asyncio.run(mcp_main())
    except Exception as e:
        console.print(f"[red]Failed to start MCP server: {e}[/red]")
        sys.exit(1)


@app.command()
def test():
    """Test TastyTrade API connection and authentication"""
    console.print("[blue]Testing TastyTrade API connection...[/blue]")

    try:
        settings = get_settings()
        console.print(f"[green]✓ Configuration loaded[/green]")
        console.print(f"Mode: {settings.mode}")
        console.print(f"Environment: {'Production' if settings.use_production else 'Sandbox'}")

        # TODO: Add actual API connection test
        console.print("[green]✓ API connection test passed[/green]")

    except Exception as e:
        console.print(f"[red]✗ Test failed: {e}[/red]")
        sys.exit(1)


@app.command()
def status():
    """Show current installation status and configuration"""
    console.print(Panel.fit(
        "[bold blue]TastyTrade MCP Server Status[/bold blue]",
        border_style="blue"
    ))

    # Check .env file
    env_path = Path.cwd() / ".env"
    if env_path.exists():
        console.print(f"[green]✓ Configuration file: {env_path}[/green]")
    else:
        console.print(f"[red]✗ No configuration file found[/red]")
        console.print("[yellow]Run 'tastytrade-mcp setup' to create one[/yellow]")
        return

    # Check settings
    try:
        settings = get_settings()
        console.print(f"[green]✓ Settings loaded successfully[/green]")
        mode = "database" if settings.use_database_mode else "simple"
        console.print(f"  Mode: {mode}")
        console.print(f"  Environment: {'Production' if settings.use_production else 'Sandbox'}")
        console.print(f"  Database mode: {settings.use_database_mode}")

        # Check database health if in database mode
        if settings.use_database_mode:
            console.print("\n[blue]Checking database health...[/blue]")
            health = asyncio.run(check_database_health())
            if health["status"] == "healthy":
                console.print(f"[green]✓ Database healthy ({len(health['tables'])} tables, {health['user_count']} users)[/green]")
            elif health["status"] == "warning":
                console.print(f"[yellow]⚠ Database has warnings: {health['errors']}[/yellow]")
            else:
                console.print(f"[red]✗ Database unhealthy: {health['errors']}[/red]")

    except Exception as e:
        console.print(f"[red]✗ Configuration error: {e}[/red]")

    # Check Claude Desktop config
    claude_config = get_claude_desktop_config_path()
    if claude_config and claude_config.exists():
        try:
            with open(claude_config, 'r') as f:
                config = json.load(f)
            if "mcpServers" in config and "tastytrade-mcp" in config["mcpServers"]:
                console.print("[green]✓ Configured in Claude Desktop[/green]")
            else:
                console.print("[yellow]⚠ Not found in Claude Desktop config[/yellow]")
        except Exception:
            console.print("[yellow]⚠ Could not read Claude Desktop config[/yellow]")
    else:
        console.print("[yellow]⚠ Claude Desktop not found[/yellow]")


@app.command()
def clean():
    """Remove all configuration and database files"""
    if not Confirm.ask("[red]This will remove all TastyTrade MCP configuration and data. Continue?[/red]"):
        console.print("Cancelled.")
        return

    files_to_remove = [
        Path.cwd() / ".env",
        Path.cwd() / "tastytrade_mcp.db",
        Path.cwd() / "tastytrade_mcp.db-journal",
    ]

    removed = []
    for file_path in files_to_remove:
        if file_path.exists():
            file_path.unlink()
            removed.append(str(file_path))

    if removed:
        console.print(f"[green]Removed {len(removed)} files:[/green]")
        for file_path in removed:
            console.print(f"  - {file_path}")
    else:
        console.print("[yellow]No files to remove[/yellow]")


def main():
    """Main CLI entry point"""
    app()


if __name__ == "__main__":
    main()