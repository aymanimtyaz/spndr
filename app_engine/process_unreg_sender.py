''' 3. process_unreg_sender() - This function is called when db_operations.credCheck() returns False for
                                    a particular sender_id, which means that the sender isn't registered with the 
                                    service.
'''



from flask_bcrypt import generate_password_hash, check_password_hash
import re

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

def process_unreg_sender(message, sender_id, transaction_state):
    if transaction_state is None:
        red.createNewTransaction(sender_id)
        return r.unregistered_sender_reply(state = 1)

    if transaction_state == 0:
        if message.lower() == 'y' or message.lower() == 'n':
            if message.lower() == 'n':
                red.deleteTransaction(sender_id)
                return r.unregistered_sender_reply(state = 3)
            red.createAccount(sender_id, state = 1)
            return r.unregistered_sender_reply(state = 2)
        
        return r.wrong_input_reply(input_error_code = 4)

    if message == '/quit':
        red.deleteTransaction(sender_id)
        return r.unregistered_sender_reply(state = 3)

    if transaction_state == 1:
        if message == '1' or message == '2':
            if message == '1':
                red.createAccount(sender_id, state = 2)
                return r.unregistered_sender_reply(state = 4)
            red.createAccount(sender_id, state = 3)
            return r.unregistered_sender_reply(state = 4)

        return r.wrong_input_reply(input_error_code = 6)

    if transaction_state == 2 or transaction_state == 3:
        if not email_is_valid(message):
            return r.wrong_input_reply(input_error_code = 7)
        if transaction_state == 2:
            if db.checkIfEmailInUse(email = message):
                red.createAccount(sender_id, state = 4, email = message)
                return r.unregistered_sender_reply(state = 5)
            return r.wrong_input_reply(input_error_code = 11)
        if not db.checkIfEmailInUse(email = message):
            red.createAccount(sender_id, state = 5, email = message)
            return r.unregistered_sender_reply(state = 6)
        return r.wrong_input_reply(input_error_code = 8)

    if transaction_state == 4 or transaction_state == 5:
        if transaction_state == 4:
            email = red.getUserInfo(sender_id, requested_info = 'email')
            hashed_password = db.retrievePassword(email)
            if hashed_password is None:
                return r.wrong_input_reply(input_error_code = 9)
            if check_password_hash(hashed_password, message):
                red.createAccount(sender_id, state = 'login')
                return r.unregistered_sender_reply(state = 7)
            return r.wrong_input_reply(input_error_code = 9)
        hashed_password = generate_password_hash(message).decode('utf-8')
        red.createAccount(sender_id, state = 'signup', hashed_password = hashed_password)
        return r.unregistered_sender_reply(state = 8)

def email_is_valid(message):
    email_regex = r'^[a-zA-Z0-9]+[a-zA-Z0-9.-_]*@[a-zA-Z0-9-]+[.][a-z0-9]{2,3}'
    regex_match = re.search(email_regex, message)
    if regex_match == None:
        return False
    elif re.search(email_regex, message).group() == message:
        return True
    return False