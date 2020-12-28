import requests

try:
    from spndr_tg.config import bot_token, webhook_url
except ModuleNotFoundError:
    from config import bot_token, webhook_url



class webhook:

    service_url_prefix = 'https://api.telegram.org/bot'+bot_token

    def set_webhook(self):
        api_params = {"url":webhook_url}
        requests.post(self.service_url_prefix + '/setWebhook', data = api_params)

    def delete_webhook(self):
        delete_webhook_request = requests.post(self.service_url_prefix + '/deleteWebhook')
        if delete_webhook_request:
            print('Webhook successfully deleted')

    def get_webhook_info(self):
        webhook_info_request = requests.post(self.service_url_prefix + '/getWebhookInfo')
        return webhook_info_request