''' This module calls the cnnct() and dscnnct() functions to get cursors with which it can interface with our Postgres
    database in the backend. The sql scripts it executes using the cursors are stored in the sql_scripts dictionary which
    is imported from the db_scripts_loader module.


    FUNCTIONS IN THIS MODULE

    1. getTransactionState() - Retrieves the transaction state of the sender of the message currently being processed.
                               If the sender doesn't have an ongoing transaction, it will return None.

    2. createNewTransaction() - If the sender has sent 'new' when their transaction state is none. A new transaction
                                will be initiated for them, and their transaction state will be increased to 0.

    3. updateTransaction() - Increments the transaction state and commits the newly provided date from the user to the 
                             current_transaction database.
                             It also calls commitTransaction() when a transaction has been completed. That is, when
                             the transaction state equals 4.

    4. commitTransaction() - Once a transaction has been completed. The transaction information is taken from the 
                             current_transaction database and committed to the transactions database.

    5. abortTransaction() - Aborts an ongoing transaction when the user gives the !abort command.

    6. checkCreds() - This function checks whether a particular sender is registered with the service or not.

    7. createAccount() - This function registers a sender if they agree to join spndr.

    8. deleteNewSender() - This function removes an unregistered sender if they don't want to sign up for spndr.

    9. lastTenTransactions() - This function retrieves upto 10 of the latest transactions made by a specific user.

    10. deleteUser() - This function removes a user from the database, essentially deleting the user's account.
'''

from db_interface import cnnct, dscnnct
from db_scripts_loader import sql_scripts as ss

def getTransactionState(sender_id):
    pool, con, curs = cnnct()
    curs.execute(ss.scr_dict['get_transaction_state'], {"sender_id":sender_id})
    query_result = curs.fetchone()
    dscnnct(pool, con, curs)
    if query_result is None:
        return None
    transaction_state = query_result[0]
    return transaction_state

def createNewTransaction(sender_id):
    pool, con, curs = cnnct()
    curs.execute(ss.scr_dict['create_new_transaction'], {"sender_id":sender_id})
    dscnnct(pool, con, curs)

def updateTransaction(sender_id, message, transaction_state):
    updation_dict = {0:[ss.scr_dict['add_product_service'], 
                        {"prod_serv":message, "sender_id":sender_id}],

                     1:[ss.scr_dict['add_price'],
                        {"price":message, "sender_id":sender_id}],

                     2:[ss.scr_dict['add_vendor'],
                        {"vendor":message, "sender_id":sender_id}],

                     3:[ss.scr_dict['add_category'],
                        {"category":message, "sender_id":sender_id}]}
    
    pool, con, curs = cnnct()
    curs.execute(updation_dict[transaction_state][0], updation_dict[transaction_state][1])
    dscnnct(pool, con, curs)
    
    transaction_state = getTransactionState(sender_id)
    if transaction_state == 4:
        commitTransaction(sender_id)
    
def commitTransaction(sender_id):
    pool, con, curs = cnnct()
    curs.execute(ss.scr_dict['commit_transaction'], {"sender_id":sender_id})
    curs.execute(ss.scr_dict['delete_completed_transaction'], {"sender_id":sender_id})
    dscnnct(pool, con, curs)

def abortTransaction(message, sender_id, transaction_state):
    pool, con, curs = cnnct()
    if message.lower() == '!abort':
        curs.execute(ss.scr_dict['init_abort_transaction'], 
                    {"previous_transaction_state":transaction_state, "sender_id":sender_id})
    elif transaction_state == 5:
        if message == 'y':
            curs.execute(ss.scr_dict['confirm_abort_transaction'], {"sender_id":sender_id})
        elif message == 'n':
            curs.execute(ss.scr_dict['stop_abort_transaction'], {"sender_id":sender_id})
    dscnnct(pool, con, curs)

def checkCreds(sender_id):
    pool, con, curs = cnnct()
    curs.execute(ss.scr_dict['check_creds'], {"sender_id":sender_id})
    creds_exist = curs.fetchone()[0]
    dscnnct(pool, con, curs)
    if creds_exist:
        return True
    return False

def createAccount(sender_id):
    pool, con, curs = cnnct()
    curs.execute(ss.scr_dict['create_account'], {"sender_id":sender_id})
    dscnnct(pool, con, curs)
    
def deleteNewSender(sender_id):
    pool, con, curs = cnnct()
    curs.execute(ss.scr_dict['delete_new_sender'], {"sender_id":sender_id})
    dscnnct(pool, con, curs)

def lastTenTransactions(sender_id):
    pool, con, curs = cnnct()
    curs.execute(ss.scr_dict['get_last_ten_transactions'], {"sender_id":sender_id})
    spending_data = curs.fetchmany(10)
    dscnnct(pool, con, curs)
    return spending_data
    
def deleteUser(sender_id, state):
    deletion_dict = {1:ss.scr_dict['init_user_deletion'],
                     2:ss.scr_dict['delete_user'],
                     3:ss.scr_dict['abort_user_deletion']}

    pool, con, curs = cnnct()
    curs.execute(deletion_dict[state], {"sender_id":sender_id})
    dscnnct(pool, con, curs)