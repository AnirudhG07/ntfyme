import subprocess
import sys
import time

from .live_capture import capture


def direct_exec(cmd, terminal_print):

    if cmd is None:
        print("Error: No input provided through direct execution.")
        sys.exit(1)

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
        "output": output,
        "command": "".join(cmd),
        "time_taken": time_taken,
        "pid": pid,
        "error": error if error != "" else "none",
    }
