from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.request import Request
import requests
import json

class Message(APIView) :

    def get_summoner_id(self,nickname):
        api =  'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+nickname+'?api_key=RGAPI-191a0cbf-9630-4561-8601-d916fe96df37'
        data = requests.get(api)
        return data

    def get_summoner_data(self,encrypt_id):
        api = 'https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/'+encrypt_id+'?api_key=RGAPI-191a0cbf-9630-4561-8601-d916fe96df37'
        data = requests.get(api)
        return data

    def post(self, request , format=None):
        data = request.data
        user_key = data['user_key']
        types = data['type']
        content = data['content']
        if types == '대화하기':
            return Response(status=status.HTTP_200_OK,data=types)

        summoner = self.get_summoner_id(content)
        encrypt_id = summoner.json()['id']
        summoner_data = self.get_summoner_data(encrypt_id)
        # summoner_data_json = json.dumps(summoner_data)
        return Response(status=status.HTTP_200_OK,data=summoner_data.json()[2])



class Keyboard(APIView):

    def get(self, request , format=None):
        return Response({
            'type':'buttons',
            'buttons':['1','2']
        })

# Create your views here
