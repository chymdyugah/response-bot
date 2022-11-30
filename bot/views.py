from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import BotSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class BotView(GenericAPIView):
    serializer_class = BotSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            predictions = serializer.save()
            return Response(data=predictions, status=status.HTTP_200_OK)
        except Exception as e:
            print(str(e))
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)
