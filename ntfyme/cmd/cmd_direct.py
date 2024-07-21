import subprocess
import time
import sys

def direct_exec(cmd):

    if cmd is None:
        print("Error: No input provided through direct execution.")
        sys.exit(1)
        
    start_time = time.time()
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, error = process.communicate()
    end_time = time.time()

    time_taken = end_time - start_time
    return {
        'output': output.strip(),
        'command': ''.join(cmd),
        'time_taken': time_taken,
        'pid': process.pid,
        'error': error.strip() if error else 'none'
    }
