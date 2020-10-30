import api_caller as ac 
import message_processor as mp
from sql_scripts_loader import sql_scripts
from replies_loader import replies_dicts

def init_app():
    sql_scripts.scr_dict

    replies_dicts.command_replies
    replies_dicts.special_replies
    replies_dicts.standard_transaction
    replies_dicts.unregistered_senders
    replies_dicts.wrong_input_replies

def main():
    while True:
        sid, msg, cid, uid = ac.getMsg()
        print('MESSAGE SENT:', msg)
        message_to_return = mp.return_message(msg, sid, cid)
        ac.sendMsg(cid, message_to_return)

if __name__ == '__main__':
    init_app()
    main()
    

    