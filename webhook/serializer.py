from rest_framework import serializers
from .models import Webhook

from webhookapp.settings import COMPANY_ID

# to serialize webhook object
class WebhookSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    url = serializers.URLField()
    headers = serializers.JSONField(required=False)
    events = serializers.JSONField()
    is_active = serializers.BooleanField(default=True)

    # method to create new webhook
    def create(self, validated_data):
        url = validated_data["url"]
        headers = validated_data["headers"]
        events = validated_data["events"]
        is_active = validated_data["is_active"]
        return Webhook.objects.create(company_id=COMPANY_ID,url=url,headers=headers,events=events,is_active=is_active)
    # to update the existing webhook
    def update(self, instance, validated_data):
        instance.company_id = validated_data.get("company_id", instance.company_id)
        instance.url = validated_data.get("url", instance.url)
        instance.headers = validated_data.get("headers", instance.headers)
        instance.events = validated_data.get("events", instance.events)
        instance.is_active = validated_data.get("is_active", instance.is_active)
        instance.save()
        return instance
