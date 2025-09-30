"""Pull agent operation for Canvas CLI."""

import yaml
from pathlib import Path
from typing import Dict, Any, Optional, List, Tuple

import click
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

from ..utils.config import ConfigManager
from ..utils.exceptions import APIError, FileSystemError
from ..services.api_client import APIClient
from ..utils.helpers import _resolve_project_id, require_canvas_workspace, require_authentication
from ..utils.helpers import convert_tool_obj_to_tool_data, convert_datasource_obj_to_datasource_data, convert_agent_obj_to_agent_data

console = Console()


def _get_project_environment(project: str) -> str:
    """Get environment from project configuration."""
    environment = "dev"  # default fallback
    try:
        # Get environment from project config
        project_dir = Path("projects") / project
        project_file = project_dir / "project.yaml"
        if project_file.exists():
            with open(project_file, 'r') as f:
                project_data = yaml.safe_load(f) or {}
            environment = project_data.get("config", {}).get("environment", "dev")
    except Exception as e:
        console.print(f"[yellow]Warning:[/yellow] Could not determine environment from project config: {e}")
        environment = "dev"
    
    return environment


def load_env_variables_from_yaml(environment: str) -> Dict[str, Any]:
    """Load environment variables from YAML file for variable replacement."""
    env_file_path = Path("env") / f"{environment}.yaml"
    if not env_file_path.exists():
        return {}
    
    try:
        with open(env_file_path, 'r') as f:
            env_data = yaml.safe_load(f) or {}
            # Filter out comment keys and None values
            return {k: v for k, v in env_data.items() if not k.startswith("#") and v is not None}
    except Exception as e:
        console.print(f"[yellow]Warning:[/yellow] Failed to load environment variables from {env_file_path}: {e}")
        return {}


def _merge_env_variables_to_yaml(environment: str, new_env_vars: Dict[str, Any]) -> None:
    """Merge new environment variables into environment-specific YAML file without overriding existing values."""
    env_file_path = Path("env") / f"{environment}.yaml"
    env_file_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Load existing environment variables
    existing_env_vars = {}
    if env_file_path.exists():
        try:
            with open(env_file_path, 'r') as f:
                existing_env_vars = yaml.safe_load(f) or {}
        except Exception as e:
            console.print(f"[yellow]Warning:[/yellow] Failed to load existing environment variables from {env_file_path}: {e}")
            existing_env_vars = {}
    
    # Merge new variables, but don't override existing ones
    merged_vars = existing_env_vars.copy()
    added_vars = []
    
    for key, value in new_env_vars.items():
        if key not in merged_vars:
            merged_vars[key] = value
            added_vars.append(key)
    
    # Write back to YAML file
    try:
        with open(env_file_path, 'w') as f:
            yaml.safe_dump(merged_vars, f, default_flow_style=False, allow_unicode=True)
        
        if added_vars:
            console.print(f"[green]✓[/green] Added {len(added_vars)} new environment variables to {env_file_path}")
            for var in added_vars[:5]:  # Show first 5 variables
                console.print(f"  • {var}")
            if len(added_vars) > 5:
                console.print(f"  • ... and {len(added_vars) - 5} more")
        else:
            console.print(f"[blue]No new environment variables to add to {env_file_path}[/blue]")
    except Exception as e:
        console.print(f"[yellow]Warning:[/yellow] Failed to write environment variables to {env_file_path}: {e}")


def pull_agent_operation(agent_short_name: str, project: Optional[str], profile: Optional[str]) -> None:
    """Pull a specific agent by short name to global agents/ directory."""
    try:
        # Validate we're in a Canvas workspace
        require_canvas_workspace()
        
        # Validate authentication
        require_authentication(profile)
        
        # Get profile and API client
        config_manager = ConfigManager()
        user_profile = config_manager.get_profile(profile)

        api_client = APIClient(user_profile)
        
        # Determine source project to pull FROM
        if not project:
            project = config_manager.get_default_project()
            
        project_id = _resolve_project_id(project)
        
        # Determine environment from project config
        environment = _get_project_environment(project)
        existing_env_vars = load_env_variables_from_yaml(environment)
        if not project_id:
            console.print(f"[red]Project '{project}' not found. Run 'canvas init' first or specify a valid project.[/red]")
            raise click.Abort()

        # Always use global directories - agents are global resources
        agents_dir = Path("agents")
        tools_dir = Path("tools")
        datasources_dir = Path("datasources")
        
        console.print(f"[blue]Pulling agent '{agent_short_name}' from project '{project}' to global workspace...[/blue]")
            
        # Ensure directories exist
        agents_dir.mkdir(parents=True, exist_ok=True)
        tools_dir.mkdir(parents=True, exist_ok=True)
        datasources_dir.mkdir(parents=True, exist_ok=True)

        # Get the specific agent from the specified project
        try:    
            agent_obj = api_client.get_agent_by_short_name(project_id, agent_short_name)
            agent_id = agent_obj.get("id")
        except APIError:
            console.print(f"[red]Agent '{agent_short_name}' not found in project '{project}'.[/red]")
            return

        # Step 1: Collect all dependencies first
        console.print("[blue]Analyzing dependencies...[/blue]")
        
        from .pull_resources import collect_all_dependencies
        all_agent_ids, all_tool_ids, all_datasource_ids = collect_all_dependencies(
            [agent_id], project_id, api_client
        )
        
        console.print(f"[green]✓[/green] Found {len(all_agent_ids)} agents, {len(all_tool_ids)} tools, {len(all_datasource_ids)} datasources")
        
        # Step 2: Pull unique resources and extract env variables
        console.print("[blue]Pulling resources...[/blue]")
        
        from .pull_resources import pull_resources_optimized
        new_env_vars = pull_resources_optimized(
            all_agent_ids, all_tool_ids, all_datasource_ids,
            project_id, api_client, existing_env_vars,
            agents_dir, tools_dir, datasources_dir, environment
        )
        
        # Step 3: Save environment variables
        if new_env_vars:
            _merge_env_variables_to_yaml(environment, new_env_vars)
            console.print(f"[green]✓[/green] Added {len(new_env_vars)} environment variables to env/{environment}.yaml")
        else:
            console.print(f"[blue]No new environment variables to add to env/{environment}.yaml[/blue]")

        console.print(f"\n[green]✓[/green] Agent '{agent_short_name}' pulled successfully to global agents/ directory!")
        console.print(f"[blue]Agent can now be used in any project.[/blue]")

    except APIError as e:
        console.print(f"[red]API Error:[/red] {e}")
        raise click.Abort()
    except FileSystemError as e:
        console.print(f"[red]File Error:[/red] {e}")
        raise click.Abort()
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        raise click.Abort()
