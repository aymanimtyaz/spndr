import api_caller as ac 


while True:
    sid, msg, cid, uid = ac.getMsg()
    #print('SENDER ID:', str(sid), ' MESSAGE SENT:', msg, 'CHAT ID:', str(cid), 'UPDATE ID:', str(uid))
    ac.sendMsg(cid, input())
    menu_driver = 
