from flask import Flask, request
import json

try:
    from spndr_tg.main_webhook import start_event, init_app
except ModuleNotFoundError:
    from main_webhook import start_event, init_app

try:
    from spndr_tg.config import webhook_port
except ModuleNotFoundError:
    from config import webhook_port

init_app()
webhook_endpoint = Flask(__name__)

@webhook_endpoint.route('/postUpdate', methods = ['POST'])
def postUpdate():
    start_event(request.get_json())
    return 'True'

if __name__ == '__main__':
    webhook_endpoint.run(port = 6000)