import ast
import datetime
import os
import re
import shutil
import sys

# --- Core Configuration ---
LIBRARY_VERSION = "0.1.0"
AGENT_VERSION = "4.0"
AGENT_FEED_FILE = "AGENT_FEED.txt"
LOG_FILE = "AGENT_LOG.txt"

def add_to_log(message):
    """Appends a timestamped message to the log file and prints a summary to the console."""
    # Log the full, detailed message to the file
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(force_safepath(LOG_FILE), 'a') as f:
        f.write(f"[{timestamp}] {message}\n")

    # Print a user-friendly part of the message to the console
    parts = message.split(':', 1)
    if len(parts) > 1:
        # If there's a colon, print the part after it
        print(parts[1].strip())
    else:
        # Otherwise, just print the whole message
        print(message)

def invoke_exception(exception_message):
    """Logs an error message and then raises an exception to halt execution."""
    # The "CRITICAL ERROR" prefix is for the log file; the part after the colon is for the console.
    add_to_log(f"CRITICAL ERROR: {exception_message}")
    raise Exception(exception_message)

def is_path_safe(requested_path):
    """Checks if a requested path is a subdirectory of the current working directory."""
    try:
        current_dir = os.path.realpath(os.getcwd())
        requested_path_resolved = os.path.realpath(os.path.join(current_dir, requested_path))
        return requested_path_resolved.startswith(current_dir)
    except Exception:
        return False

def force_safepath(requested_path):
    """Ensures a path is safe; raises an exception if it is not."""
    if not is_path_safe(requested_path):
        invoke_exception(f"Path is outside the allowed sandbox: {requested_path}")
    return requested_path

def ensure_safe_directory(dir_path):
    """Safely creates a directory if it doesn't exist, raising an exception on failure."""
    force_safepath(dir_path)
    try:
        os.makedirs(dir_path, exist_ok=True)
    except Exception as e:
        invoke_exception(f"Could not create directory {dir_path}: {e}")

def request_human_approval(message):
    """Stalls the program to request human approval for a critical action."""
    add_to_log(f"request_human_approval: Awaiting human approval for: {message}")
    # These prints are for direct user interaction, not logging, so they remain.
    print("\n--- AWAITING HUMAN REVIEW ---")
    print(message)
    user_input = input("Enter 'YES' to apply this change or any other key to abandon and terminate the entire operation: ").strip().upper()
    
    if user_input != 'YES':
        add_to_log("request_human_approval: Operation terminated by human reviewer.")
        print("--- OPERATION TERMINATED BY HUMAN REVIEWER ---")
        sys.exit(1)
    
    add_to_log("request_human_approval: Change approved by human reviewer.")
    print("--- Change approved by human reviewer. Continuing... ---")

def handle_create_and_write_file(filepath, content):
    force_safepath(filepath)
    parent_dir = os.path.dirname(filepath)
    if parent_dir:
        ensure_safe_directory(parent_dir)
    try:
        with open(filepath, 'w') as f:
            f.write(content)
        return f"handle_create_and_write_file: Successfully created and wrote to file: {filepath}"
    except Exception as e:
        invoke_exception(f"Could not create file {filepath}: {e}")

def handle_update_file(filepath, new_content):
    force_safepath(filepath)
    if not os.path.exists(filepath):
        invoke_exception(f"File to update does not exist: {filepath}")

    refinery_folder = "REFINERY"
    ensure_safe_directory(refinery_folder)

    try:
        base_name, file_extension = os.path.splitext(os.path.basename(filepath))
        original_file_refinery_path = force_safepath(os.path.join(refinery_folder, f"{base_name}_ORIGINAL{file_extension}"))
        updated_file_refinery_path = force_safepath(os.path.join(refinery_folder, f"{base_name}_UPDATED{file_extension}"))

        shutil.copyfile(filepath, original_file_refinery_path)
        with open(updated_file_refinery_path, 'w') as f:
            f.write(new_content)
        
        approval_message = (f"An update is proposed for the file: {filepath}\n"
                            f"Please review the files in the '{refinery_folder}' directory.")
        request_human_approval(approval_message)
        
        shutil.copyfile(updated_file_refinery_path, filepath)
        return f"handle_update_file: Update for {filepath} approved and applied successfully."
    except Exception as e:
        invoke_exception(f"Error during update process for {filepath}: {e}")

