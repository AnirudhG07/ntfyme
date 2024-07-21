from argparse import ArgumentParser

from cmd_pipe import pipe_exec
from cmd_direct import direct_exec

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
        --fg or -f : Does not send the process to the background
        --cmd or -c : Input the command to cli as 'ntfyme --cmd <command>'
        log : The command log of ntfyme
        config: The configuration file of ntfyme

        --help or -h : Shows the help message
        --version or -v : Shows the version of the program
    """

    parser = ArgumentParser(description="ntfyme")
    parser.add_argument("--fg", "-f", action="store_true", help="Run the process in the foreground")
    parser.add_argument("--cmd", "-c", help="Run the command through direct execution")
    parser.add_argument("--log", nargs='?', help="The command log of ntfyme")
    parser.add_argument("--config", nargs='?', help="The configuration file of ntfyme")

    args = parser.parse_args()

    # Handling log and config arguments
    if args.log:
        print(f"Command log: {args.log}")
    if args.config:
        print(f"Configuration file: {args.config}")

    # Handling --fg and --cmd flags
    if args.cmd:
        result = direct_exec(args.cmd)
        temp_print(result)
        if args.fg:
            pass
        else:
            # Then piping is used.
            pass 
    else:
        result = pipe_exec()
        temp_print(result)

    
if __name__ == "__main__":
    main()