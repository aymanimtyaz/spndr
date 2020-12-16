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

def process_reg_sender(message, sender_id, chat_id, transaction_state):
    if transaction_state is None:

        if message.lower() == 'new':
            red.createNewTransaction(sender_id)
            return r.standard_reply(transaction_state)
        
        if message.lower() == 'show':
            return generate_show_reply(sender_id, chat_id)
        
        if message.lower() == 'delete':
            red.initDeleteUser(sender_id)
            return r.special_reply(state = 6)

    elif transaction_state in range(0,4):
         
        if transaction_state == 1:
            try:
                float(message)
            except ValueError:
                return r.wrong_input_reply(input_error_code = 1)
            if float(message) <= 0:
                return r.wrong_input_reply(input_error_code = 2)
            message = float(message)

        red.updateTransaction(sender_id, message, transaction_state)
        return r.standard_reply(transaction_state)

    elif transaction_state == 5:

        if message == 'y' or message == 'n':
            if message == 'y':
                red.abortTransaction(sender_id, state = 'abort')
                return r.special_reply(state = 1)
            red.abortTransaction(sender_id, state = 'skip')
            ac.sendMsg(chat_id, r.special_reply(state = 2))
            return r.standard_reply(transaction_state=(red.getTransactionState(sender_id)-1))
        return r.wrong_input_reply(input_error_code = 3)

    elif transaction_state == 6:

        if message == 'y' or message == 'n':
            red.deleteTransaction(sender_id)
            if message == 'y':
                db.deleteUser(sender_id)
                return r.special_reply(state = 7)
            return r.special_reply(state = 8)
        return r.wrong_input_reply(input_error_code = 5)
            
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