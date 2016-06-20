# A CatFacts slack bot, based on slack-starterbot
A simple Python-powered Slack bot, using [the Cat Facts API](https://catfacts-api.appspot.com).

## Steps to set up:
1. Set up a new Bot User, as instructed in the tutorial below (don't forget to invite your new bot user to one or more slack channels).
2. configure your bot token environment variable:
    * `export SLACK_BOT_TOKEN='your slack token pasted here'`
3. clone this repo and `cd` into the new directory
4. create a new virtualenv for the project, and activate it
5. run `pip install requirements.txt` to install the slackclient library
5. find your bot user ID and target user ID
    * option 1: visit the API page below and use a Ctrl-F search to find your bot and target user IDs by name
    * option 2: use the included python script, passing in the user name as an argument
6. configure your other environment variables:
    * `export CATFACT_BOT_TRIGGER_STRING="cat"`
    * `export CATFACT_BOT_TARGET_USER_ID="U1234Q03D:`
    * `export CATFACT_BOT_ID="U1234Q03D"`
7. start the bot (you should see the bot user become 'active' in slack)
    * `python starterbot.py`

[the starterbot tutorial](https://www.fullstackpython.com/blog/build-first-slack-bot-python.html)

[users.list API test page](https://api.slack.com/methods/users.list/test)
