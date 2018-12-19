import requests
import json
import random
import os

GRAPH_URL = "https://graph.facebook.com/v3.2"
GIPHY_URL = "https://api.giphy.com/v1/gifs/search?api_key="
ACCESS_TOKEN = os.environ.get("TOKEN")
GIPHY_TOKEN = os.environ.get("API")

def get_GIPHY(keyword):
    url = "{0}{1}&q={2}&limit=25&offset=0&rating=G&lang=en".format(GIPHY_URL,GIPHY_TOKEN,keyword)
    index = random.randint(0,24)
    r = requests.get(url)
    r = r.json()

    return r['data'][index]['images']['original']['url'] 

def send_message(id,text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL,ACCESS_TOKEN)
    payload = {
        "messaging_type": "RESPONSE",
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("unable to send message\n")

    return response.text

def send_GIPHY(id,text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL,ACCESS_TOKEN)
    giphy_url = get_GIPHY(text)
    payload = {
        "messaging_type": "RESPONSE",
        "recipient": {"id": id},
        "message": {
            "attachment": {
                "type" : "image",
                "payload": {
                    "url": giphy_url
                }
            } 
        }
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("unable to send image message\n")

    return response.text