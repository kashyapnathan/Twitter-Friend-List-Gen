# Twitter List Friends Generation Script

This is a script that allows you to create a Twitter List on your account with all the people that someone is following on your account. Just input the desired user and you're all set!

I used Python to write the script itself, invoking the Twitter API via the the [Tweepy](https://www.tweepy.org/) library to both read a given user's "friends" (people they follow) and subsequently write a new list to the given account.

## How to Use this Script

1. Get a Twitter Developer Account in your username by going to https://developer.twitter.com/en/apply-for-access.

2. Create a new app under "Standard" (so you can get V2 access to the API) and retrieve your:

> - API Key
> - API Key Secret
> - Access Token
> - Access Token Secret

**NOTE:** If this script doesn't work the first time even after authentication, try regenerating all your keys and using those.

3. Make sure you have the latest version of python3 installed. If you don't, run the following in your home directory:

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)" && brew install python
```

Afterwards, check if you have python3 installed by running ``python3 --version`` — if you get back a python version number above 3, you're all set!

4. Open up terminal and clone this repo in your home directory by running the command:

```
git clone https://github.com/nstrike2/twitter-list-friends-generation-script.git
```

While in the same home directory (one level up from the ``twitter-list-friends-generation-script`` directory), run:

```
chmod 777 twitter-list-friends-generation-script/driver.sh && ./twitter-list-friends-generation-script/driver.sh
```

5. Input all the requested information from the prompts, and you should be set!

**NOTE:** If you're serious about using this script, I would highly suggest upgrading to a paid [Twitter Enterprise Developer Account](https://developer.twitter.com/en/products/twitter-api/enterprise). Twitter is very aggressive with their rate limits for standard accounts, which could hinder your download capacity.
