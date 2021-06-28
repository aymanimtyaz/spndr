from flask import Flask, request

from config import webhook_port, debug
from telegram_automation.telegram import TelegramMessage
from chatbot_engine import chatbot
from utils import timer

webhook_endpoint = Flask(__name__)

@webhook_endpoint.route('/postUpdate', methods = ['POST'])
@timer
def postUpdate():
    telegram_message = TelegramMessage(request.get_json())
    chatbot.execute(
        uid=telegram_message.sender_id, 
        message=telegram_message.message, 
        chat_id=telegram_message.chat_id, 
        sender_id=telegram_message.sender_id)
    return 'True', 200

if __name__ == '__main__':
    webhook_endpoint.run(port = webhook_port, debug = debug)
