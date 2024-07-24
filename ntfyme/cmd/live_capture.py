import subprocess
import sys
import threading
import os

def read_output(pipe, output_list, print_func):
    """Read lines or characters from a pipe and print them, storing them in a list."""
    while True:
        data = pipe.read(1)  # Read one character at a time
        if not data:
            break
        output_list.append(data)
        print_func(data, end='', flush=True)

def capture(cmd):
    # Set the PYTHONUNBUFFERED environment variable to force unbuffered output
    env = os.environ.copy()
    env["PYTHONUNBUFFERED"] = "1"

    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True, bufsize=0, env=env)
    output, error = [], []
    
    stdout_thread = threading.Thread(target=read_output, args=(process.stdout, output, print))
    stderr_thread = threading.Thread(target=read_output, args=(process.stderr, error, lambda x, **kwargs: print(x, file=sys.stderr, **kwargs)))
    
    stdout_thread.start()
    stderr_thread.start()
    
    stdout_thread.join()
    stderr_thread.join()
    
    process.wait()

    return {
        "output": "".join(output),
        "error": "".join(error),
        "pid": process.pid,
    }
