import subprocess
import sys
import time


def direct_exec(cmd, terminal_print):

    if cmd is None:
        print("Error: No input provided through direct execution.")
        sys.exit(1)

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
