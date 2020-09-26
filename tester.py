import api_caller as ac 
import message_processor as mp



while True:
    sid, msg, cid, uid = ac.getMsg()
    message_to_return = mp.return_message(msg, sid)
    ac.sendMsg(cid, message_to_return)
    

    #print('SENDER ID:', str(sid), ' MESSAGE SENT:', msg, 'CHAT ID:', str(cid), 'UPDATE ID:', str(uid))