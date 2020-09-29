''' This module opens the text files containing the replies of the bot.

    FUNCTIONS IN THIS MODULE
    
    1. standard_reply() - This function returns the replies made by the bot when a transaction is going on.

    2. wrong_input_reply() - This function returns the replies made by the bot when the sender has entered an input
                             /message that is not valid/actionable in the current context of the conversation.

    3. special_reply() - This function returns the replies made by the bot in special circumstances. For now,
                         the replies that this function returns have arbitrarily been placed in it as they didn't
                         fit in any of the other reply functions. Once their 'fit' has been decided, they will be 
                         moved.

    4. command_reply() - This function returns the replies made by the bot when a command message has been sent to 
                         it. This function is called from process_command() function.
    
    5. unregistered_sender_reply() - This function return the replies made by the bot when a new/unregistered sender
                                     sends a message to the bot.
'''

import os

def standard_reply(transaction_state):
    rep_dir = os.getcwd()+'//replies//standard_transaction//'
    if transaction_state is None or transaction_state == -1:
        return open(rep_dir+'transaction_state_zero.txt').read()
    if transaction_state == 0:
        return open(rep_dir+'transaction_state_one.txt').read()
    if transaction_state == 1:   
        return open(rep_dir+'transaction_state_two.txt').read()
    if transaction_state == 2:
        return open(rep_dir+'transaction_state_three.txt').read()
    if transaction_state == 3:
        return open(rep_dir+'transaction_state_four.txt').read()

def wrong_input_reply(input_error_code):
    rep_dir = os.getcwd()+'//replies//wrong_input_replies//'
    if input_error_code == 1:
        return open(rep_dir+'price_should_be_numeric.txt').read()
    if input_error_code == 2:
        return open(rep_dir+'price_zero_or_negative.txt').read()
    if input_error_code == 3:
        return open(rep_dir+'abort_state_reply_y_or_n.txt').read()
    if input_error_code == 4:
        return open(rep_dir+'unreg_sender_wrong_mssg.txt').read()

def special_reply(state):
    rep_dir = os.getcwd()+'//replies//special_replies//'
    if state == 1:
        return open(rep_dir+'transaction_aborted.txt').read()
    if state == 2:
        return open(rep_dir+'transaction_not_aborted.txt').read()

def command_reply(command):
    rep_dir = os.getcwd()+'//replies//command_reply//'
    if command == 1:
        return open(rep_dir+'!help_no_transaction.txt').read()
    if command == 2:
        return open(rep_dir+'!help_ongoing_transaction.txt').read()
    if command == 3:
        return open(rep_dir+'!abort_surety_check.txt').read()

def unregistered_sender_reply(state):
    rep_dir = os.getcwd()+'//replies//unregistered_senders//'
    if state == 1:
        return open(rep_dir+'brand_new_sender.txt').read()
    if state == 2:
        return open(rep_dir+'new_sender_yes.txt').read()
    if state == 3:
        return open(rep_dir+'new_sender_no.txt').read()
    

    