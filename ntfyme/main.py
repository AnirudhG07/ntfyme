from argparse import ArgumentParser

from notification import notify

from .cmd.cmd_direct import direct_exec
from .cmd.cmd_pipe import pipe_exec
from .utils.log.log import log_add


def temp_print(result):
    print(f"Output: {result['output']}")
    print(f"Command run: {result['command']}")
    print(f"Time taken: {result['time_taken']} seconds")
    print(f"PID: {result['pid']}")
    print(f"Error: {result['error']}")


def main():
    """
    -> Handles the flags and errors
    -> calls functions based on the flags

    Arguments:
        None: Assumes the user wants to run the main command through pipe
        --cmd or -c : Input the command to cli as 'ntfyme --cmd <command>'
        log : The command log of ntfyme
        config: The configuration file of ntfyme

        --help or -h : Shows the help message
        --version or -v : Shows the version of the program
    """

    parser = ArgumentParser(description="ntfyme")
    parser.add_argument("--cmd", "-c", help="Run the command through direct execution")
    parser.add_argument("--log", "-l", nargs="?", help="The command log of ntfyme")
    parser.add_argument("--config", nargs="?", help="The configuration file of ntfyme")

    args = parser.parse_args()

    # Handling log and config arguments
    if args.log:
        print(f"Command log: {args.log}")
    if args.config:
        print(f"Configuration file: {args.config}")

    # Handling --fg and --cmd flags
    if args.cmd:
        result = direct_exec(args.cmd)
        log_add(result)
        temp_print(result)

    else:
        result = pipe_exec()
        log_add(result)
        temp_print(result)

    notify(result)
    return 0


if __name__ == "__main__":
    main()
