from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.request import Request
import requests
import json
from django.http import JsonResponse
class Message(APIView) :

    def get_summoner_id(self,nickname):
        api ='https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+nickname+'?api_key=RGAPI-f4f16fe6-015f-4471-b99d-e6235bc452d2' 
        data = requests.get(api)
        if data.status_code != 200:
            return False
        return data.json()

    def get_summoner_data(self,encrypt_id):
        api = 'https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/'+encrypt_id+'?api_key=RGAPI-f4f16fe6-015f-4471-b99d-e6235bc452d2'
        data = requests.get(api)
        return data.json()

    def post(self, request , format=None):
        data = request.data
        user_key = data['user_key']
        types = data['type']
        content = data['content']
        result = {"message":{"text":"닉네임을 입력하세요"}}
        if content == '대화하기':
            return Response(
                    status=status.HTTP_200_OK,data=result)

        summoner = self.get_summoner_id(content)
        if summoner is False:
            return Response(data={'message':{'text':'사용자가 존재하지 않습니다.'}})
        encrypt_id = summoner['id']
        summoner_data = self.get_summoner_data(encrypt_id)
        for i in summoner_data:
            if i['queueType'] =='RANKED_TFT':
                tier = i['tier']
                rank = i['rank']
                name = i['summonerName']
                point = i['leaguePoints']
                win = i['wins']
                loss = i['losses']
                result2 = {'message':{'text':'소환사이름 : '+name+'\n티어 : '+tier+' '+rank+'\t'+str(point)+'\n승리 : '+str(win)+'\n패배 : '+str(loss) }}
                return Response(status=status.HTTP_200_OK,data=result2)
        return Response(data={'message':{'text':'전적 검색 결과가 없습니다.'}})


class Keyboard(APIView):

    def get(self, request , format=None):
        return Response({
            'type':'buttons',
            'buttons':['대화하기']
        })

# Create your views here
