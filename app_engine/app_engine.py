''' This module can be thought of as the heart of the entire program. All the messages that are sent
    to the bot are processed here, giving thought to the context in which the message was sent.

    The module processes the message, does the required database operation and returns the correct contextual 
    reply to the calling function.

    FUNCTIONS IN THIS MODULE

        1. return_message() - This function is the heart of the module. The messages sent to the bot are first sent
                            here to be processed. 

    TRANSACTION STATES
    Transaction states are a property of each message and sender pair. They describe the context in which the sender has 
    sent the message. The transaction state is needed for the bot to give the correct contextual reply to the sender. It
    lets the bot know the context in which a user's message was sent.

    Transaction states are only needed when a line of conversation between the bot and the sender spans more than one
    message and reply. If one message and reply is enough to start and end the conversation between the bot and the sender,
    transaction states won't be used.

    Currently, the transaction states are:

    WHEN db_operations.checkCreds() RETURNS True (SENDER IS REGISTERED WITH THE SERVICE)

        None - This is the default state for all senders who don't have an ongoing transaction. All conversations between the 
                bot and the sender will start from this state.
        
        0 - This is the state when the sender has initiated a new transaction. At this stage, the sender has to enter the item
            or service that they have purchased.
            
        1 - This is the state after the item has been entered by the sender. At this stage, the sender has to enter the price
            paid for the above stated purchase.

        2 - This is the state after the price of the purchase has been entered by the sender, the sender has to enter the 
            name of the seller of the above purchase.
            
        3 - This is the state after the seller of the purchase has been entered by the sender, ther sender has to enter the
            category that they would like to put this purchase in.
        
        4 - This is the state after the category of the purchase has been entered by the sender. At this stage, all the 
            necessary information regarding a purchase has been entered by the sender, and can now be committed to the 
            main transactions database.

        5 - This is the state after and !abort command has been entered by the sender when they have an ongoing transaction.
            When this stage is entered, a confirmatory check is made to the sender to confirm the abortion of the current
            transaction.

        6 - This is the state after a user has initiated account deletion. At this stage, a confirmatory check is sent to 
            the user to confirm if they really want to delete their account.

    The transaction states for when WHEN db_operations.checkCreds() RETURNS False (SENDER IS NOT REGISTERED WITH THE SERVICE) are
    different, please look at the documentation in app_engine/process_unreg_sender.py   
'''

try:
    from spndr_tg.db_engine import db_operations as db
except ModuleNotFoundError:
    from db_engine import db_operations as db

try:
    from spndr_tg.api_engine import telegrambot_caller as ac
except ModuleNotFoundError:
    from api_engine import telegrambot_caller as ac

try:
    from spndr_tg.replies_engine import replies as r
except ModuleNotFoundError:
    from replies_engine import replies as r

try:
    from spndr_tg.app_engine.process_unreg_sender import process_unreg_sender
except:
    from app_engine.process_unreg_sender import process_unreg_sender

try:
    from spndr_tg.app_engine.process_command import process_command
except:
    from app_engine.process_command import process_command

try:
    from spndr_tg.app_engine.process_reg_sender import process_reg_sender
except:
    from app_engine.process_reg_sender import process_reg_sender


def return_message(message, sender_id, chat_id):
    transaction_state = db.getTransactionState(sender_id)
    cred_state = db.checkCreds(sender_id)
    print(cred_state)

    if cred_state is False:
        return process_unreg_sender(message, sender_id, transaction_state)

    if message.startswith('!'):
        return process_command(message, transaction_state, sender_id, chat_id)

    return process_reg_sender(message, sender_id, chat_id, transaction_state)
