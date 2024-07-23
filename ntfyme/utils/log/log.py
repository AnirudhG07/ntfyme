import datetime
import os
import platform


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
    pid = log_dict["pid"]
    error = log_dict["error"]
    time_taken = log_dict["time_taken"]
    command = log_dict["command"]

    system = platform.system()
    if system not in ["Windows", "Linux"]:
        system = "Macos"

    log_dir = os.path.dirname(__file__)
    log_file = os.path.join(log_dir, "ntfyme.log")

    with open(log_file, "a") as lg:  # Note: Changed mode to "a" for appending
        status = "Successful" if error == "none" else "Error"
        lg.write(f"{log_time} :: PID: {pid} :: Status: {status}\n")
        lg.write(
            f"Command run: {command}\nTime taken: {time_taken} seconds :: OS: {system}\n"
        )
        lg.write(
            f"Key: {log_dict['key']} :: Execution{log_dict['execution']} :: Notify: {log_dict['notify']}\n"
        )
        lg.write(f"Error: {error}\n")
        lg.write("\n")


def log_add(results: dict, log_info: dict):
    """
    The log file adds log attribs to the log file
    The output include -
    * results dict
        * pid
        * command run
        * error (if any)
    * debug elements: log_info dict
    """
    log_dict = {
        "pid": results["pid"],
        "command": results["command"],
        "error": results["error"],
        "time_taken": results["time_taken"],
        "key": log_info["key"],
        "execution": log_info["execution"],
        "notify": log_info["notify"],
    }

    log_print(log_dict)
