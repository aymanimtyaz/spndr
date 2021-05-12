# try:
#     from spndr_tg.api_engine import telegrambot_caller as ac
# except ModuleNotFoundError:
#     from api_engine import telegrambot_caller as ac

# try:
#     from spndr_tg.app_engine import app_engine as ae
# except ModuleNotFoundError:
#     from app_engine import app_engine as ae

# try:
#     from spndr_tg.db_engine.db_scripts_loader import sql_scripts
# except ModuleNotFoundError:
#     from db_engine.db_scripts_loader import sql_scripts

# try:
#     from spndr_tg.replies_engine.replies_loader import replies_dicts
# except ModuleNotFoundError:
#     from replies_engine.replies_loader import replies_dicts

try:
    from spndr_tg.api_engine.webhook_update_parser import get_update
except ModuleNotFoundError:
    from api_engine.webhook_update_parser import get_update

# import os

from chatbot_engine import chatbot

# def init_app():
#     sql_scripts.scr_dict

#     replies_dicts.command_replies
#     replies_dicts.special_replies
#     replies_dicts.standard_transaction
#     replies_dicts.unregistered_senders
#     replies_dicts.wrong_input_replies

#     print('Bot initiallized, Process ID:', os.getpid())

def start_event(json_update):
    sid, msg, cid = get_update(json_update)
    # message_to_return = ae.return_message(msg, sid, cid)
    chatbot.execute(uid=sid, input=(msg, cid, sid, ))
    # ac.sendMsg(cid, message_to_return)