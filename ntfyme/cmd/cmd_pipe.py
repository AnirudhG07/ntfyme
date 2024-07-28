import subprocess
import sys
import time

from .live_capture import *

def seconds_to_time(seconds):
    """
    Converts seconds to human readable time format.
    """
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    if h == 0:
        if m == 0:
            return f"{s}"
        return f"{m} minutes {s}"
    return f"{h} hours {m} minutes {s}"


def pipe_exec(terminal_print, track_process) -> dict:
    """
    Executes the main command and returns the output, command, time taken and pid of the process.
    """

    if sys.stdin.isatty():
        print("Error: No input provided through pipe.")
        sys.exit(1)
    cmd = sys.stdin.read().strip()

    start_time = time.time()

    if terminal_print == "on":
        results = capture(cmd, track_process)
    else:
        process = subprocess.Popen(
            cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        output, error = process.communicate()
        results = {
            "output": output,
            "error": error,
            "pid": process.pid,
            "return_code": process.returncode,
        }
    output = results["output"]
    error = results["error"]
    pid = results["pid"]
    return_code = results["return_code"]

    end_time = time.time()
    time_taken = end_time - start_time
    time_taken = seconds_to_time(time_taken)

    return {
        "output": "\n".join(output),
        "command": "".join(cmd),
        "time_taken": time_taken,
        "pid": pid,
        "error": error if return_code != 0 else "none",
        "return_code": return_code,
        "remarks": remarks(return_code),
    }
