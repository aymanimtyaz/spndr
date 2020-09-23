'''**********************************************************************************************

This is a simple wrapper class that implements a low level abstraction on the calling of the 
telegram API. Please go to https://core.telegram.org/bots/api to look at the API's documentation 
and to gain a better understanding of how this wrapper works.

**********************************************************************************************'''

import requests
import json
import os

class communicate:

    service_url_prefix = 'https://api.telegram.org/bot'

    def __init__(self, offset=0, limit=100, timeout=0, allowed_updates=[]):
        self.token = open(os.getcwd()+'//bot_token.txt').read()
        self.offset = offset
        self.limit = limit
        self.timeout = timeout
        self.allowed_updates = allowed_updates


    ''' receive() implements the /getUpdates method of the API, all the parameters for this call 
        have been taken as attributes of the calling object'''
    def receive(self):
        api_params = {"offset":self.offset, "limit":self.limit,
                      "timeout":self.timeout, "allowed_updates":self.allowed_updates}
        req_obj = requests.get(self.service_url_prefix+self.token+'/getUpdates', 
                               params=api_params)
        json_resp = req_obj.json()
        print(json.dumps(json_resp, indent = 4))


    ''' send() implements the /sendMessage method of the API, the necessary parameters for this
        call are the chat id which is unique for each chat/user and the text message to send '''
    def send(self, chat_id, text):
        api_params = {"chat_id":chat_id, "text":text}

        req_obj = requests.get(self.service_url_prefix+self.token+'/sendMessage',
                               params=api_params)

        json_resp = req_obj.json()
        print(json.dumps(json_resp, indent=4))


    