def handle_read_file(filepath):
    force_safepath(filepath)
    if not os.path.exists(filepath):
        invoke_exception(f"File to read does not exist: {filepath}")
    try:
        with open(filepath, 'r') as f:
            file_content = f.read()
        
        # This print is a primary action (displaying content), not a log status.
        print(f"\n--- Reading File: {filepath} ---\n{file_content}\n--- End of File: {filepath} ---")
        return f"handle_read_file: Successfully read content of {filepath}"
    except Exception as e:
        invoke_exception(f"Could not read file {filepath}: {e}")

def handle_list_files(directory):
    force_safepath(directory)
    if not os.path.isdir(directory):
        invoke_exception(f"Directory to list does not exist: {directory}")
    
    refinery_folder = "REFINERY"
    ensure_safe_directory(refinery_folder)

    try:
        list_output = f"Listing for directory: {directory}\n" + "-" * 20 + "\n"
        for item in os.listdir(directory):
            list_output += f"[{'DIR' if os.path.isdir(os.path.join(directory, item)) else 'FILE'}] {item}\n"
        
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        list_filepath = force_safepath(os.path.join(refinery_folder, f"file_list_{timestamp}.txt"))

        with open(list_filepath, 'w') as f:
            f.write(list_output)
        
        return f"handle_list_files: Successfully generated file list for '{directory}' at: {list_filepath}"
    except Exception as e:
        invoke_exception(f"Could not list directory {directory}: {e}")

def handle_generate_docs(filepath):
    force_safepath(filepath)
    if not os.path.exists(filepath):
        invoke_exception(f"File for doc generation does not exist: {filepath}")

    docs_dir = "docs"
    ensure_safe_directory(docs_dir)
    try:
        with open(filepath, 'r') as f:
            source_code = f.read()
        tree = ast.parse(source_code)
        docs_content = f"# Documentation for {os.path.basename(filepath)}\n\n"
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                docstring = ast.get_docstring(node)
                if docstring:
                    docs_content += f"## {node.name}\n\n```python\n{node.name}(...)\n```\n\n{docstring.strip()}\n\n"
        
        filename_without_ext = os.path.splitext(os.path.basename(filepath))[0]
        docs_filepath = force_safepath(os.path.join(docs_dir, f"{filename_without_ext}_docs.md"))
        
        with open(docs_filepath, 'w') as f:
            f.write(docs_content)
        return f"handle_generate_docs: Successfully generated documentation for {filepath} at {docs_filepath}."
    except Exception as e:
        invoke_exception(f"Could not generate documentation for {filepath}: {e}")

def handle_generate_structured_state_snapshot(requested_dir):
    force_safepath(requested_dir)
    if not os.path.isdir(requested_dir):
        invoke_exception(f"Directory for generating State Snapshot does not exist: {requested_dir}")

    refinery_folder = "REFINERY"
    ensure_safe_directory(refinery_folder)
    try:
        output_content = ""
        for root, _, files in os.walk(requested_dir):
            for f in files:
                filepath = os.path.join(root, f)
                with open(filepath, 'r', errors='ignore') as file_to_read:
                    file_content = file_to_read.read()
                output_content += f"AGENT_CREATE_AND_WRITE_FILE_START {filepath}\nAGENT_CREATE_AND_WRITE_FILE_CONTENT\n{file_content}\nAGENT_CREATE_AND_WRITE_FILE_FINISH\n\n"
        
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filepath = force_safepath(os.path.join(refinery_folder, f"generated_structured_state_snapshot{timestamp}.txt"))
        
        with open(output_filepath, 'w') as f:
            f.write(output_content)
        return f"handle_generate_structured_state_snapshot: Successfully generated structured state snapshot for '{requested_dir}' at {output_filepath}"
    except Exception as e:
        invoke_exception(f"Could not generate LLM response for {requested_dir}: {e}")

def handle_download_resource(filepath, url):
    DISABLED_FOR_SAFETY_MESSAGE = "handle_download_resource:This functionality has been completely disabled for safety for all versions of skeptofox < 3.0.0"
    invoke_exception(DISABLED_FOR_SAFETY_MESSAGE)

def handle_save_webpage(folderpath, url):
    DISABLED_FOR_SAFETY_MESSAGE = "handle_save_webpage:This feature has been completely disabled for safety for all versions of skeptofox < 3.0.0"
    invoke_exception(DISABLED_FOR_SAFETY_MESSAGE)

