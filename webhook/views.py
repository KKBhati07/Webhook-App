# importing request and response from DRF
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# importing webhook model
from .models import Webhook
from typing import Any

from webhookapp.settings import COMPANY_ID

# importing webhook serializer
from .serializer import WebhookSerializer
# hardcoding company id for demonstration purpose
class WebhookApi(APIView):
    # ----------------------------------------GET-------------------------------
    def get(self,req:Request,id:Any=None)->Response:
        if id:
            return self.get_one(req,id)
        return self.get_all(req)
    
    # to get one webhook by id
    def get_one(self,req:Request,id:Any)->Response:
        try:
            webhook=Webhook.objects.get(id=str(id))
            serializer=WebhookSerializer(webhook)
            return Response({"webhook":serializer.data,"message":"Webhook fetched successfully"},status=status.HTTP_200_OK)
        # if there is no webhook with the provided id
        except Webhook.DoesNotExist:
            return Response({"message":"Webhook not found"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message":"Internal Server Error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    # to get all webhooks
    def get_all(self,req:Request)->Response:
        try:
            webhooks=Webhook.objects.filter(company_id=COMPANY_ID)
            serializer=WebhookSerializer(webhooks,many=True)
            return Response({"webhook":serializer.data,"message":"Webhooks fetched successfully"},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message":"Internal Server Error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # ------------------------------------POST---------------------------------------
    def post(self,req:Request)->Response:
        try:
            serializer=WebhookSerializer(data=req.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"webhookId":serializer.data["id"],"message":"Webhook created successfully"},status=status.HTTP_201_CREATED)
            # if invalid data is provided
            return Response({"message":"Invalid data"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message":"Internal Server Error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    # ---------------------------------PATCH------------------------------------
    # to update a webhook
    def patch(self, req: Request, id: Any) -> Response:
        try:
            webhook = Webhook.objects.get(id=str(id))
            serializer = WebhookSerializer(instance=webhook, data=req.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"webhookId": serializer.data["id"], "message": "Webhook updated successfully"}, status=status.HTTP_200_OK)
            return Response({"message": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)

        except Webhook.DoesNotExist:
            return Response({"message": "Webhook not found"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({"message": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    # ----------------------------------DELETE----------------------------------

    # to delete a webhook
    def delete(self, req: Request, id: Any) -> Response:
        try:
            webhook = Webhook.objects.get(id=str(id))
            webhook.delete()

            return Response({"message": "Webhook deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        
        except Webhook.DoesNotExist:
            return Response({"message": "Webhook not found"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({"message": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
