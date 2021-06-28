from extensions import t
from config import webhook_url

t.delete_webhook(True)
t.set_webhook(webhook_url=webhook_url)
