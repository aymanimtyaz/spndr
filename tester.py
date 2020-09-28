import api_caller as ac 
import message_processor as mp



while True:
    sid, msg, cid, uid = ac.getMsg()
    print('MESSAGE SENT:', msg)
    message_to_return = mp.return_message(msg, sid, cid)
    ac.sendMsg(cid, message_to_return)
    

    