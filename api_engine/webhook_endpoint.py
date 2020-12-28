from flask import Flask, request
import json
import redis

try:
    from spndr_tg.config import webhook_port
except ModuleNotFoundError:
    from config import webhook_port

r = redis.Redis(decode_responses = True)

webhook_endpoint = Flask(__name__)

@webhook_endpoint.route('/postUpdate', methods = ['POST'])
def postUpdate():
    r.lpush("update_queue", json.dumps(request.get_json()))
    return 'True'

def start_webhook_endpoint():
    webhook_endpoint.run(port = webhook_port)

    

