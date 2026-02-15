import subprocess

def run_shell_command(command: str):
    """
    Executes a string command through the system shell.
    """
    try:
        # shell=True allows using shell features like pipes (|) or wildcards (*)
        # capture_output=True saves stdout and stderr to the result object
        # text=True ensures output is returned as a string rather than bytes
        result = subprocess.run(
            command, 
            shell=True, 
            capture_output=True, 
            text=True, 
            check=True
        )
        return result.stdout.strip()
    
    except subprocess.CalledProcessError as e:
        return f"Error occurred: {e.stderr.strip()}"

# Usage:
output = run_shell_command("echo 'Hello World' | tr '[:lower:]' '[:upper:]'")
print(output)  # Output: HELLO WORLD
