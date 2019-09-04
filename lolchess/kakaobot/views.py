from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.request import Request
import requests
import json
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


    def post(self, request , format=None):
        data = request.data
        summoner_id = data['action']['name']
        print(data)
        result = {
                "version": "2.0",
                "template": {
                    "output": [
                        {
                            "simpleText": {
                                "text": "옹박엘보우"
                                }
                            }
                        ]
                    }
        }
        return Response(status=status.HTTP_200_OK, data=result)
        # data = request.data
        # content = data['content']
        #
        # if content == '소환사 검색':
        #     return Response(data={
        #         'message': {
        #             'text': '소환사 이름을 입력하세요'
        #         }
        #     })
        #
        # summoner = self.get_summoner_id(content)
        # if summoner == False :
        #     return Response(data={
        #         'message':{
        #             'text': '소환사가 존재하지 않습니다.'
        #         },
        #         'keyboard': button
        #     })
        # encrypt_id = summoner['id']
        # summoner_data = self.get_summoner_data(encrypt_id)
        #
        # for i in summoner_data:
        #    if i['queueType'] == 'RANKED_TFT':
        #         return Response(data={
        #             'message':
        #                 {   'photo': {
        #                         'url': f'https://cdn.lolchess.gg/images/lol/tier/{i["tier"].lower()}_{len(i["rank"])}.png',
        #                         'width': 640,
        #                         'height': 640
        #                     },
        #                     'text': f'소환사이름 : {i["summonerName"]}\n티어 : {i["tier"]} {i["rank"]}    {i["leaguePoints"]}점\n승리 : {i["wins"]}\n패배 : {i["losses"]}'
        #                 },
        #         })
        #
        # return Response(data={
        #     'message': {
        #         'text': '전적 검색 결과가 없습니다.'
        #     },
        # })



class Keyboard(APIView):

    def get(self, request , format=None):
        return Response(data=button)
