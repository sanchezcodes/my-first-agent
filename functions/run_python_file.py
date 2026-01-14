import os
from google.genai import types
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        working_directory_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_directory_abs, file_path))
        is_valid_directory = os.path.commonpath([working_directory_abs, target_dir]) == working_directory_abs
        
        if not is_valid_directory:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_dir):
            return f'Error: "{file_path}" does not exist or is not a regular file' 
        
        if not target_dir.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_dir]
        if args != None:
            command.extend(args)

        run_process = subprocess.run(command, capture_output=True, timeout=30, text=True)
        return_code = run_process.returncode
        
        output_string_process = ""
        if return_code != 0:
            output_string_process += f"Process exited with code {return_code} \n "
        if run_process.stdout == None and run_process.stderr == None:
            output_string_process += "No output produced \n "
        if run_process.stdout != None:
            output_string_process += f'STDOUT: {run_process.stdout} \n '
        if run_process.stderr != None:
            output_string_process += f'STDERR: {run_process.stderr} \n '

        return output_string_process

    except Exception as e:
        return f'Error: {e}'

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a specified Python file within the working directory and returns its output",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to run, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                ),
                description="Optional list of arguments to pass to the Python script",
            ),
        },
        required=["file_path"],
    ),
)
