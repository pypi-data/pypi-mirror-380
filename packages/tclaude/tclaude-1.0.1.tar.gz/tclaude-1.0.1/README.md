# tclaude — Claude in the terminal &nbsp;&nbsp; ![](https://github.com/tom94/tclaude/workflows/CI/badge.svg)

A complete implementation of Claude in the terminal.

Unlike other tools that aim to support all kinds of LLMs, **tclaude** is designed specifically for Claude.
As such, Claude-specific features like caching, Claude-native web search or code execution are implemented correctly and fully.

### Highlights

- Interactive chat with resumable sessions, extended thinking, and tool use
    - Built-in grounded web search, code execution, and file analysis
    - [MCP server](https://mcpservers.org/) support (both remote and local)
- Implement any custom tool in just a few lines of Python
- Automatic caching (makes Claude up to 10x cheaper!)

## Installation

```bash
pip install tclaude
```

Then set the `ANTHROPIC_API_KEY` environment variable to your [Claude API key](https://console.anthropic.com/settings/keys) and you are good to go.

## Usage

Running `tclaude` opens a new chat session. You can also directly pass a prompt to start a session.

```bash
tclaude "How do I make great pasta?"
# or: echo "How do I make great pasta?" | tclaude
> Great pasta starts with quality ingredients and proper technique. ...
```

Or use an outward pipe to integrate `tclaude` into unix workflows

```bash
git diff --staged | tclaude "Write a commit message for this diff." | xargs -0 git commit -m
```

Upload files with `-f`

```bash
tclaude -f paper.pdf "Summarize this paper."
tclaude -f cat.png "Is this a dog?"
```

Claude will use web search and server-side code execution when the request demands it:

```bash
tclaude "Tell me the factorials from 1 through 20."
> [Uses Python to compute the answer.]

tclaude "What is the state of the art in physically based rendering?"
> [Uses web search and responds with citations.]
```

### Sessions

Once you're done chatting, the session will be automatically named and saved as `<session-name>.json` in the working directory.

You can resume the session with `tclaude -s <session-name>.json` or browse past sessions with fuzzy finding via `tclaude -s`.

Customize where sessions are saved by passing `--sessions-dir <dir>` or by setting `sessions_dir` in the [configuration file](#configuration).

### Extended thinking

Enable thinking with `--thinking` or by setting `thinking = true` in the [configuration file](#configuration).

```bash
tclaude --thinking "Write a quine in C++."
> [Claude thinks about how to write a quine before responding.]
```

### Commands

Several commands are available to do other things than chatting with Claude, such as `/download` to download files previously created by Claude. Use `/help` to see a list of available commands.

### Custom system prompt

If you'd like to customize the behavior of Claude (e.g. tell it to be brief, or give it background information), create `~/.configs/tclaude/roles/default.md`.
The content of this file will be prepended as system prompt to all conversations.

If you'd like to load different system prompts on a case-by-case basis, you can pass them as command line argument or set `role` in the [configuration file](#configuration).

```bash
tclaude --role pirate.md "How do I make great pasta?"
> Ahoy there, matey! Ye be seekin' the secrets of craftin' the finest pasta this side of the Mediterranean, eh? ...
```

### Custom tools

Simply implement your tool as a function in `src/tclaude/tools.py` and it will be callable by Claude.
Make sure to [document](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/implement-tool-use#best-practices-for-tool-definitions) the tools' function thoroughly such that Claude uses it optimally.

### Custom endpoints

**tclaude** can connect to any [Anthropic-compatible endpoint](https://docs.anthropic.com/en/docs/claude-code/third-party-integrations).
By default **tclaude** uses Anthropic's official API endpoint, but you can set up your own endpoint in the [configuration file](#configuration) and then use it with `tclaude --endpoint <name>`.

### MCP server support

**tclaude** supports two kinds of [MCP servers](https://mcpservers.org).
See the [the configuration section](#configuration) for details on how to set up the servers.

1. Remote servers (e.g. [remote-mcp-servers](https://mcpservers.org/remote-mcp-servers))
    - Claude will connect directly to the server and use the tools it provides. The connection is not made by your machine.
    - Remote servers are useful for tools that require a lot of resources or need to be run in a server environment.
    - If the server needs authentication, it can be done via OAuth2 or a custom token.

2. Local servers (running on your machine or in an internal network)
    - **tclaude** will connect to the MCP server via your machine and forward the tools to Claude.
    - Local servers are useful for tools that require access to local resources (e.g. files on your machine).
    - Two protocols are supported: STDIN (**tclaude** starts the server and pipes the input to it) and HTTPS (**tclaude** connects to the server via a URL).

### Configuration

You can configure **tclaude** by creating the `~/.configs/tclaude/tclaude.toml` file.
If you have `$XDG_CONFIG_HOME` set, the file should be placed at `$XDG_CONFIG_HOME/tclaude/tclaude.toml`.

The default configuration file looks as follows. (Or use `tclaude --print-default-config` to print it to stdout.)
You can copy it as a starting point for your own configuration or you can only set the settings you want to differ from the defaults.
Commenta indicate optional settings such as custom endpoints or MCP servers.

Nearly all settings can be overridden via command line arguments, e.g. `tclaude --thinking` or `tclaude --no-web-search`.
Run `tclaude --help` to see all available arguments.

```toml
# Default configuration for the tclaude CLI tool.
# All settings can be omitted in your own config, in which case the defaults from this file will be used.

model = "claude-sonnet-4-5-20250929"
max_tokens = 16384
role = "default.md"  # Custom system prompt file. Should be placed ~/.config/tclaude/roles/

code_execution = true
web_search = true
thinking = false
thinking_budget = "auto"  # In tokens. (default: max_tokens / 2)

sessions_dir = "."  # Directory for storing session data.

endpoint = "anthropic"

[endpoints.anthropic]
kind = "anthropic"
url = "https://api.anthropic.com"
api_key = "$ANTHROPIC_API_KEY"

# Example vertex endpoint

# [endpoints.custom]
# kind = "vertex"
# url = "https://aiplatform.googleapis.com/v1/projects/<VERTEX_API_PROJECT>/locations/global/publishers/anthropic/models/<MODEL>:streamRawPredict"
# api_key = "$(gcloud auth print-access-token)"
# code_execution = false # This endpoint does not support code execution
# web_search = false # This endpoint does not support web search

# Example configuration for remote Model Context Protocol (MCP) servers

# [[mcp.local_servers]]
# name = "filesystem"
# command = "npx" # command and arguments to start the MCP server
# args = [
#     "-y",
#     "@modelcontextprotocol/server-filesystem",
#     "~", # access to the home directory
# ]
# or: url = "http://localhost:3000" # if the server is already running

# [[mcp.remote_servers]]
# name = "example-mcp"
# url = "https://example-server.modelcontextprotocol.io/sse"

# authentication = "oauth2" # opens a browser window to authenticate on first use
# or: authentication = "none"
# or: authentication = "token", authorization_token = "<your-authorization-token>"

# Optional: restrict the tools that can be used with this MCP server
# authorization_token = "<your-authorization-token>"
# tool_configuration.enabled = true
# tool_configuration.allowed_tools = [
#   "example_tool_1",
#   "example_tool_2",
# ]
#
# [[mcp.remote_servers]]
# name = "another-mcp"
# ...
```

## License

GPLv3; see [LICENSE](LICENSE.txt) for details.
