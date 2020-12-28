import redis
import json

r = redis.Redis(decode_responses = True)

def get_update():
    json_obj = json.loads(r.brpop("update_queue")[1])
    sender_id = json_obj['message']['from']['id']
    chat_id = json_obj['message']['chat']['id']

    try:
        message_body = json_obj['message']['text']
    except KeyError:
        return sender_id, '!non_text_input', chat_id

    message_body = json_obj['message']['text']
    return sender_id, message_body, chat_id

