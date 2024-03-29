from flask import Flask, request, send_file
import json
import os
import requests
from io import BytesIO

from fsm import TourMachine

timestamp = -1
app = Flask(__name__)

message_entry = None


"""page_id 1704878453059005"""

machine = TourMachine(
    states=[
        'user',
        'liberal',
        'science',
        'management',
        'engineering',
        'eecs',
        'css',
        'cpd',
        'bb',
        'med',
        'detail_liberal',
        'detail_science',
        'detail_management',
        'detail_engineering',
        'detail_eecs',
        'detail_css',
        'detail_cpd',
        'detail_bb',
        'detail_med',
        'gif',
        'gif_detail'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'liberal',
            'conditions': 'is_going_to_liberal',
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'science',
            'conditions': 'is_going_to_science',
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'management',
            'conditions': 'is_going_to_management',
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'engineering',
            'conditions': 'is_going_to_engineering',
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'eecs',
            'conditions': 'is_going_to_eecs',
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'css',
            'conditions': 'is_going_to_css',
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'cpd',
            'conditions': 'is_going_to_cpd',
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'bb',
            'conditions': 'is_going_to_bb',
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'med',
            'conditions': 'is_going_to_med',
        },
        {
            'trigger': 'advance',
            'source': 'liberal',
            'dest': 'detail_liberal',
            'conditions': 'is_going_to_detail'
        },
        {
            'trigger': 'advance',
            'source': 'science',
            'dest': 'detail_science',
            'conditions': 'is_going_to_detail'
        },
        {
            'trigger': 'advance',
            'source': 'management',
            'dest': 'detail_management',
            'conditions': 'is_going_to_detail'
        },
        {
            'trigger': 'advance',
            'source': 'engineering',
            'dest': 'detail_engineering',
            'conditions': 'is_going_to_detail'
        },
        {
            'trigger': 'advance',
            'source': 'eecs',
            'dest': 'detail_eecs',
            'conditions': 'is_going_to_detail'
        },
        {
            'trigger': 'advance',
            'source': 'css',
            'dest': 'detail_css',
            'conditions': 'is_going_to_detail'
        },
        {
            'trigger': 'advance',
            'source': 'cpd',
            'dest': 'detail_cpd',
            'conditions': 'is_going_to_detail'
        },
        {
            'trigger': 'advance',
            'source': 'bb',
            'dest': 'detail_bb',
            'conditions': 'is_going_to_detail'
        },
        {
            'trigger': 'advance',
            'source': 'med',
            'dest': 'detail_med',
            'conditions': 'is_going_to_detail'
        },
        {
            'trigger': 'advance',
            'source': [
                'liberal',
                'science',
                'management',
                'engineering',
                'eecs',
                'css',
                'cpd',
                'bb',
                'med'
            ],
            'dest':'user',
            'conditions': 'is_going_user'
        },
        {
            'trigger': 'go_back',
            'source': [
                'detail_liberal',
                'detail_science',
                'detail_management',
                'detail_engineering',
                'detail_eecs',
                'detail_css',
                'detail_cpd',
                'detail_bb',
                'detail_med'
            ],
            'dest':'user'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'gif',
            'conditions': 'is_going_to_gif'
        },
        {
            'trigger': 'advance',
            'source': 'gif',
            'dest': 'gif_detail',
            'conditions': 'is_going_to_gif_detail'
        },
        {
            'trigger': 'go_back',
            'source': 'gif_detail',
            'dest': 'gif'
        },
        {
            'trigger': 'advance',
            'source': 'gif',
            'dest': 'user',
            'conditions': 'is_going_to_main_from_gif'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'user',
            'conditions': 'is_first_entry'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)







@app.route("/webhook", methods=["GET"])
def webhook():
    verification_code='THIS_IS_SPARTA'
    verify_token=request.args.get('hub.verify_token')
    if verification_code == verify_token:
        return request.args.get('hub.challenge')

@app.route("/webhook", methods=["POST"])
def recv_msg_and_reply():
    message_entries = json.loads(request.data.decode('utf8'))
    '''print(message_entries)'''
    global timestamp
    event = message_entries['entry'][0]['messaging'][0]
    if timestamp != event['timestamp'] and 'message' in event:
        print("timestamp:{0}".format(timestamp))
        timestamp = event['timestamp']
        print("timestamp:{0}".format(timestamp))
        machine.advance(event)
        return "OK"
    else:
        return "NOT_OK"

@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.get_graph().draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')




if __name__ == "__main__":
    
    app.run()