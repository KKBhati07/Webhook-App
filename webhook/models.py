from django.db import models
import time,uuid


# method to generate unique id for each webhook
def generate_unique_id()->str:
    id= f"{time.time()}-{uuid.uuid4()}"
    return id[:20]


# model for webhooks
class Webhook(models.Model):
    id=models.CharField(default=generate_unique_id,unique=True,primary_key=True,editable=False, max_length=25)
    company_id = models.CharField(max_length=100)
    url = models.URLField()
    headers = models.JSONField(blank=True, null=True)
    events = models.JSONField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Webhook: {self.id} - Company: {self.company_id}"
