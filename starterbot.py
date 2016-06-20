import json
import os
import time
import urllib2

from slackclient import SlackClient


# constants
TRIGGER = os.environ.get('CATFACT_BOT_TRIGGER_STRING')
USER_ID = os.environ.get('CATFACT_BOT_TARGET_USER_ID')
BOT_ID = os.environ.get('CATFACT_BOT_ID')

# instantiate Slack client
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))


def parse_slack_output(slack_rtm_output):
    """
    The Slack Real Time Messaging API is an events firehose.
    This parsing function scans the content for the TRIGGER string (also not sent by the Bot itself),
    and if found, calls the catfacts API.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and TRIGGER in output['text'] and BOT_ID != output['user']:
                print "getting cat fact ..."
                return get_cat_fact()

    return None


def get_cat_fact():
    """
    Hit the CatFacts API and get some cat knowledge
    :return: String
    """

    url = 'http://catfacts-api.appspot.com/api/facts?number=1'
    response = json.load(urllib2.urlopen(url))

    if response['success'] == "true":
        return response['facts'][0]

    else:
        return 'Kitty loves you'


def send_cat_fact(cat_fact):

    # first, we open the IM channel
    result = slack_client.api_call("im.open", user=USER_ID)

    if 'ok' in result and result['ok'] == 'success':
        print 'error opening the IM channel'
        return

    else:
        channel_id = result['channel']['id']

        # then we send the message
        slack_client.api_call("chat.postMessage", channel=channel_id, text=cat_fact, as_user=True)

if __name__ == "__main__":

    if not TRIGGER or not USER_ID or not BOT_ID:
        print("One or more required environment variables are missing.")
        print("CATFACT_BOT_TRIGGER_STRING: {}".format(TRIGGER))
        print("CATFACT_BOT_TARGET_USER_ID: {}".format(USER_ID))
        print("CATFACT_BOT_ID: {}".format(BOT_ID))
        exit()

    READ_WEBSOCKET_DELAY = 1  # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("StarterBot connected and running!")
        while True:
            output = parse_slack_output(slack_client.rtm_read())
            if output:
                print output
                send_cat_fact(output)

            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token?")
