# skeptofox
![PyPI - Version](https://img.shields.io/pypi/v/skeptofox)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/skeptofox)
![License](https://img.shields.io/pypi/l/skeptofox)

skeptofox provides a powerful, declarative paradigm for designing, building, and analyzing complex systems where human insight and machine intelligence collaborate. Define your *what*, and Skeptofox orchestrates the *how*.

This version introduces the **Skeptofox Agent**: a fail-fast agent for secure, transparent, and deterministic execution of LLM-generated commands in a sandboxed environment.

-----

## Installation

```bash
pip install skeptofox
```

-----

## Quick Start

1.  **Create an instruction file** named `AGENT_FEED.txt` in your project directory.

    **File: `AGENT_FEED.txt`**

    ```
    AGENT_CREATE_AND_WRITE_FILE_START src/main.py
    AGENT_CREATE_AND_WRITE_FILE_CONTENT
    # My first Python script
    print("Hello, Skeptofox!")
    AGENT_CREATE_AND_WRITE_FILE_FINISH

    AGENT_LIST_FILES src
    ```

2.  **Create a runner script** to import and run the agent.

    **File: `run_agent.py`**

    ```python
    from skeptofox import agent

    # This will read AGENT_FEED.txt and execute the commands.
    agent.run()
    ```

3.  **Run the agent** from your terminal.

    ```bash
    python run_agent.py
    ```

-----

## Agent Architecture & Features

The agent's internal architecture is designed for maintainability, scalability, and clarity, adhering to the **Don't Repeat Yourself (DRY)** principle.

### Core Design & Architecture

  * **Centralized Command Parser**: The agent uses a single function, `parse_commands_from_content`, to read the `AGENT_FEED.txt` file once. It extracts all commands into a structured list, creating a single source of truth for the execution plan.
  * **Dynamic Command Dispatcher**: A `COMMAND_DISPATCHER` dictionary maps command types (e.g., `'CREATE_AND_WRITE_FILE'`) directly to their corresponding handler functions. This makes the system highly extensible.
  * **Modular, Single-Responsibility Handlers**: Each `handle_...` function performs only its core task, receiving its arguments directly. This improves code readability and testability.
  * **Consolidated Logging**: A single utility, `add_to_log`, handles both writing detailed, timestamped messages to `AGENT_LOG.txt` and printing user-friendly summaries to the console, streamlining all feedback.

### Security & Fail-Fast Workflow

The agent prioritizes a "no-compromise" approach to security and workflow integrity. It is designed to halt completely at the first sign of an error rather than continue in an uncertain state.

  * **Strict Sandboxing**: All file system operations are constrained to the agent's working directory. The `force_safepath` utility acts as a security gate for every file operation, raising a script-terminating exception if any path attempts to escape the sandbox.
  * **Fail-Fast Error Handling**: The agent operates on a strict fail-fast basis. The failure of **any** single command will immediately trigger an exception via the `invoke_exception` utility. **This halts the entire script**, preventing any subsequent commands from running and ensuring the system never proceeds in a partially failed or unpredictable state.
  * **Synchronous Human Approval Gate**: For critical operations like updating a file, the `request_human_approval` function halts execution and requires an explicit `'YES'` from the user. A rejection terminates the entire script via `sys.exit(1)`, fitting perfectly with the fail-fast philosophy.

### Implemented Commands & Capabilities

The agent has a comprehensive set of commands for file system management, documentation, and web interaction.

  * **Create & Write File**: Safely creates a new file and writes content to it.
  * **Update File (with Approval)**: Initiates the human-in-the-loop workflow to modify an existing file, staging versions in the `REFINERY` folder.
  * **Read File**: Reads the content of a file and displays it directly in the console.
  * **List Files**: Saves a formatted list of a directory's contents to a timestamped file in the `REFINERY` folder.
  * **Generate Docs**: Parses a Python file to extract class and function docstrings, generating a clean markdown documentation file.
  * **Generate Structured State Snapshot**: Scans a directory to produce a structured (text-analyzable) and reproducible snapshot as a series of `CREATE_AND_WRITE_FILE` commands.

### Internal Tooling & Utilities

  * **Diagnostic Logging**: All operations, status updates, and critical errors are logged with timestamps to `AGENT_LOG.txt`. This file serves as the definitive trace for diagnosing the agent's execution flow and pinpointing the exact cause of any failure.
  * **Refinery Folder**: A dedicated `REFINERY` directory is used as a staging and output area for generated artifacts like directory listings and file update comparisons.
  * **Fail-Fast Utilities**: The core workflow is enforced by specialized functions like `invoke_exception` (which centralizes the "log and crash" behavior) and `force_safepath`, ensuring consistent application of the agent's security principles.

-----

## Agent Command Reference

This provides a complete list of all commands available for the agent. These commands are designed to be placed in the `AGENT_FEED.txt` file for execution.

### File Management Commands

These commands are for interacting with files and directories within the agent's secure sandbox.

  * **Create & Write File**

      * **Syntax:**
        ```
        AGENT_CREATE_AND_WRITE_FILE_START <filepath>
        AGENT_CREATE_AND_WRITE_FILE_CONTENT
        <content>
        AGENT_CREATE_AND_WRITE_FILE_FINISH
        ```
      * **Description:** Creates a new file at the specified `<filepath>`. If the parent directories do not exist, it will create them. The multi-line `<content>` is then written to this new file.

  * **Update File (Requires Human Approval)**

      * **Syntax:**
        ```
        AGENT_UPDATE_FILE_START <filepath>
        AGENT_UPDATE_FILE_NEW_CONTENT
        <new_content>
        AGENT_UPDATE_FILE_FINISH
        ```
      * **Description:** Initiates a secure, human-in-the-loop process to update an existing file. It stages the original and updated versions in the `REFINERY` folder and prompts for explicit user approval before overwriting the original file. The script will terminate if approval is not granted.

  * **List Files**

      * **Syntax:** `AGENT_LIST_FILES <directory>`
      * **Description:** Lists all files and subdirectories within the specified `<directory>`. The output, tagged with `[DIR]` or `[FILE]`, is saved to a new, timestamped `.txt` file inside the `REFINERY` folder.

  * **Read File**

      * **Syntax:** `AGENT_READ_FILE <filepath>`
      * **Description:** Reads the full content of the file at `<filepath>` and prints it directly to the console for immediate review.

### Project & Documentation Commands

These commands are for higher-level project management and introspection.

  * **Generate Docs**

      * **Syntax:** `AGENT_GENERATE_DOCS <filepath>`
      * **Description:** Reads a Python file at `<filepath>` and generates a clean Markdown documentation file based on its class and function docstrings. The output is saved in the `docs` folder.


* **Generate Structured State Snapshot (Signature Ability)**
    * **Syntax:** `AGENT_GENERATE_STRUCTURED_STATE_SNAPSHOT <folderpath>`
    * **Description:** Captures a complete, structured snapshot of a directory's state. It generates a single text file that embeds the full contents of every file within a series of `AGENT_CREATE_AND_WRITE_FILE` commands. This output serves a dual purpose: it allows an LLM to perform complete project analysis in additon to being usable by the agent as feed to perfectly replicate the project's state.

-----

## License

This project is licensed under the MIT License.