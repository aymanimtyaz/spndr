from telegrambot import communicate
import json


''' FUNCTION TO INITIALIZE communicate() class OBJECT WHENEVER ANY OF THE SUBSEQUENT 
    METHODS ARE CALLED '''
def init_obj(fn):
    com = communicate()
    def wrapper(*kargs, **kwargs):
        return fn(com, kargs, kwargs)
    return wrapper

''' FUNCTION TO RECEIVE THE LATEST UNREAD MESSAGE '''
@init_obj
def getMsg(*args):
    json_obj = None
    while json_obj is None:
        json_obj = args[0].receive()

    sender_id = json_obj['result'][-1]['message']['from']['id']
    chat_id = json_obj['result'][-1]['message']['chat']['id']
    update_id = json_obj['result'][-1]['update_id']

    try:
        message_body = json_obj['result'][-1]['message']['text']
    except KeyError:
        return sender_id, '!non_text_input', chat_id, update_id

    message_body = json_obj['result'][-1]['message']['text']
    return sender_id, message_body, chat_id, update_id

''' FUNCTION TO SEND MESSAGE '''
@init_obj
def sendMsg(*args):
    args[0].send(args[1][0], args[1][1])
    