try:
    from spndr_tg.api_engine.telegrambot_webhook import webhook
except ModuleNotFoundError:
    from api_engine.telegrambot_webhook import webhook
        
webhook_object = webhook()
webhook_object.delete_webhook()
webhook_object.set_webhook()
print(webhook_object.get_webhook_info().json())