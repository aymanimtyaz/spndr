''' TRANSACTION STATES:
    None - No transaction is currently ongoing for the current sender
    0 -
    '''



import os
import database_operations as db

def return_message(message, sender_id):
    transaction_state = db.getTransactionState(sender_id)

    if transaction_state is None:
        if message == 'new':
            db.createNewTransaction(sender_id)
            return open(os.getcwd()+'//replies//standard_transaction//transaction_state_zero.txt').read()

    else:
        db.updateTransaction(sender_id, message, transaction_state)
        if transaction_state == 0:
            return open(os.getcwd()+'//replies//standard_transaction//transaction_state_one.txt').read()
        if transaction_state == 1:
            return open(os.getcwd()+'//replies//standard_transaction//transaction_state_two.txt').read()
        if transaction_state == 2:
            return open(os.getcwd()+'//replies//standard_transaction//transaction_state_three.txt').read()
        if transaction_state == 3:
            return open(os.getcwd()+'//replies//standard_transaction//transaction_state_four.txt').read()

        

            

        

        
        

























    