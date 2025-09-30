# sast-fixer-mcp: SAST Fixer MCP Server

A Model Context Protocol (MCP) server that provides dedicated handling of Static Application Security Testing (SAST) reports. It includes capabilities for parsing DOCX reports, tracking vulnerability remediation statuses, and exporting comprehensive fix reports. Seamless integration with Zhanlu AI Programmer enables automated remediation for vulnerabilities identified in SAST processes.


## Features

- **DOCX Report Processing**: Convert SAST reports from DOCX format to structured JSON
- **Vulnerability Tracking**: Track remediation status of security vulnerabilities  
- **Report Generation**: Generate comprehensive CSV reports of fixed vulnerabilities
- **MCP Integration**: Full integration with Model Context Protocol servers
- **Automated Workflow**: Streamlined vulnerability fixing process with AI assistance

## Available Tools

- **convert_sast_docx_to_json** - Converts SAST reports from DOCX format to JSON
  - `file_path` (string, required): Path to the SAST report DOCX file

- **get_pending_vulnerability_json_files** - Retrieves all pending vulnerability JSON files (`_new.json`) from the `.scanissuefix` directory

- **generate_csv_report** - Generates a CSV report from all resolved vulnerability JSON files (`_finished.json`)


## Prerequisites

* **Python 3.10 or higher** is required. Verify your Python version:

```bash
python --version  # or python3 --version
```

* Check if you have the appropriate Python environment installed:

```bash
which python  # or which python3
```


### Install Python

If you do not have Python installed or your version is not match the prerequisites, it's recommended to install the most stable version of Python 3.12 using the following direct download links:

* **Mac**: [Download Python 3.12 for macOS](https://mirrors.aliyun.com/python-release/macos/python-3.12.10-macos11.pkg)

  * For silent installation on macOS:

  ```bash
  sudo installer -pkg /path/to/python-3.12.4-macos11.pkg -target /
  ```

* **Windows**: [Download Python 3.12 for Windows](https://mirrors.aliyun.com/python-release/windows/python-3.12.9-amd64.exe)

  * For silent installation on Windows, run:

  ```bash
  python-3.12.4-amd64.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
  ```

### Upgrade Python

If your current Python version does not meet the required standard, download and install the recommended Python 3.12 version using the above links. Ensure your system's PATH points to the new Python installation.



### Additional Setup Notes
If Python was newly installed while the Terminal (either inside an IDE or a standalone system terminal) was already open,  the session may not automatically detect updated environment variables (e.g., PATH).  Use the following commands to refresh PATH in the current session without restarting your IDE or terminal:

* **Windows:**
  ```powershell
  $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
  python -V
  ```

* **macOS:**
  ```bash
  source ~/.zshrc   # or ~/.bashrc depending on your shell
  python -V
  ```


## Installation

### Using uv (Recommended)

First, install `uv` if you haven't already:

```bash
pip install uv
```

When using [`uv`](https://docs.astral.sh/uv/) no specific installation is needed. We will use [`uvx`](https://docs.astral.sh/uv/guides/tools/) to directly run *sast-fixer-mcp*.

Run the SAST Fixer MCP server directly:

```bash
uvx sast-fixer-mcp
```


### Using pip

Alternatively you can install `sast-fixer-mcp` via pip:

```bash
pip install sast-fixer-mcp
```

After installation, you can check its usage with:

```bash
python -m sast_fixer_mcp --help
```


## Configuration

### Usage with VS Code Extension zhanlu AI Programmer

For manual installation, add the following JSON block to your User Settings (JSON) file in VS Code.

<details>
<summary>Using uvx</summary>

```json
{
  "mcpServers": {
    "sast-fixer-mcp": {
      "command": "uvx",
      "args": ["sast-fixer-mcp"]
    }
  }
}
```
</details>

<details>
<summary>Using pip installation</summary>

```json
{
  "mcpServers": {
    "sast-fixer-mcp": {
      "command": "python",
      "args": ["-m", "sast_fixer_mcp"]
    }
  }
}
```
</details>

**Configuration Notes:**
- For specific Python environments, use \`which python\` to get the full path. For venv or conda environments, specify the absolute path to the python executable. Incorrect python executable specifying in "command" might cause issues such as "No module named sast_fixer_mcp" or "MCP error -32000: Connection closed". 
For example:
    ```bash
    which python
    /opt/miniconda3/envs/myenv/bin/python
    ```
- If Python was installed during MCP setup and environment variables were updated,  
errors like **“Error executing MCP tool: Not connected”** or  
**“MCP error -32000: Connection closed”** may appear.  Restarting only the MCP server will not help， you must **restart the IDE** so it reloads the updated PATH and Python environment.  

- For large SAST reports, increase the `timeout` setting to avoid timeouts.

## Usage Workflow

1. **Obtain SAST Report**: Get the SAST report Word document for your target codebase
2. **Setup Repository**: Clone the codebase and switch to the appropriate branch  
3. **Start Analysis**: Use AI assistant with SAST Fixer MCP integration for security vulnerability analysis
4. **Process Report**: Convert DOCX report to JSON format using the `convert_sast_docx_to_json` tool
5. **Track Progress**: Monitor vulnerability remediation using pending and completed file tracking
6. **Generate Reports**: Create comprehensive CSV reports of fixed vulnerabilities

**Important Notes:**
- Ensure your working directory is positioned at the project root during the fixing process
- For continued analysis, use natural language commands like: "continue fixing", "generate csv report", "analyze vulnerabilities", etc.
- The tool creates a `.scanissuefix` directory to track vulnerability status

## Debugging

You can use the MCP inspector to debug the server. For uvx installations:

```bash
npx @modelcontextprotocol/inspector uvx sast-fixer-mcp
```

Or if you've installed the package in a specific directory or are developing on it:

```bash
cd path/to/servers/src/sast_fixer_mcp
npx @modelcontextprotocol/inspector uv run sast-fixer-mcp
```


## Development

If you are doing local development, there are two ways to test your changes:

1. **Run the MCP inspector** to test your changes. See [Debugging](#debugging) for run instructions.



### Local Development Setup

For local development:

```bash
cd src/sast_fixer_mcp
uv sync
uv run python -m sast_fixer_mcp --verbose --working-directory /path/to/test/project
```

Run tests:

```bash
uv run pytest
```

Run linting and type checking:

```bash
uv run ruff check
uv run pyright
```

## Build

```
cd .\mcp-servers\servers\sast_fixer_mcp\
uv build
twine upload .\dist\*


```

## License

MIT License - see LICENSE file for details.