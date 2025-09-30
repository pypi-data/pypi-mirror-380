# Raga Canvas CLI

A command-line interface for interacting with the Raga Canvas no-code agent deployment platform.

## Installation

```bash
pip install raga-canvas-cli
```

## Quick Start

1) Login
```bash
canvas login [--api-base https://api.canvas.raga.ai] [--profile <name>]
```
- Prompts for username and password, saves a profile locally.

2) Initialize a workspace
```bash
canvas init <directory> [--profile <name>] [--force] [--name <home-dir-name>]
```
- Fetches projects, asks for the default project short name, creates `canvas.yaml`, `project_config.yaml`, `environments/<project>.env`, and the workspace folders.

3) List your projects and agents
```bash
canvas list projects [--profile <name>]
canvas list agents [--project <short-name>] [--folder <id>] [--search <text>] [--active-only] [--profile <name>]
```

4) Pull resources locally (optional)
```bash
canvas pull projects [--profile <name>]
canvas pull agents [--agent <short-name-or-id>] [--profile <name>]
canvas pull tools [--tool <short-name-or-id>] [--profile <name>]
canvas pull datasources [--datasource <short-name-or-id>] [--profile <name>]
```

5) Push and deploy an agent
```bash
canvas push agents --agent <short-name> [--target-project <short-name>] [--profile <name>] [--force]
canvas deploy agents --agent <short-name> [--target-project <short-name>] [--profile <name>]
```

## Commands

### canvas login
Authenticate with the Canvas platform and save credentials.

Usage:
```bash
canvas login [--api-base <url>] [--profile <name>]
```
- Prompts for username and password, validates, and stores a token under the given profile (default: `default`).

### canvas init
Initialize Canvas workspaces for all projects in separate folders by shortName.

Usage:
```bash
canvas init <directory> [--profile <name>] [--force] [--name <home-dir-name>]
```
- `--profile`: profile to use for authentication
- `--force`: proceed even if files already exist
- `--name`: home directory name under the provided `<directory>`

Creates the base structure and writes:
- `canvas.yaml`
- `project_config.yaml`
- `environments/<project>.env`
- Folders: `agents/`, `tools/`, `datasources/`, `environments/`

### canvas set default-project
Set the default project short name in `canvas.yaml`.

Usage:
```bash
canvas set default-project <project_short_name>
```

### canvas list
List Canvas resources.

- Projects
```bash
canvas list projects [--profile <name>]
```

- Agents
```bash
canvas list agents [--project <short-name>] [--folder <id>] [--search <text>] [--active-only] [--profile <name>]
```

- Tools
```bash
canvas list tools --project <short-name> [--search <text>] [--profile <name>]
```

- Datasources
```bash
canvas list datasources --project <short-name> [--search <text>] [--profile <name>]
```

- Workflows
```bash
canvas list workflows --project <short-name> [--folder <id>] [--profile <name>]
```

### canvas pull
Pull resources from the Canvas platform into your workspace.

- Projects → writes `project_config.yaml` and per-project env files
```bash
canvas pull projects [--profile <name>]
```

- Agents (uses default project unless overridden in config)
```bash
canvas pull agents [--agent <short-name-or-id>] [--profile <name>]
```

- Tools
```bash
canvas pull tools [--tool <short-name-or-id>] [--profile <name>]
```

- Datasources
```bash
canvas pull datasources [--datasource <short-name-or-id>] [--profile <name>]
```

### canvas push
Create or update resources in the target project. Uses the default project unless `--target-project` is provided.

- Agents
```bash
canvas push agents --agent <short-name> [--target-project <short-name>] [--profile <name>] [--force]
```

- Tools
```bash
canvas push tools --tool <short-name> [--target-project <short-name>] [--profile <name>] [--force]
```

- Datasources
```bash
canvas push datasources --datasource <short-name> [--target-project <short-name>] [--profile <name>] [--force]
```

### canvas deploy
Trigger deployment for an existing remote agent version in the target project.

- Agents
```bash
canvas deploy agents --agent <short-name> [--target-project <short-name>] [--profile <name>]
```

## Directory Structure

When you run `canvas init` or pull from a project, the following structure is created:

```
my-canvas-repo/
├── canvas.yaml                 # workspace config
├── .canvasrc                   # local profiles (ignored by VCS)
├── agents/
│   └── test-agent/
│       ├── agent.yaml
│       └── config.yaml
├── tools/
│   └── test-tool/
│       ├── tool.yaml
│       └── config.yaml
├── datasources/
│   └── test-datasource/
│       ├── datasource.yaml
│       └── config.yaml
├── environments/
│   ├── dev.env
│   ├── stage.env
│   ├── prod.env
│   └── <project>.env
└── project_config.yaml
```

## Configuration

The CLI uses the following configuration files:

- `~/.canvasrc` - Global user configuration and profiles
- `canvas.yaml` - Workspace configuration
- `project_config.yaml` - Project IDs and metadata pulled from the platform
- `environments/*.env` - Environment-specific secrets/placeholders

## Development

To set up for development:

```bash
git clone https://github.com/raga-ai/raga-canvas-cli
cd raga-canvas-cli
pip install -e ".[dev]"
```

Run tests:

```bash
pytest
```

## License

MIT License - see LICENSE file for details.
