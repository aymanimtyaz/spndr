import os

class replies_dicts:

    command_replies = {}
    special_replies = {}
    standard_transaction = {}
    unregistered_senders = {}
    wrong_input_replies = {}

    for file in os.listdir(os.path.dirname(__file__)+'\\replies\\command_reply'):
        command_replies[file[:-4]] = open(os.path.join(os.path.dirname(__file__)+'\\replies\\command_reply', file), 'r').read()

    for file in os.listdir(os.path.dirname(__file__)+'\\replies\\special_replies'):
        special_replies[file[:-4]] = open(os.path.join(os.path.dirname(__file__)+'\\replies\\special_replies', file), 'r').read()

    for file in os.listdir(os.path.dirname(__file__)+'\\replies\\standard_transaction'):
        standard_transaction[file[:-4]] = open(os.path.join(os.path.dirname(__file__)+'\\replies\\standard_transaction', file), 'r').read()

    for file in os.listdir(os.path.dirname(__file__)+'\\replies\\unregistered_senders'):
        unregistered_senders[file[:-4]] = open(os.path.join(os.path.dirname(__file__)+'\\replies\\unregistered_senders', file), 'r').read()
        
    for file in os.listdir(os.path.dirname(__file__)+'\\replies\\wrong_input_replies'):
        wrong_input_replies[file[:-4]] = open(os.path.join(os.path.dirname(__file__)+'\\replies\\wrong_input_replies', file), 'r').read()

