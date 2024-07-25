# ntfyme

> A python based tool to track and notify your long running process on termination.
> Send notification with Gmail, Telegram and more with success/error messages.
> More information: <https://github.com/AnirudhG07/ntfyme>.

- Directly run your command:

`ntfyme {{-c|--cmd}} {{COMMAND}}`

- Pipe your command and run:

`echo {{COMMAND}} | ntfyme`

- Run multiple commands by enclosing them in quotes:

`echo "{{COMMAND1; COMMAND2; COMMAND3}}" | ntfyme`

- Track and terminate your process after prolong suspension:

`ntfyme {{-t|--track-process}} {{-c|--cmd}} {{COMMAND}}`

- Setup the tool configurations interactively:

`ntfyme {{-i|--interactive-setup}}`

- Encrypt your password:

`ntfyme {{-e|--enc}} {{PASSWORD}}`

- See the log history:

`ntfyme {{--log}}`

- Open and edit the configuration file:

`ntfyme {{--config}}`
