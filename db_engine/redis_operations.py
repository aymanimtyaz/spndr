import redis

try:
    from spndr_tg.db_engine import db_operations as db
except ModuleNotFoundError:
    from db_engine import db_operations as db

red = redis.Redis(decode_responses = True)

def getTransactionState(sender_id):
    key = f'on_tra:{sender_id}'
    transaction_state = red.hget(key, 'transaction_state')
    if transaction_state is None:
        return None
    return int(transaction_state)

def createNewTransaction(sender_id):
    key = f'on_tra:{sender_id}'
    red.hmset(key, {'transaction_state':0})

def initDeleteUser(sender_id):
    key = f'on_tra:{sender_id}'
    red.hmset(key, {'transaction_state':6})

def updateTransaction(sender_id, message, transaction_state):
    key = f'on_tra:{sender_id}'
    if transaction_state == 3:
        completed_transaction = red.hgetall(key)
        deleteTransaction(sender_id)
        completed_transaction['category'] = message
        db.commitTransaction(sender_id, completed_transaction)
    else:
        updation_dict = {0:{'transaction_state':1, 'item':message},
                        1:{'transaction_state':2, 'price':message},
                        2:{'transaction_state':3, 'vendor':message}}
        red.hmset(key, updation_dict[transaction_state])
    
def abortTransaction(sender_id, state, transaction_state = None):
    key = f'on_tra:{sender_id}'
    if state == 'abort':
        red.delete(key)
    elif state == 'skip':
        prev_transaction_state = red.hget(key, 'previous_transaction_state')
        red.hmset(key, {'transaction_state':prev_transaction_state})
        red.hdel(key, 'previous_transaction_state')
    elif state == 'init abort':
        red.hmset(key, {'transaction_state':5, 'previous_transaction_state':transaction_state})
        
def deleteTransaction(sender_id):
    key = f'on_tra:{sender_id}'
    red.delete(key)

def createAccount(sender_id, state, email = None, hashed_password = None):
    key = f'on_tra:{sender_id}'
    if state in range(1, 4):
        red.hmset(key, {'transaction_state':state})
    elif state == 4 or state == 5:
        red.hmset(key, {'transaction_state':state, 'email':email})
    elif state == 'login' or state == 'signup':
        user_info = red.hgetall(key)
        deleteTransaction(sender_id)
        user_info['hashed_password'] = hashed_password
        db.createAccount(sender_id, state = state, user_info = user_info)

def getUserInfo(sender_id, requested_info):
    key = f'on_tra:{sender_id}'
    return red.hget(key, requested_info)