# importing shared task form celery
from celery import shared_task
from celery.exceptions import Retry
# importing model
from .models import Webhook
# importing request module
import requests

# function to fire event
@shared_task
def fire_event(event_name:str, company_id:str,data:dict={}):
    try:
        active_subscriptions = Webhook.objects.filter(events__contains=[event_name], company_id=company_id, is_active=True)
        for subscription in active_subscriptions:
            try:
                call_webhook.delay(url=subscription.url,headers=subscription.headers or {},data=data,)
            except Retry as exc:
                pass
    except Exception as e:
        pass
    

# function to call the webhook
@shared_task(bind=True)
def call_webhook(self, url, headers, data, max_retries=3, backoff=2):
    try:
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()
    except requests.exceptions.RequestException as exc:
        if self.request.retries < max_retries:
            # for exponential backoff
            retry_delay = backoff ** self.request.retries 
            self.retry(countdown=retry_delay, exc=exc)
        else:
            pass

