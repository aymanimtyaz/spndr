'''**********************************************************************************************

This is a simple wrapper class that implements a low level abstraction on the calling of the 
telegram API. Please go to https://core.telegram.org/bots/api to look at the API's documentation 
and to gain a better understanding of how this wrapper works.

**********************************************************************************************'''

import requests, json, os

class communicate:

    service_url_prefix = 'https://api.telegram.org/bot'

    def __init__(self, offset=0, limit=1, timeout=100, allowed_updates=[], init=0):
        self.token = open(os.getcwd()+'//bot_token.txt').read()
        self.offset = offset
        self.limit = limit
        self.timeout = timeout
        self.allowed_updates = allowed_updates
        self.data = None
        self.init = init



    ''' receive() implements the /getUpdates method of the API, all the parameters for this call 
        have been taken as attributes of the calling object'''
    def receive(self):
        api_params = {"offset":self.offset, "limit":self.limit,
                      "timeout":self.timeout, "allowed_updates":self.allowed_updates}
        #print("waiting for input")
        req_obj = requests.get(self.service_url_prefix+self.token+'/getUpdates', 
                               params=api_params)
        self.data = req_obj.json()
        #print(json.dumps(self.data, indent=4))
        if len(self.data['result'])==0:
            self.data=None
            return self.data
        if self.init == 0:
            self.offset = self.data['result'][-1]['update_id']
            self.init+=1
        self.offset+=1
        return 


    ''' sendMsg() implements the /sendMessage method of the API, the necessary parameters for this
        call are the chat id which is unique for each chat/user and the text message to send '''
    def sendMsg(self, chat_id, text):
        api_params = {"chat_id":chat_id, "text":text}

        req_obj = requests.get(self.service_url_prefix+self.token+'/sendMessage',
                               params=api_params)

        json_resp = req_obj.json()
        #print(json.dumps(json_resp, indent=4))


    ''' getMsg() calls receive() to get a json object back, from which it extracts the oldest
        untracked message from the API '''
    def getMsg(self):
        self.receive()
        if self.data == None:
            return self.getMsg()
        else:
            message_body=self.data['result'][-1]['message']['text']
            chat_id=self.data['result'][-1]['message']['chat']['id']
            update_id=self.data['result'][-1]['update_id']
            return [message_body, chat_id, update_id]






    








