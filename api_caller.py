from telegrambot import communicate


''' FUNCTION TO INITIALIZE communicate() class OBJECT WHENEVER ANY OF THE SUBSEQUENT 
    METHODS ARE CALLED '''
def init_obj(fn):
    com = communicate()
    def wrapper(*kargs, **kwargs):
        return fn(com, kargs, kwargs)
    return wrapper

''' FUNCTION TO RECIEVE THE OLDEST UNREAD MESSAGE '''
@init_obj
def getMsg(*args):
    #print(args[0])
    json_obj = None
    while json_obj is None:
        json_obj = args[0].receive()

    sender_id = json_obj['result'][0]['message']['from']['id']
    message_body = json_obj['result'][0]['message']['text']
    chat_id = json_obj['result'][0]['message']['chat']['id']
    update_id = json_obj['result'][0]['update_id']

    return sender_id, message_body, chat_id, update_id

''' FUNCTION TO SEND MESSAGE '''
@init_obj
def sendMsg(*args):
    args[0].send(args[1][0], args[1][1])
    