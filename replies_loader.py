import os

class replies_dicts:

    command_replies = {}
    special_replies = {}
    standard_transaction = {}
    unregistered_senders = {}
    wrong_input_replies = {}

    for file in os.listdir(os.getcwd()+'\\replies\\command_reply'):
        command_replies[file[:-4]] = open(os.path.join(os.getcwd()+'\\replies\\command_reply', file)).read()

    for file in os.listdir(os.getcwd()+'\\replies\\special_replies'):
        special_replies[file[:-4]] = open(os.path.join(os.getcwd()+'\\replies\\special_replies', file)).read()

    for file in os.listdir(os.getcwd()+'\\replies\\standard_transaction'):
        standard_transaction[file[:-4]] = open(os.path.join(os.getcwd()+'\\replies\\standard_transaction', file)).read()

    for file in os.listdir(os.getcwd()+'\\replies\\unregistered_senders'):
        unregistered_senders[file[:-4]] = open(os.path.join(os.getcwd()+'\\replies\\unregistered_senders', file)).read()
        
    for file in os.listdir(os.getcwd()+'\\replies\\wrong_input_replies'):
        wrong_input_replies[file[:-4]] = open(os.path.join(os.getcwd()+'\\replies\\wrong_input_replies', file)).read()

