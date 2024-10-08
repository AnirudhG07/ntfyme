Gmail Setup
===========

This walkthrough will guide you through setting up your Gmail to get
mails from ``ntfyme``.

But before we start, I will make the below claims for any security
related concerns:

1. No form of mailing is done to any other email address other than the
   one you provide. You will mail yourself ONLY.
2. Your email address, app password and any other sensitive information
   is not shared with any third party.
3. The code is open source and you can verify the code to see that it
   does not do anything malicious.
4. The code is run on your local machine and does not send any data to
   any other server.
5. Your ``ntfyme_key`` is not stored ANYWHERE in the code/by the code.
   You will have to provide it everytime you run with gmail enabled.

ntfyme_key
==========

Now let’s discuss about usage of ``ntfyme_key``. This key is made by you
which the code will use to decrypt your gmail app password and use it to
send mails. This key is not stored anywhere in the code/by the code.

If you forget this key, no need to worry. Simply run the
``ntfyme --interactive-setup`` or in short ``ntfyme -i`` command to
reset your details with your new key. This will overwrite your previous
details. Please be mindful of the use and do not share this key with
anyone. Providing this key to anyone will not be taken as a
responsibility of the repository owner.

Let’s Start
===========

To setup your gmail, you will need to configure your gmail security
settings to allow apps to send mails. This is a one time setup and you
will not have to do this again.

Step 1: Open Web Browser
------------------------

.. figure::
   https://github.com/user-attachments/assets/1f3cfee4-cdc3-4904-a6fe-9482107f5245
   :alt: PHOTO-2024-07-23-14-45-53

   PHOTO-2024-07-23-14-45-53

Go to ``Manage your Google Account``.

Step 2: Go to Security
----------------------

Go to ``Security``.

Step 3: Enable Two Factor Authorization
---------------------------------------

Scroll down and enable two factor authorization.

Turn on 2 factor authorization and Give your authentication passkeys
which the google asks for.

Step 4: Enabling App Password
-----------------------------

Come Back to the Security Page and search ``app password`` in search
bar.

Now, simply write your app name to anything like ``ntfyme_bot`` or
anything you wish.

Now copy the app password you are given. Save this APP PASSWORD since
you will be required to give this password to setup the GMAIL with
ntfyme.

Step 5: Configuring ntfyme
--------------------------

Run the command -

.. code:: bash

   ntfyme -i

Enter ``1`` for gmail setup. Enter your gmail id as well as your APP
PASSWORD you got. **NOTE:** It is recommended to not remove the spaces
between them, if you do then remember to remove it again next time you
configure GMAIL again.

Enter the ``ntfyme_key`` which you have to think and make it yourself.
And you are DONE!

Congratulations, you should be able to get email from ntfyme.
