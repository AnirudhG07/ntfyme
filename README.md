# ntfyme

Have you ever wanted a simple tool in your terminal which gives you notification when the program is done, like some computer notification or some mail.
This tool helps you ease your life with appropriate notifications you can set in your OS, get mail regarding it and best of all, it is VERY SIMPLE TO USE!
<br>

`ntfyme` stands for 'notify-me', obviously! So just write your command and pipe the notification of its Error(or Success) with ntfyme.

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Previews/Screenshots](#previewsscreenshots)
- [Features](#features)
- [Usages](#usages)
  - [1. Direct Run](#1-direct-run)
  - [2. Piping the command](#2-piping-the-command)
- [Installation](#installation)
  - [Pypi Installation](#pypi-installation)
  - [Homebrew Installation(for MacOS)](#homebrew-installationfor-macos)
  - [Manual Installation](#manual-installation)
- [Getting Started](#getting-started)
- [Configurations](#configurations)
- [Contribute](#contribute)

## Previews/Screenshots

TBD

## Features

- Very easy to use and setup.
- Cross platform support for Windows, MacOS and Linux.
- Get local notifications when your command is done.
- Get notifications like gmail, telegram bot, etc. when your command is done.
- Get information about output, errors, time taken, pid and more in the notification.
- Track your process for possible suspensions and get notified after thorough diagnostics.

## Usages

Say you want to run your terminal command called `<command>`, which can be running some python script, some shell scripts, or any terminal regular command.

There are mainly two ways to use the tool to get a notification -

### 1. Direct Run

For "direct running", you can follow the below format -

```bash
ntfyme -c <command>
```

### 2. Piping the command

For "piping the command", you can follow the below format -

```bash
echo <command> | ntfyme
```

Both the above commands will give the SAME output, a notification when the command is done.

> For Windows, it is recommended to enclose you commands in double quotes. For example - `ntfyme -c "echo hi"`.

### More examples

1. To run multiple commands, you can use the `"multiple commands"` syntax to input to ntfyme. For example -

```bash
echo "echo hi; touch hello.txt; echo 'What a day!' > hello.txt" | ntfyme
```

The net output will be outputted for such commands with an overall diagnostics instead of seperate for each command.

2. Running ssh will not work with ntfyme. Although one can use it to test the connection and then run the command. For example -

```bash
echo "nmap 1.1.1.1 -p 22" | ntfyme
```

This command may take some time to run, but will give you a notification when the command is done.

3. If you would like to get notifications for an ssh command, you would need to install `ntfyme` on the remote machine, give your gmail id and app password in the `config.toml`.

## Installation

You can install this tool with the below options available:

### Pypi Installation

You can download this tool by running the below command -

```bash
pip install ntfyme
```

### Homebrew Installation(for MacOS)

This tool can downloaded from my Homebrew tap, by running the below command -

```bash
brew install anirudhg07/anirudhg07/ntfyme
```

### Manual Installation

You can download the source code from the repository and run the below command to install the tool -

```bash
git clone https://github.com/AnirudhG07/ntfyme.git
cd ntfyme
pip install .
```

## Getting Started

To get started with `ntfyme`, first download the tool using the above installation methods. To enable notifications through gmail or telegram bot, you will need to setup the respective services manually. The guides to setup the services are mentioned in the docs.

To know more about the `config.toml` and configurations, read below.

## Configurations

`ntfyme` allows you to configure the tool according to your needs. The configurations are stored in the `config.toml` which you can open using root privilages while running `ntfyme --config`. Let's understand some of the configurations below.

`ntfyme` uses `on/off` to enable/disable ny settings. Please do not input any other values other than `on/off` for the `enabled` option. The comments for each option is mentioned, please read them before changing any option. They will give a thorough idea about the configurations and their usage.
Please do not mess around with the `config.toml` file, as it may lead to some errors in the tool.

## Contribute

You are very welcome to contribute to this project. If you find bugs, or more API's for notifications, some more features, etc. feel free to create an issue, discuss and then make a PR. To make `ntfyme` better and used throughout the world, please star and share this repo to everyone!
