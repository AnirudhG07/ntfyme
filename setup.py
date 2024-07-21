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
"""

setup(
    name="ntfyme",
    version="0.0.1",
    description="",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/AnirudhG07/ntfyme",
    author="Anirudh Gupta",
    package_data={},
    packages=find_packages(),
    install_requires=["toml, pyler"],
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
