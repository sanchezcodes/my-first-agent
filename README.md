# My First Agent

An AI-powered code agent built with Python and Google's Gemini 2.5 Flash. This agent can understand natural language instructions and autonomously perform file operations, read code, and execute Python scripts.

## Features

- **File Exploration** - List files and directories with metadata
- **File Reading** - Read and analyze file contents
- **Python Execution** - Run Python scripts and capture output
- **File Writing** - Create or modify files
- **Agentic Loop** - Automatically chains multiple operations to complete complex tasks

## Requirements

- Python >= 3.13
- Google Gemini API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/sanchezcodes/my-first-agent.git
cd my-first-agent
```

2. Install dependencies using `uv`:
```bash
uv sync
```

3. Create a `.env` file with your Gemini API key:
```
GEMINI_API_KEY='your-api-key-here'
```

## Usage

Run the agent with a natural language instruction:

```bash
python main.py "your instruction here"
```

### Examples

```bash
# List all files in the working directory
python main.py "List all files in the working directory"

# Run the calculator
python main.py "Run the calculator with expression 3 + 5"

# Create a new file
python main.py "Create a file called hello.txt with the content 'Hello World!'"

# Run tests and get results
python main.py "Run all tests in the calculator and tell me the results"
```

### Verbose Mode

Add `--verbose` to see detailed information about token usage and function calls:

```bash
python main.py "your instruction" --verbose
```

## Project Structure

```
my-first-agent/
├── main.py              # Agent entry point
├── call_function.py     # Function routing and execution
├── config.py            # Configuration constants
├── prompts.py           # System prompts for the LLM
├── functions/           # Tool implementations
│   ├── get_files_info.py
│   ├── get_file_content.py
│   ├── run_python_file.py
│   └── write_file.py
└── calculator/          # Sample application for testing
    ├── main.py
    ├── tests.py
    └── pkg/
        ├── calculator.py
        └── render.py
```

## Available Tools

| Tool | Description |
|------|-------------|
| `get_files_info` | Lists files and directories with size and type information |
| `get_file_content` | Reads the content of a file (up to 10,000 characters) |
| `run_python_file` | Executes a Python script with optional arguments |
| `write_file` | Creates or overwrites a file with specified content |

## Configuration

Edit `config.py` to customize:

```python
MAX_CHARS = 10000          # Max characters to read from files
WORKING_DIR = "./calculator"  # Restricted working directory
MAX_ITERS = 20             # Max agent loop iterations
```

## Security

The agent includes several safety measures:
- Path validation to prevent directory traversal
- Working directory sandboxing
- Process execution timeout (30 seconds)
- File size limits

## License

MIT
