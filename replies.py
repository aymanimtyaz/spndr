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
    return_dict = {None:open(rep_dir+'transaction_state_zero.txt').read(),
                   -1:open(rep_dir+'transaction_state_zero.txt').read(),
                   0:open(rep_dir+'transaction_state_one.txt').read(),
                   1:open(rep_dir+'transaction_state_two.txt').read(),
                   2:open(rep_dir+'transaction_state_three.txt').read(),
                   3:open(rep_dir+'transaction_state_four.txt').read()}
    return return_dict[transaction_state]

def wrong_input_reply(input_error_code):
    rep_dir = os.getcwd()+'//replies//wrong_input_replies//'
    return_dict = {1:open(rep_dir+'price_should_be_numeric.txt').read(),
                   2:open(rep_dir+'price_zero_or_negative.txt').read(),
                   3:open(rep_dir+'abort_state_reply_y_or_n.txt').read(),
                   4:open(rep_dir+'unreg_sender_wrong_mssg.txt').read(),
                   5:open(rep_dir+'delete_user_wrong_reply.txt').read()}
    return return_dict[input_error_code]

def special_reply(state):
    rep_dir = os.getcwd()+'//replies//special_replies//'
    return_dict = {1:open(rep_dir+'transaction_aborted.txt').read(),
                   2:open(rep_dir+'transaction_not_aborted.txt').read(),
                   3:open(rep_dir+'show_last_10_transactions.txt').read(),
                   4:open(rep_dir+'no_spending_data_yet.txt').read(),
                   5:open(rep_dir+'last_ten_transactions.txt').read(),
                   6:open(rep_dir+'confirm_user_deletion.txt').read(),
                   7:open(rep_dir+'user_deleted.txt').read(),
                   8:open(rep_dir+'user_deletion_aborted.txt').read()}
    return return_dict[state]

def command_reply(command):
    rep_dir = os.getcwd()+'//replies//command_reply//'
    return_dict = {1:open(rep_dir+'!help_no_transaction.txt').read(),
                   2:open(rep_dir+'!help_ongoing_transaction.txt').read(),
                   3:open(rep_dir+'!abort_surety_check.txt').read()}
    return return_dict[command]

def unregistered_sender_reply(state):
    rep_dir = os.getcwd()+'//replies//unregistered_senders//'
    return_dict = {1:open(rep_dir+'brand_new_sender.txt').read(),
                   2:open(rep_dir+'new_sender_yes.txt').read(),
                   3:open(rep_dir+'new_sender_no.txt').read()}
    return return_dict[state]
    

    