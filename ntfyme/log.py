import datetime

def log_print(log_dict):
    """
    The log file prints prints the formatted log file.
    Format is - 
    Time: <time> :: PID: <pid> :: Error status: Successful/Error
    Command run: <command> :: Time taken: <time_taken> seconds
    Error: <error> (if any)
    Debug elements TBD
    """
    log_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pid = log_dict['pid']
    error = log_dict['error']
    time_taken = log_dict['time_taken']
    command = log_dict['command']

    with open('./settings/ntfyme.log', "a") as lg:  # Note: Changed mode to "a" for appending
        status = f"Successful" if error == 'none' else f"Error"
        lg.write(f"{log_time} :: PID: {pid} :: Status: {status}\n")
        lg.write(f"Command run: {command} :: Time taken: {time_taken} seconds\n")
        lg.write(f"Error: {error}\n")
        lg.write("\n")  

def log_add(results):
    """
    The log file adds log attribs to the log file
    The output include -
        * pid
        * command run
        * error (if any)
        * debug elements TBD
    """
    log_dict = {
        'pid': results['pid'],
        'command': results['command'],
        'error': results['error'],
        'time_taken': results['time_taken']
    }

    log_print(log_dict)
           
