import os

class sql_scripts:

    scr_dict={}
    for file in os.listdir(os.path.dirname(__file__)+'/sql_scripts'):
        scr_dict[file[:-4]] = open(os.path.join(os.path.dirname(__file__)+'/sql_scripts', file), 'r').read()