# ntfyme

Have you ever wanted a simple tool in your terminal which gives you notification when the program is done, like some computer notification or some mail.
This tool helps you ease your life with appropriate notifications you can set in your OS, get mail regarding it and best of all, it is VERY SIMPLE TO USE!

<br>

`ntfyme` stands for 'notify-me', obviously! So just write your command and pipe the notification of its Error(or Success) with ntfyme.

## Table of Contents

- [Previews/Screenshots](#previewsscreenshots)
- [Features](#features)
- [Usages](#usages)
  - [1. Direct Run](#1-direct-run)
  - [2. Piping the command](#2-piping-the-command)
- [Installation](#installation)
  - [Pypi Installation](#pypi-installation)
  - [Homebrew Installation(for MacOS)](#homebrew-installationfor-macos)
  - [Manual Installation](#manual-installation)
- [Configurations](#configurations)

## Previews/Screenshots

TBD

## Features

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

## Configurations
