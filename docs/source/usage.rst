🔨 Installation
===============

You can install this tool with the below options available:

Pypi Installation
-----------------

You can download this tool by running the below command -

.. code:: bash

   pip install ntfyme

..

   [!Tip]

   For Windows, you may get a mesage to add
   ``C:\Users\your\path\to\Python31x\Scripts``\ (whatever you get) to
   path, refer this
   `guide <https://stackoverflow.com/questions/44272416/how-to-add-a-folder-to-path-environment-variable-in-windows-10-with-screensho>`__.
   Please add it to the path in order to run ntfyme.

Homebrew Installation(for MacOS)
--------------------------------

This tool can downloaded from my Homebrew tap, by running the below
command -

.. code:: bash

   brew install anirudhg07/anirudhg07/ntfyme

Manual Installation
-------------------

You can download the source code from the repository and run the below
command to install the tool -

.. code:: bash

   git clone https://github.com/AnirudhG07/ntfyme.git
   cd ntfyme
   pip install .

..

   [!Important]

   WSL will be counted as windows instead of linux, thus notifications
   will be done through “plyer” library instead of linux notify-send. To
   complete the installation process for WSL, please run
   `wsl.sh <https://github.com/AnirudhG07/ntfyme/blob/main/docs/setup_guide/wsl.sh>`__
   script in your WSL terminal with sudo permissions. You can do this by
   running -

.. code:: bash

   chmod +x wsl.sh
   sudo ./wsl.sh
