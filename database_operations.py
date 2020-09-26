import psycopg2 as pg2 
import os

def getTransactionState(sender_id):
    get_transaction_state_script = open(os.getcwd()+'//sql_scripts//get_transaction_state.sql').read()
    con = pg2.connect(database='spndr', user='postgres', password='password')
    curs = con.cursor()
    curs.execute(get_transaction_state_script, {"sender_id":sender_id})
    query_result = curs.fetchone()
    if query_result is None:
        con.commit(); curs.close(); con.close()
        return None
    transaction_state = query_result[0]
    con.commit(); curs.close(); con.close()
    return transaction_state


def createNewTransaction(sender_id):
    create_new_transaction_script = open(os.getcwd()+'//sql_scripts//create_new_transaction.sql').read()
    con = pg2.connect(database='spndr', user='postgres', password='password')
    curs = con.cursor()
    curs.execute(create_new_transaction_script, {"sender_id":sender_id})
    con.commit(); curs.close(), con.close()

def updateTransaction(sender_id, message, previous_transaction_state):
    con = pg2.connect(database='spndr', user='postgres', password='password')
    curs = con.cursor()

    if previous_transaction_state == 0:
        add_product_service_script = open(os.getcwd()+'//sql_scripts//add_product_service.sql').read()
        curs.execute(add_product_service_script, {"prod_serv":message, "sender_id":sender_id})
        
    if previous_transaction_state == 1:
        add_price_script = open(os.getcwd()+'//sql_scripts//add_price.sql').read()
        curs.execute(add_price_script, {"price":float(message), "sender_id":sender_id})

    if previous_transaction_state == 2:
        add_vendor_script = open(os.getcwd()+'//sql_scripts//add_vendor.sql').read()
        curs.execute(add_vendor_script, {"vendor":message, "sender_id":sender_id})

    if previous_transaction_state == 3:
        add_category_script = open(os.getcwd()+'//sql_scripts//add_category.sql').read()
        curs.execute(add_category_script, {"category":message, "sender_id":sender_id})

    
    con.commit(); curs.close(); con.close()

    transaction_state = getTransactionState(sender_id)
    if transaction_state == 4:
        commitTransaction(sender_id)

def commitTransaction(sender_id):
    con = pg2.connect(database='spndr', user='postgres', password='password')
    cur = con.cursor()

    commit_transaction_script = open(os.getcwd()+'//sql_scripts//commit_transaction.sql').read()
    delete_completed_transaction_script = open(os.getcwd()+'//sql_scripts//delete_completed_transaction.sql').read()
    cur.execute(commit_transaction_script, {"sender_id":sender_id})
    cur.execute(delete_completed_transaction_script, {"sender_id":sender_id})

    con.commit(); cur.close(); con.close()







    


