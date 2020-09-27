''' This module is the can be thought of as the hearf of the entire program. All the messages that are sent
    to the bot are processed here, giving thought to the context in which that message was sent.

    The module processes the message, does the required database operation and returns the correct contextual 
    reply to the calling function.

    FUNCTIONS IN THIS MODULE

    1. return_message() - This is currently the only function in this module. It carries out the entire 
                          working of this module as explained above. 
                          A lot of the functionality in this module will be removed and separate functions 
                          will be made for those functionalities. This will be done to improve the code's
                          readibility and to improve the running of the program (if possible)

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
        if transaction_state == 1:
            try:
                float(message)
            except ValueError:
                return open(os.getcwd()+'//replies//standard_transaction//price_should_be_numeric.txt').read()
            if float(message) <= 0:
                return open(os.getcwd()+'//replies//standard_transaction//price_zero_or_negative.txt').read()

        db.updateTransaction(sender_id, message, transaction_state)

        if transaction_state == 0:
            return open(os.getcwd()+'//replies//standard_transaction//transaction_state_one.txt').read()
        if transaction_state == 1:   
            return open(os.getcwd()+'//replies//standard_transaction//transaction_state_two.txt').read()
        if transaction_state == 2:
            return open(os.getcwd()+'//replies//standard_transaction//transaction_state_three.txt').read()
        if transaction_state == 3:
            return open(os.getcwd()+'//replies//standard_transaction//transaction_state_four.txt').read()

        

        

            

        

        
        

























    