import datetime
import os
import platform


def log_print(log_dict):
    """
    The log file prints prints the formatted log file.
    """
    log_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pid = log_dict["pid"]
    time_taken = log_dict["time_taken"]
    command = log_dict["command"]
    track_process = log_dict["track_process"]
    return_code = log_dict["return_code"]
    remarks = log_dict["remarks"]

    system = platform.system()
    if system not in ["Windows", "Linux"]:
        system = "Macos"

    log_dir = os.path.dirname(__file__)
    log_file = os.path.join(log_dir, "ntfyme.log")

    with open(log_file, "a") as lg:
        status = "Successful" if return_code == 0 else "Error"
        lg.write(f"{log_time} :: PID: {pid} :: Status: {status}\n")
        lg.write(
            f"Command run: {command}\nTime taken: {time_taken} seconds :: OS: {system}\n"
        )
        lg.write(
            f"Key: {log_dict['key']} :: Execution : {log_dict['execution']} :: Notify: {log_dict['notify']} :: Track-Process: {track_process}\n"
        )
        lg.write(f"Return Code: {str(return_code)} :: Remarks: {remarks}\n")
        lg.write("\n")


def log_add(results: dict, log_info: dict):
    """
    The log file adds log attribs to the log file
    The output include -
    * results dict
    * debug elements: log_info dict
    """
    log_dict = {
        "pid": results["pid"],
        "command": results["command"],
        "time_taken": results["time_taken"],
        "return_code": results["return_code"],
        "remarks": results["remarks"],
        "key": log_info["key"],
        "execution": log_info["execution"],
        "notify": log_info["notify"],
        "track_process": log_info["track_process"],
    }

    log_print(log_dict)
