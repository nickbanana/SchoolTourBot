from flask import Flask, request
import json
import os

app = Flask(__name__)

ACCESS_TOKEN = os.environ.get("TOKEN")

"""page_id 1704878453059005"""

@app.route("/webhook", methods=["GET"])
def webhook():
    verification_code='THIS_IS_SPARTA'
    verify_token=request.args.get('hub.verify_token')
    if verification_code == verify_token:
        return request.args.get('hub.challenge')

@app.route("/webhook", methods=["POST"])
def recv_msg():
    message_entries = json.loads(request.data.decode('utf8'))
    print(message_entries)
    print(type(message_entries))
    """
    print(message_entries['entry'][0]['messaging'][0]['message']['text'])
    
    for entry in message_entries:
        for message in entry['messaging']:
            if message.get('message'):
                print("{sender[id]} says {message[text]}".format(**message))
    """
    return "HI"


if __name__ == "__main__":
    app.run()