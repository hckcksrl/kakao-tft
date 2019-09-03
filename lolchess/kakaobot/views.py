from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.request import Request
import requests
import json
<<<<<<< HEAD
=======

>>>>>>> ef34e1df3620d382ee3fae25901631017f28ec60
with open('/home/ubuntu/kakao-tft/lolchess/kakaobot/config.json', 'r') as f:
    config = json.load(f)

api_key = config['api_key']
button = {
    'type': 'buttons',
    'buttons': ['소환사 검색']
}

class Message(APIView) :

    def get_summoner_id(self,nickname):
        api =f'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{nickname}?api_key={api_key}'
        data = requests.get(api)
        if data.status_code != 200:
            return False
        return data.json()

    def get_summoner_data(self,encrypt_id):
        api = f'https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/{encrypt_id}?api_key={api_key}'
        data = requests.get(api)
        return data.json()

    # def summoner_result(self, content):
    #
    #     summoner = self.get_summoner_id(content)
    #     encrypt_id = summoner['id']
    #     summoner_data = self.get_summoner_data(encrypt_id)
    #
    #     for i in summoner_data:
    #         if i['queueType'] == 'RANKED_TFT':
    #             return Response(data={
    #                 'message':
    #                     {
    #                         'text': f'소환사이름 : {i["summonerName"]}\n티어 : {i["tier"]} {i["rank"]}\t{i["leaguePoints"]}\n승리 : {i["wins"]}\n패배 : {i["losses"]}'
    #                     }
    #             })
    #
    #     return Response(data={
    #         'message': {
    #             'text': '전적 검색 결과가 없습니다.'
    #         }
    #     })

    def post(self, request , format=None):
        data = request.data
        user_key = data['user_key']
        types = data['type']
        content = data['content']

        if content == '소환사 검색':
            return Response(data={
                'message': {
                    'text': '소환사 이름을 입력하세요'
                },
                'keyboard': button
                # 'keyboard':{
                #     "type": "buttons",
                #     "buttons": [
                #         "처음으로",
                #         "아이템",
                #         "시너지"
                #     ]
                # }
            })
        # elif content == '시너지':
        #     return Response(data={
        #         'message': {
        #             'text': '롤토체스 시너지 보기'
        #         },
        #         'keyboard':{
        #             'type':'buttons',
        #             'buttons':[
        #                 '롤체지지 사이'
        #             ]
        #         }
        #     })
        # elif content == '아이템':
        #     pass
        # else :

        summoner = self.get_summoner_id(content)
        if summoner == False :
            return Response(data={
                'message':{
                    'text': '소환사가 존재하지 않습니다.'
                },
                'keyboard': button
            })
        encrypt_id = summoner['id']
        summoner_data = self.get_summoner_data(encrypt_id)

        for i in summoner_data:
           if i['queueType'] == 'RANKED_TFT':
                return Response(data={
                    'message':
                        {   'photo': {
                                'url': f'http://ddragon.leagueoflegends.com/cdn/9.17.1/img/profileicon/{summoner["profileIconId"]}.png',
                                'width': 640,
                                'height': 480
                            },
                            'text': f'소환사이름 : {i["summonerName"]}\n티어 : {i["tier"]} {i["rank"]}\t{i["leaguePoints"]}\n승리 : {i["wins"]}\n패배 : {i["losses"]}'
                        },
                    'keyboard':button
                })

        return Response(data={
            'message': {
                'text': '전적 검색 결과가 없습니다.'
            },
            'keyboard': button
        })



class Keyboard(APIView):

    def get(self, request , format=None):
<<<<<<< HEAD
        return Response({
            'type':'buttons',
            'buttons':['소환사 검색']
        })
=======
        return Response(data=button)
>>>>>>> ef34e1df3620d382ee3fae25901631017f28ec60
