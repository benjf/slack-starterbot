import os
import sys
from slackclient import SlackClient

if len(sys.argv) != 2:
    print("User Name must be passed in as the only argument on the command line.")
    exit()

slack_token = os.environ.get('SLACK_BOT_TOKEN')

if not slack_token:
    print("Slack token environment variable is missing: SLACK_BOT_TOKEN")
    exit()

user_name = sys.argv[1]

slack_client = SlackClient(slack_token)

if __name__ == "__main__":
    api_call = slack_client.api_call("users.list")
    if api_call.get('ok'):
        # retrieve all users so we can find our bot
        users = api_call.get('members')
        for user in users:
            if 'name' in user and user.get('name') == user_name:
                print("User ID for [{}] is [{}]".format(user['name'], user.get('id')))
    else:
        print("Could not find user with the name: ".format(user_name))
