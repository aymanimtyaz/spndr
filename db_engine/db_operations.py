''' This module calls the cnnct() and dscnnct() functions to get cursors with which it can interface with our Postgres
    database in the backend. The sql scripts it executes using the cursors are stored in the sql_scripts dictionary which
    is imported from the db_scripts_loader module.


    FUNCTIONS IN THIS MODULE

    1. commitTransaction() - Once a transaction has been completed. The transaction information is taken from the 
                             Redis database and committed to the transactions database.

    2. checkCreds() - This function checks whether a particular sender is registered with the service or not.

    3. createAccount() - This function registers a user's telegram account if they agree to join spndr.

    4. lastTenTransactions() - This function retrieves upto 10 of the latest transactions made by a specific user.

    5. deleteUser() - This function unlinks a user's telegram account from their spndr account.

    6. checkIfEmailInUse() - This function checks if the email entered by a user who wishes to signup is already in use or not.

    7. retrievePassword() - This function retrieves the password of a user who wished to link their telegram account to an existing spndr account.

    8. getUserID() - This function gets the user ID of a user from their telegram account.

    9. add_new_transaction_ws() - This function adds a users transaction to the database, when the user logs a transaction through the website.

    10. get_last_ten_transactions_ws() - This function get the 10 latest transactions of a user when they login to spndr on the website.
'''
# try:
#     from spndr_tg.db_engine.db_interface import cnnct, dscnnct
# except ModuleNotFoundError:
#     from db_engine.db_interface import cnnct, dscnnct

try:
    from spndr_tg.db_engine.db_interface import dbc
except ModuleNotFoundError:
    from db_engine.db_interface import dbc

try:    
    from spndr_tg.db_engine.db_scripts_loader import sql_scripts as ss
except ModuleNotFoundError:
    from db_engine.db_scripts_loader import sql_scripts as ss

def commitTransaction(sender_id, completed_transaction):
    con, curs = dbc.cnnct()
    curs.execute(ss.scr_dict['commit_transaction_2'], {"sender_id":sender_id, "item":completed_transaction['item'],
                                                       "price":completed_transaction['price'], "vendor":completed_transaction['vendor'],
                                                        "category":completed_transaction['category']})
    dbc.dscnnct(con, curs)
    
def checkCreds(sender_id):
    con, curs = dbc.cnnct()
    curs.execute(ss.scr_dict['check_creds'], {"sender_id":sender_id})
    creds_exist = curs.fetchone()[0]
    dbc.dscnnct(con, curs)
    return creds_exist

def createAccount(sender_id, state, user_info):
    creation_dict = {'login':ss.scr_dict['create_account_login'],
                     'signup':ss.scr_dict['create_account_signup']}
    con, curs = dbc.cnnct()
    curs.execute(creation_dict[state], {"sender_id":sender_id, "email":user_info['email'], "hashed_password":user_info['hashed_password']})
    dbc.dscnnct(con, curs)

def lastTenTransactions(sender_id):
    user_id = getUserInfo(sender_id, 'id')
    con, curs = dbc.cnnct()
    curs.execute(ss.scr_dict['get_last_ten_transactions'], {"user_id":user_id})
    spending_data = curs.fetchmany(10)
    dbc.dscnnct(con, curs)
    return spending_data
    
def deleteUser(sender_id):
    con, curs = dbc.cnnct()
    curs.execute(ss.scr_dict['delete_user'], {"sender_id":sender_id})
    dbc.dscnnct(con, curs)

def checkIfEmailInUse(email):
    con, curs = dbc.cnnct()
    curs.execute(ss.scr_dict['check_if_email_in_use'], {"email":email})
    email_exists = curs.fetchone()[0]
    dbc.dscnnct(con, curs)
    return email_exists

def retrievePassword(email):
    con, curs = dbc.cnnct()
    curs.execute(ss.scr_dict['retrieve_password'], {"email":email})
    try:
        hashed_password = curs.fetchone()[0]
    except TypeError:
        hashed_password = None
    dbc.dscnnct(con, curs)
    return hashed_password

def getUserInfo(sender_id, requested_info):
    request_dict = {'id':ss.scr_dict['get_user_id']}
    con, curs = dbc.cnnct()
    curs.execute(request_dict[requested_info], {"sender_id":sender_id})
    requested_info = curs.fetchone()[0]
    dbc.dscnnct(con, curs)
    return requested_info   

#### REDACTED ####
# def getUserID(sender_id):
#     pool, con, curs = cnnct()
#     curs.execute(ss.scr_dict['get_user_id'], {"sender_id":sender_id})
#     user_id = curs.fetchone()[0]
#     dscnnct(pool, con, curs)
#     return user_id

'''################################################################################################################################'''

def add_new_transaction_ws(id, item, price, vendor, category):
    con, curs = dbc.cnnct()
    curs.execute(ss.scr_dict['add_new_transaction_ws'], {"id":id, "item":item, "price":price, "vendor":vendor, "category":category})
    dbc.dscnnct(con, curs)

def get_last_ten_transactions_ws(id):
    con, curs = dbc.cnnct()
    curs.execute(ss.scr_dict['get_last_ten_transactions_ws'], {"id":id})
    spending_data = curs.fetchmany(10)
    dbc.dscnnct(con, curs)
    return spending_data

