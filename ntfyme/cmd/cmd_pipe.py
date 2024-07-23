import subprocess
import sys
import time

from .live_capture import capture


def pipe_exec(terminal_print) -> dict:
    """
    Executes the main command and returns the output, command, time taken and pid of the process.
    """

    if sys.stdin.isatty():
        print("Error: No input provided through pipe.")
        sys.exit(1)
    cmd = sys.stdin.read().strip()

    start_time = time.time()

    if terminal_print == "on":
        results = capture(cmd)
    else:
        process = subprocess.Popen(
            cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        output, error = process.communicate()
        results = {"output": output, "error": error, "pid": process.pid}
    output = results["output"]
    error = results["error"]
    pid = results["pid"]

    end_time = time.time()
    time_taken = end_time - start_time
    return {
        "output": "\n".join(output),
        "command": "".join(cmd),
        "time_taken": time_taken,
        "pid": pid,
        "error": error if error != "" else "none",
    }
