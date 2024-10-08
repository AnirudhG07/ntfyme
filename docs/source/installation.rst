🔥 Usages
=========

Say you want to run your terminal command called ``<command>``, which
can be running some python script, some shell scripts, or any terminal
regular command.

There are mainly two ways to use the tool to get a notification -

1. Direct Run
-------------

For “direct running”, you can follow the below format -

.. code:: bash

   ntfyme exec -c <command>

2. Piping the command
---------------------

For “piping the command”, you can follow the below format -

.. code:: bash

   echo <command> | ntfyme exec

Both the above commands will give the SAME output, a notification when
the command is done.

   [!Note]

   For Windows, it is recommended to enclose you commands in double
   quotes. For example - ``ntfyme exec -c "echo hi"``.

More examples
-------------

1. To run multiple commands, you can use the ``"multiple commands"``
   syntax to input to ntfyme. For example -

.. code:: bash

   echo "echo hi; touch hello.txt; echo 'What a day!' > hello.txt" | ntfyme exec

The net output will be outputted for such commands with an overall
diagnostics instead of seperate for each command.

2. Running ssh will not work with ntfyme. Although one can use it to
   test the connection and then run the command. For example -

.. code:: bash

   echo "nmap 1.1.1.1 -p 22" | ntfyme exec

This command may take some time to run, but will give you a notification
when the command is done.

3. If you would like to get notifications for an ssh command, you would
   need to install ``ntfyme`` on the remote machine, give your gmail id
   and app password in the ``config.toml``.
