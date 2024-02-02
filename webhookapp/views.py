from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class WebhookApp(APIView):
    def get(self,req:Request)->Response:
        return Response({"message":"welcome to Webhook App"},status=status.HTTP_200_OK)
        
    def post(self,req:Request)->Response:
        return Response({"message":"welcome to Webhook App"},status=status.HTTP_200_OK)