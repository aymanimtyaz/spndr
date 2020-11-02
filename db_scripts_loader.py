import os

class sql_scripts:

    scr_dict={}
    for file in os.listdir(os.getcwd()+'\\sql_scripts'):
        scr_dict[file[:-4]] = open(os.path.join(os.getcwd()+'\\sql_scripts', file), 'r').read()