def parse_commands_from_content(content):
    commands = []
    cmd_patterns = {
        'CREATE_AND_WRITE_FILE': r'AGENT_CREATE_AND_WRITE_FILE_START\s+(.*?)\s+AGENT_CREATE_AND_WRITE_FILE_CONTENT\s+(.*?)\s+AGENT_CREATE_AND_WRITE_FILE_FINISH',
        'UPDATE_FILE': r'AGENT_UPDATE_FILE_START\s+(.*?)\s+AGENT_UPDATE_FILE_NEW_CONTENT\s+(.*?)\s+AGENT_UPDATE_FILE_FINISH',
        'DOWNLOAD_RESOURCE': r'AGENT_DOWNLOAD_RESOURCE_START\s+(.*?)\s+AGENT_DOWNLOAD_RESOURCE_URL\s+(.*?)\s+AGENT_DOWNLOAD_RESOURCE_FINISH',
        'SAVE_WEBPAGE': r'AGENT_SAVE_WEBPAGE_START\s+(.*?)\s+AGENT_SAVE_WEBPAGE_URL\s+(.*?)\s+AGENT_SAVE_WEBPAGE_FINISH',
    }
    arg_names = {'CREATE_AND_WRITE_FILE': ['filepath', 'content'], 'UPDATE_FILE': ['filepath', 'new_content'], 'DOWNLOAD_RESOURCE': ['filepath', 'url'], 'SAVE_WEBPAGE': ['folderpath', 'url']}
    for cmd_type, pattern in cmd_patterns.items():
        for match in re.findall(pattern, content, re.DOTALL):
            commands.append({'type': cmd_type, 'args': {arg_names[cmd_type][i]: val.strip() for i, val in enumerate(match)}})
    
    single_arg_patterns = {
        'READ_FILE': r'AGENT_READ_FILE\s+(.*?)$', 'LIST_FILES': r'AGENT_LIST_FILES\s+(.*?)$',
        'GENERATE_DOCS': r'AGENT_GENERATE_DOCS\s+(.*?)$', 'GENERATE_STRUCTURED_STATE_SNAPSHOT': r'AGENT_GENERATE_STRUCTURED_STATE_SNAPSHOT\s+(.*?)$',
    }
    single_arg_names = {'READ_FILE': 'filepath', 'LIST_FILES': 'directory', 'GENERATE_DOCS': 'filepath', 'GENERATE_STRUCTURED_STATE_SNAPSHOT': 'requested_dir'}
    for cmd_type, pattern in single_arg_patterns.items():
        for match in re.findall(pattern, content, re.MULTILINE):
            commands.append({'type': cmd_type, 'args': {single_arg_names[cmd_type]: match.strip()}})
    return commands

COMMAND_DISPATCHER = {
    'CREATE_AND_WRITE_FILE': handle_create_and_write_file, 'UPDATE_FILE': handle_update_file,
    'READ_FILE': handle_read_file, 'LIST_FILES': handle_list_files,
    'GENERATE_DOCS': handle_generate_docs, 'GENERATE_STRUCTURED_STATE_SNAPSHOT': handle_generate_structured_state_snapshot,
    'DOWNLOAD_RESOURCE': handle_download_resource, 'SAVE_WEBPAGE': handle_save_webpage,
}

def execute_commands(commands):
    if not commands:
        add_to_log("execute_commands: No valid commands found to execute.")
        return
        
    for i, command in enumerate(commands):
        command_type, command_args = command.get('type'), command.get('args', {})
        handler = COMMAND_DISPATCHER.get(command_type)
        
        add_to_log(f"execute_commands: Executing Task {i+1}/{len(commands)}: {command_type}")
        
        if handler:
            result = handler(**command_args)
            add_to_log(f"execute_commands: Task {i+1} SUCCEEDED. {result}")
        else:
            invoke_exception(f"Unknown command type '{command_type}'. Halting.")

def run():
    """Initializes and runs the Skeptofox agent."""
    if os.path.exists(force_safepath(LOG_FILE)):
        os.remove(LOG_FILE)

    add_to_log("run: Agent 4.0 Initializing with Fail-Fast protocol and consolidated logging.")
    print(f"Sandboxed to: {os.getcwd()}")

    if not os.path.exists(force_safepath(AGENT_FEED_FILE)):
        print(f"\nCRITICAL ERROR: The required response file '{AGENT_FEED_FILE}' was not found.")
        sys.exit(1)

    try:
        add_to_log(f"run: Reading commands from '{AGENT_FEED_FILE}'.")
        with open(force_safepath(AGENT_FEED_FILE), 'r') as f:
            llm_content = f.read()

        parsed_commands = parse_commands_from_content(llm_content)
        execute_commands(parsed_commands)

        add_to_log("run: All tasks completed successfully.")

    except Exception as e:
        print("\n--- AGENT HALTED DUE TO A CRITICAL ERROR ---")
        print(f"Error Details: {e}")
        print(f"Please review '{LOG_FILE}' for a detailed execution trace.")
        sys.exit(1)
