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
try:
    from spndr_tg.replies_loader import replies_dicts as rd
except ModuleNotFoundError:
    from replies_loader import replies_dicts as rd

def standard_reply(transaction_state):
    return_dict = {None:rd.standard_transaction['transaction_state_zero'],
                   -1:rd.standard_transaction['transaction_state_zero'],
                   0:rd.standard_transaction['transaction_state_one'],
                   1:rd.standard_transaction['transaction_state_two'],
                   2:rd.standard_transaction['transaction_state_three'],
                   3:rd.standard_transaction['transaction_state_four']}
    return return_dict[transaction_state]

def wrong_input_reply(input_error_code):
    return_dict = {1:rd.wrong_input_replies['price_should_be_numeric'],
                   2:rd.wrong_input_replies['price_zero_or_negative'],
                   3:rd.wrong_input_replies['abort_state_reply_y_or_n'],
                   4:rd.wrong_input_replies['unreg_sender_wrong_input_0'],
                   5:rd.wrong_input_replies['delete_user_wrong_reply'],
                   6:rd.wrong_input_replies['unreg_sender_wrong_input_1'],
                   7:rd.wrong_input_replies['unreg_sender_wrong_email'],
                   8:rd.wrong_input_replies['unreg_sender_existing_email'],
                   9:rd.wrong_input_replies['unreg_sender_login_wrong_password'],
                   10:rd.wrong_input_replies['non_text_input']}
    return return_dict[input_error_code]

def special_reply(state):
    return_dict = {1:rd.special_replies['transaction_aborted'],
                   2:rd.special_replies['transaction_not_aborted'],
                   3:rd.special_replies['show_last_10_transactions'],
                   4:rd.special_replies['no_spending_data_yet'],
                   5:rd.special_replies['last_ten_transactions'],
                   6:rd.special_replies['confirm_user_deletion'],
                   7:rd.special_replies['user_deleted'],
                   8:rd.special_replies['user_deletion_aborted']}
    return return_dict[state]

def command_reply(command):
    return_dict = {1:rd.command_replies['!help_no_transaction'],
                   2:rd.command_replies['!help_ongoing_transaction'],
                   3:rd.command_replies['!abort_surety_check']}
    return return_dict[command]

def unregistered_sender_reply(state):
    return_dict = {1:rd.unregistered_senders['brand_new_sender'],
                   2:rd.unregistered_senders['new_sender_yes'],
                   3:rd.unregistered_senders['new_sender_no'],
                   4:rd.unregistered_senders['new_sender_email'],
                   5:rd.unregistered_senders['new_sender_login_password'],
                   6:rd.unregistered_senders['new_sender_signup_password'],
                   7:rd.unregistered_senders['success_login_new_sender'],
                   8:rd.unregistered_senders['success_signup_new_sender']}
    return return_dict[state]
    

    