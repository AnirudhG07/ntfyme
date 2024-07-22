# Gmail Setup

This walkthrough will guide you through setting up your Gmail to get mails from `ntfyme`.

But before we start, I will make the below claims for any security related concerns:

1. No form of mailing is done to any other email address other than the one you provide. You will mail yourself ONLY.
2. Your email address, password and any other sensitive information is not shared with any third party.
3. The code is open source and you can verify the code to see that it does not do anything malicious.
4. The code is run on your local machine and does not send any data to any other server.
5. Your `ntfyme_key` is not stored ANYWHERE in the code/by the code. You will have to provide it everytime you run with gmail enabled.

# ntfyme_key

Now let's discuss about usage of `ntfyme_key`. This key is made by you which the code will use to decrypt your gmail password and use it to send mails. This key is not stored anywhere in the code/by the code.

If you forget this key, no need to worry. Simply run the `ntfyme --interactive-setup` or in short `ntfyme -i` command to reset your details with your new key. This will overwrite your previous details. Please be mindful of the use and do not share this key with anyone. Providing this key to anyone will not be taken as a responsibility of the repository owner.

# Let's Start

To setup your gmail, you will need to configure your gmail security settings to allow apps to send mails. This is a one time setup and you will not have to do this again.

## Step 1: Allow Less Secure Apps

TBC
