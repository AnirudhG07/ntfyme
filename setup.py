import gzip
import os
import platform
import shutil

from setuptools import find_packages, setup


def install_man_page():
    source_path = os.path.join("docs", "man", "ntfyme.1")
    dest_path = os.path.join("/usr/local/", "share", "man", "man1", "ntfyme.1.gz")

    # Compress the man page
    with open(source_path, "rb") as src, gzip.open(dest_path, "wb") as dst:
        shutil.copyfileobj(src, dst)


description = """
Have you ever wanted a simple tool in your terminal which gives you notification when the program is done, like some computer notification or some mail.
This tool helps you ease your life with appropriate notifications you can set in your OS, get mail regarding it and best of all, it is VERY SIMPLE TO USE!

## Features

- Very easy to use and setup.
- Cross platform support for Windows, MacOS and Linux.
- Get local notifications when your command is done.
- Get notifications like gmail, telegram bot, etc. when your command is done.
- Get information about output, errors, time taken, pid and more in the notification.

## Usages
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

For more information, visit the official github repository https://github.com/AnirudhG07/ntfyme
"""

setup(
    name="ntfyme",
    version="0.0.1",
    description="Simple notification tool to notify yourself when a long running process ends with local ping, gmail, telegram, etc.",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/AnirudhG07/ntfyme",
    author="Anirudh Gupta",
    package_data={
        "ntfyme": ["config.toml", "utls/log/ntfyme.log"],
    },
    packages=find_packages(),
    install_requires=[
        "toml",
        "pyler",
        "tomlkit",
        "cryptography",
        "smtplib",
        "selectors",
        "threading",
    ],
    keywords=["notification", "notify", "cli", "python"],
    python_requires=">=3.11",
    entry_points={
        "console_scripts": [
            "ntfyme=ntfyme.main:main",
        ],
    },
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
    ],
)
