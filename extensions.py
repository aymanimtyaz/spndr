import redis

from telegram_automation.telegram import Telegram
from config import bot_token

t = Telegram(bot_token)
red = redis.Redis(decode_responses=True)