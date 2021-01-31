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

try:
    from spndr_tg.db_engine import redis_operations as red
except ModuleNotFoundError:
    from db_engine import redis_operations as red

def process_command(message, transaction_state, sender_id, chat_id):
    if transaction_state is None:
        if message.lower() == '/help':
            return r.command_reply(command = 1)

        if message.lower() == '/new':
            red.createNewTransaction(sender_id)
            return r.standard_reply(transaction_state)
        
        if message.lower() == '/show':
            return generate_show_reply(sender_id, chat_id)
        
        if message.lower() == '/delete':
            red.initDeleteUser(sender_id)
            return r.special_reply(state = 6)
    
    elif transaction_state in range(0, 4):
        if message.lower() == '/non_text_input':
            ac.sendMsg(chat_id, r.wrong_input_reply(input_error_code = 10))
            return r.standard_reply(transaction_state-1)
        if message.lower() == '/help':
            return r.command_reply(command = 2)
        if message.lower() == '/abort':
            red.abortTransaction(sender_id, state = 'init abort', transaction_state = transaction_state)
            return r.command_reply(command = 3)
        else:
            ac.sendMsg(chat_id, r.command_reply(command = 2))
            return r.standard_reply(transaction_state = transaction_state-1)

    elif transaction_state == 5:
        return r.wrong_input_reply(3)

def generate_show_reply(sender_id, chat_id):
    spending_data = db.lastTenTransactions(sender_id)
    if len(spending_data) == 0:
        return r.special_reply(state = 4)
    ac.sendMsg(chat_id, r.special_reply(state = 3))
    ret_str = ''; i=1
    for row in spending_data:
        article = 'An' if row[0].lower()[0] in ['a', 'e', 'i', 'o', 'u'] else 'A'
        if row[0].lower().endswith('s'):
            article = '' 
        ret_str+=str(i)+str(r.special_reply(state = 5)).format(
        article, row[0], row[1], row[2], row[3])+'\n\n'
        i+=1
    return ret_str