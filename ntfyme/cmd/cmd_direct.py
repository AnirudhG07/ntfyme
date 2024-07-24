import subprocess
import sys
import time

from .live_capture import capture


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


def direct_exec(cmd, terminal_print, track_process):

    if cmd is None:
        print("Error: No input provided through direct execution.")
        sys.exit(1)

    start_time = time.time()
    if terminal_print == "on":
        results = capture(cmd, track_process)
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
    time_taken = seconds_to_time(time_taken)
    return {
        "output": output,
        "command": "".join(cmd),
        "time_taken": time_taken,
        "pid": pid,
        "error": error if error != "" else "none",
    }
