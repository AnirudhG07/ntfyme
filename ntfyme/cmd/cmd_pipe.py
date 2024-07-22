import subprocess
import sys
import time


def pipe_exec(terminal_print) -> dict:
    """
    Executes the main command and returns the output, command, time taken and pid of the process.
    """

    if sys.stdin.isatty():
        print("Error: No input provided through pipe.")
        sys.exit(1)
    cmd = sys.stdin.read().strip()

    start_time = time.time()
    if terminal_print == "off":
        process = subprocess.Popen(
            cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        output, error = process.communicate()
    else:
        process = subprocess.Popen(cmd, stderr=subprocess.PIPE, shell=True, text=True)
        output, error = process.communicate()
        error = "none" if error == "" else error
        output = "Displayed on terminal or as you would expect."

    end_time = time.time()
    time_taken = end_time - start_time
    return {
        "output": output.strip(),
        "command": "".join(cmd),
        "time_taken": time_taken,
        "pid": process.pid,
        "error": error.strip() if error else "none",
    }
