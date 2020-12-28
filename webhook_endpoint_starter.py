try:
    from spndr_tg.api_engine.webhook_endpoint import start_webhook_endpoint
except ModuleNotFoundError:
    from api_engine.webhook_endpoint import start_webhook_endpoint

start_webhook_endpoint()