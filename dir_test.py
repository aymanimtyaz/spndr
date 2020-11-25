import os
from os import path

def cwd():
    print("This is os.getcwd() in dir_test: ")
    print(os.getcwd())

def absp():
    print("This is os.path.dirname(__file__) in dir_test: ")
    print(os.path.dirname(__file__))