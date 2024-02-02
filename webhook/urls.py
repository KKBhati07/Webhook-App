from django.urls import path

from .views import WebhookApi
urlpatterns=[
    path("",WebhookApi.as_view()),
    path("<id>/",WebhookApi.as_view()),
]