from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.request import Request

class Message(APIView) :

   def post(self, request , format=None):
       print(request.data)
       return Response(status=status.HTTP_200_OK)



class Keyboard(APIView):

    def get(self, request , format=None):
        return Response({
            'type':'buttons',
            'buttons':['1','2']
        })

# Create your views here
