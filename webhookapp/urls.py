from django.urls import path,include

# importing webhook urls file
import webhook.urls as webhook_urls
from .views import WebhookApp
urlpatterns = [
    path('', WebhookApp.as_view()),
    path('webhooks/', include(webhook_urls)),

]
