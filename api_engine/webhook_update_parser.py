import json

def get_update(json_update):
    sender_id = json_update['message']['from']['id']
    chat_id = json_update['message']['chat']['id']

    try:
        message_body = json_update['message']['text']
    except KeyError:
        return sender_id, '!non_text_input', chat_id

    message_body = json_update['message']['text']
    return sender_id, message_body, chat_id

