.. bept documentation master file, created by
   sphinx-quickstart on Tue Oct  1 23:44:33 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

:Release: |release|
:Date: |today|


NTFYME 
====
Have you ever wanted a simple tool in your terminal which gives you
notification when the program is done, like some computer notification
or some mail. This tool helps you ease your life with appropriate
notifications you can set in your OS, get mail regarding it and best of
all, it is VERY SIMPLE TO USE!

``ntfyme`` stands for ‘notify-me’, obviously! So just write your command
and pipe the notification of its Error(or Success) with ntfyme.

For more information, visit the official [Github](https://github.com/AnirudhG07/ntfyme) repository.


⚡ Features
-----------

-  ✨ Very easy to use and setup.
-  ✨ Cross platform support for Windows, MacOS and Linux.
-  ✨ Get local notifications when your command is done.
-  ✨ Get notifications like gmail, telegram bot, etc. when your command
   is done.
-  ✨ Get information about output, errors, time taken, pid and more in
   the notification.
-  ✨ Track your process for possible suspensions and get notified after
   thorough diagnostics.
-  ✨ Enhanced UI features powered by rich and beaupy.

OS’s Supported
--------------

ntfyme is supported on all major OS's and distributions.

It is available for MacOS, Linux and Windows. It is also available for WSL usages, but with some more dependencies which needs to be installed as mentioned in the repository.


⭐ Getting Started
------------------

To get started with `ntfyme`, first download the tool using the above installation methods. To enable notifications through gmail or telegram bot, you will need to setup the respective services manually. The guides to setup the services are mentioned in the docs.

To know more about the `config.toml` and configurations, read below.

Configurations
--------------

`ntfyme` allows you to configure the tool according to your needs. The configurations are stored in the `config.toml` which you can open using root privilages while running `ntfyme --config`. Let's understand some of the configurations below.

`ntfyme` uses `on/off` to enable/disable ny settings. Please do not input any other values other than `on/off` for the `enabled` option. The comments for each option is mentioned, please read them before changing any option. They will give a thorough idea about the configurations and their usage.
Please do not mess around with the `config.toml` file, as it may lead to some errors in the tool.

Contribute
----------

You are very welcome to contribute to this project. If you find bugs, or more API's for notifications, some more features, etc. feel free to create an issue, discuss and then make a PR. To make `ntfyme` better and used throughout the world, please star and share this repo to everyone!

========
Contents
========

.. toctree::
   :maxdepth: 2

   installtion
   setup_guide/gmail
   setup_guide/telegram_bot
   usage
   ntfyme_key


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


