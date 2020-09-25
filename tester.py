import api_caller as ac 
import message_processor as mp


while True:
    sid, msg, cid, uid = ac.getMsg()
    #print('SENDER ID:', str(sid), ' MESSAGE SENT:', msg, 'CHAT ID:', str(cid), 'UPDATE ID:', str(uid))
    menu_driver = mp.menu_option(msg)




    
    ac.sendMsg(cid, input())
    

