''' 2. process_command() - This function is used to process command messages, commands that start with an
                            exclamation mark are considered to be command messages. The command messages are
                            processed taking the context of the conversation as an argument (transaction_state)
                            For more information on transaction_states, please scroll below to its corresponding
                            section.
'''


try:
    from spndr_tg.api_engine import telegrambot_caller as ac
except ModuleNotFoundError:
    from api_engine import telegrambot_caller as ac

try:
    from spndr_tg.db_engine import db_operations as db
except ModuleNotFoundError:
    from db_engine import db_operations as db

try:
    from spndr_tg.replies_engine import replies as r
except ModuleNotFoundError:
    from replies_engine import replies as r

def process_command(message, transaction_state, sender_id, chat_id):
    if transaction_state is None:
        if message.lower() == '!help':
            return r.command_reply(command = 1)
        
    elif transaction_state in range(0, 4):
        if message.lower() == '!non_text_input':
            ac.sendMsg(chat_id, r.wrong_input_reply(input_error_code = 10))
            return r.standard_reply(transaction_state-1)
        if message.lower() == '!help':
            return r.command_reply(command = 2)
        if message.lower() == '!abort':
            db.abortTransaction(message, sender_id, transaction_state)
            return r.command_reply(command = 3)
        else:
            ac.sendMsg(chat_id, r.command_reply(command = 2))
            return r.standard_reply(transaction_state = transaction_state-1)
    
    elif transaction_state == 5:
        return r.wrong_input_reply(3)