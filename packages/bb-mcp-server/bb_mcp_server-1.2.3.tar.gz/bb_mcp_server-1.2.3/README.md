# Bitbucket MCP Server

[![PyPI version](https://badge.fury.io/py/bb-mcp-server.svg)](https://badge.fury.io/py/bb-mcp-server)
[![Python](https://img.shields.io/pypi/pyversions/bb-mcp-server.svg)](https://pypi.org/project/bb-mcp-server/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Model Context Protocol (MCP) server that provides programmatic access to Bitbucket API v2.0. Built with FastMCP, this server enables LLMs and other tools to interact with Bitbucket repositories, pull requests, pipelines, and workspaces.

## Features

- **11 MCP Tools**: Lean surface covering pull requests, pipelines, and workspace insights
- **7 MCP Resources**: Quick access to repository info, branches, members, and more
- **Optimized for LLMs**: Token-efficient design with structured outputs
- **Flexible Configuration**: Works with any Bitbucket workspace and repository via environment variables or HTTP headers
- **Context-Aware Credentials**: Per-request headers are cached in the FastMCP context so every tool call shares the same configuration

## Installation

### From PyPI

```bash
pip install bb-mcp-server
```

### From Source

```bash
git clone https://github.com/jasonpaulso/bitbucket-openapi-generated.git
cd bitbucket-openapi-generated
pip install -e .
```

## Configuration

1. Create a Bitbucket App Password:

   - Go to https://bitbucket.org/account/settings/app-passwords/
   - Create a new app password with necessary permissions
   - Save the password securely

2. Supply credentials on every request via HTTP headers (see below). You can also set
   environment variables as server defaults for single-tenant deployments.

3. Environment variable template (optional server defaults):

   ```env
   BITBUCKET_USERNAME=your_username
   BITBUCKET_APP_PASSWORD=your_app_password
   BITBUCKET_WORKSPACE=your_workspace  # Optional; auto-discovered when absent
   BITBUCKET_REPO=your_repo
   REQUIRE_CLIENT_CREDENTIALS=false  # Set true to require HTTP headers for sensitive values
   ```

4. HTTP header equivalents (case-insensitive):

   | Header | Purpose |
   | ------ | ------- |
   | `X-Bitbucket-Username` | Bitbucket username |
   | `X-Bitbucket-App-Password` | Bitbucket app password |
   | `X-Bitbucket-Workspace` | Workspace slug (optional; auto-detected when only one exists) |
   | `X-Bitbucket-Repo` | Repository slug |
   | `Authorization: Bearer <token>` | Optional bearer token (overrides basic auth) |
   | `Authorization: Basic <...>` | Optional pre-encoded basic credential |

   > When `REQUIRE_CLIENT_CREDENTIALS=true`, the server refuses to fall back to environment
   > variables for sensitive keys during HTTP requests.

   You can also suffix requests with `?repo=<workspace>/<repo>` (or simply `?repo=<repo>` in
   a single-workspace account) instead of sending the `X-Bitbucket-Repo` header. Add
   `?workspace=<workspace>` to override the workspace explicitly. Query parameters take
   precedence over headers and inferred defaults, making it easy to pin a repo/workspace
   for a single request.

   Examples:
   - `...?repo=busie/fe-main`
   - `...?repo=fe-main&workspace=busie` (equivalent)

   Single-workspace accounts can skip the workspace header altogether; the server will
   auto-discover the slug on first use.

5. Project-level configuration lives in `fastmcp.json`, which you can customise and run via
   `fastmcp run fastmcp.json` in any environment that supports the FastMCP CLI.

## Usage

### Running the Server

```bash
# Using the installed package (HTTP transport only)
bb-mcp-server --host 0.0.0.0 --port 8000

# Or run directly from source
python server.py --host 0.0.0.0 --port 8000

# Via the FastMCP CLI with declarative config
fastmcp run fastmcp.json

# Skip environment bootstrapping when dependencies are preinstalled (e.g., Docker)
fastmcp run fastmcp.json --skip-env
```

Both `bb-mcp-server` and `python server.py` accept `--host`, `--port`, and `--transport`
flags (HTTP only). The `fastmcp.json` file in this repository mirrors those defaults so
`fastmcp run` starts an HTTP server without additional arguments.

### Integrating with MCP Clients

Forward the headers listed in the configuration section with every request. See
[AGENTS.md](AGENTS.md) for agent integration details and context behaviour.

Tools automatically reuse the scoped workspace/repo from the FastMCP context, so the HTTP schemas hide those arguments—use request-level overrides (headers or `?workspace=`/`?repo=`) when you need to switch context.

## Available Tools

The lean surface ships ten focused tools with summary-first payloads:

- `pr.list` – List PRs with compact metadata.
- `pr.overview` – Return digest: meta, blockers, diffstat, recent comments.
- `pr.review` – Generate a structured review summary based on the overview.
- `pr.comment.add` – Post a PR comment (optional inline path/line).
- `pr.tasks.sync` – Create and resolve PR tasks in one call.
- `pipe.run` – Start a pipeline for the given repo/ref/spec.
- `pipe.fail.summary` – Summarise the most recent failing pipelines.
- `workspace.list` – List repos, members, or projects (summary by default).
- `repo.get` – Repo basics plus a five-item PR sample.
- `me.whoami` – Minimal identity plus accessible workspaces.

### Resources

- `repo://{repo}/info` – Repository information
- `pipelines://{repo}/recent` – Recent pipeline runs
- `pull-requests://{repo}/open` – Open pull requests
- `workspace://{workspace}/members` – Team members for reviewers
- `workspace://{workspace}/default-reviewers` – Suggested reviewers
- `repo://{repo}/branches` – Available branches
- `repo://{repo}/branching-model` – Branching configuration

## Development

### Setting up Development Environment

```bash
# Clone the repository
git clone https://github.com/jasonpaulso/bitbucket-openapi-generated.git
cd bitbucket-openapi-generated

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install in development mode
pip install -e .
pip install -r requirements.txt
```

### Running Tests

```bash
# Install test dependencies
pip install pytest pytest-asyncio pytest-cov

# Run tests
pytest tests/

# Run with coverage
pytest tests/ --cov=. --cov-report=html
```

### Code Quality

```bash
# Linting
ruff check .

# Formatting
black .

# Type checking
mypy server.py utils/ modules/
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [FastMCP](https://github.com/jlowin/fastmcp) framework
- Uses Bitbucket API v2.0
- Implements Model Context Protocol (MCP) specification

## Support

For issues, questions, or contributions, please visit:

- GitHub Issues: https://github.com/jasonpaulso/bitbucket-openapi-generated/issues
- Documentation: https://github.com/jasonpaulso/bitbucket-openapi-generated/wiki


## Next Steps?

- Built-in Auth Providers: if you plan to expand beyond simple bearer/basic
  auth, FastMCP’s auth providers (see docs/fast-mcp/auth-overview.md) can
  replace the custom middleware with reusable token/OAuth flows and built-in
  metadata hints for clients.
