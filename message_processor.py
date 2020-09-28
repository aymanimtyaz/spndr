''' This module can be thought of as the heart of the entire program. All the messages that are sent
    to the bot are processed here, giving thought to the context in which that message was sent.

    The module processes the message, does the required database operation and returns the correct contextual 
    reply to the calling function.

    FUNCTIONS IN THIS MODULE

    1. return_message() - This is currently the only function in this module. It carries out the entire 
                          working of this module as explained above. 
                          A lot of the functionality in this function will be removed and separate functions 
                          will be made for those functionalities. This will be done to improve the code's
                          readibility and to improve (if possible) the running of the program.
                          

'''
import os
import database_operations as db
import api_caller as ac

def return_message(message, sender_id, chat_id):
    transaction_state = db.getTransactionState(sender_id)

    if message.startswith('!'):
            return process_command(message, transaction_state, sender_id)

    if transaction_state is None:
        if message == 'new':
            db.createNewTransaction(sender_id)
            return open(os.getcwd()+'//replies//standard_transaction//transaction_state_zero.txt').read()

    elif transaction_state in range(0, 4):

        if transaction_state == 1:
            try:
                float(message)
            except ValueError:
                return open(os.getcwd()+'//replies//standard_transaction//price_should_be_numeric.txt').read()
            if float(message) <= 0:
                return open(os.getcwd()+'//replies//standard_transaction//price_zero_or_negative.txt').read()

        db.updateTransaction(sender_id, message, transaction_state)

        return standard_reply(transaction_state)
    
    elif transaction_state == 5:
        if message == 'y' or message == 'n':
            db.abortTransaction(message, sender_id, transaction_state)
            if message == 'y':
                return open(os.getcwd()+'//replies//special_replies//transaction_aborted.txt').read()    
            ac.sendMsg(chat_id, open(os.getcwd()+'//replies//special_replies//transaction_not_aborted.txt').read())
            return standard_reply(transaction_state=(db.getTransactionState(sender_id)-1))        
        else:
            return open(os.getcwd()+'//replies//wrong_input_replies//abort_state_reply_y_or_n.txt').read()

def process_command(message, transaction_state, sender_id):
    if transaction_state is None:
        if message == '!help':
            return open(os.getcwd()+'//replies//command_reply//!help_no_transaction.txt').read()
    
    elif transaction_state in range(0, 4):
        if message == '!help':
            return open(os.getcwd()+'//replies//command_reply//!help_ongoing_transaction.txt').read()
        if message == '!abort':
            db.abortTransaction(message, sender_id, transaction_state)
            return open(os.getcwd()+'//replies//command_reply//!abort_surety_check.txt').read()

def standard_reply(transaction_state):
    if transaction_state == 0:
        return open(os.getcwd()+'//replies//standard_transaction//transaction_state_one.txt').read()
    if transaction_state == 1:   
        return open(os.getcwd()+'//replies//standard_transaction//transaction_state_two.txt').read()
    if transaction_state == 2:
        return open(os.getcwd()+'//replies//standard_transaction//transaction_state_three.txt').read()
    if transaction_state == 3:
        return open(os.getcwd()+'//replies//standard_transaction//transaction_state_four.txt').read()


        

            

        

        
        

























    