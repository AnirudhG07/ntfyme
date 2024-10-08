Telegram Bot Setup
==================

This walkthrough will guide you through setting up your Telegram Bot to
get messages from ``ntfyme``.

But before we start, I will make the below claims for any security
related concerns:

1. No form of mailing is done to any other email address other than the
   one you provide. You will message yourself ONLY.
2. Your chat_id, bot token and any other sensitive information is not
   shared with any third party.
3. The code is open source and you can verify the code to see that it
   does not do anything malicious.
4. The code is run on your local machine and does not send any data to
   any other server.

**NOTE:** The chat_id and bot token are not encrypted for your own
convenience. This is because chat_id is a public information and bot
token can be changed anytime. However, if you feel the need to encrypt
it, please raise an issue on repository and this feature maybe added as
optional(currently not planned).

Let’s Start
===========

To setup your Telegram Bot, you will need to create a bot and get the
bot token and chat_id. This is a one time setup and you will not have to
do this again, unless you are changing your bot.

I am assuming you already have a Telegram account. If not, please create
one.

Step 1: Getting your Chat id
----------------------------

Open the below link in telegram to find your chat_id.

Link: https://t.me/raw_data_bot

Step 2: Create your telegram bot
--------------------------------

Open the BotFather link below to start creating your new bot.

Link: https://t.me/BotFather

Step 3: Setting up bot
----------------------

-  Now as your chat opens, type ``/start`` in the chat to get
   information about your new bot.
-  After this, click on ``/newbot`` or type it to create your new bot
-  Give the bot name to anything you like for example - ``ntfyme_bot``
-  From the message from BotFather, you have your new bot token which
   you will input in the ``ntfyme`` setup.

Once this is completed you will get a message containing the
``bot token`` which you will input to the ``ntfyme`` setup.

Step 4: Configuring ntfyme
--------------------------

Run the command -

.. code:: bash

   ntfyme -i

Enter ``2`` for telegram bot setup. Enter your chat_id and bot token you
have collected before.

AND YOU ARE DONE! Congratulations. If you have any issues, feel free to
raise an issue in the repository.
