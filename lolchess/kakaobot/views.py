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


def get_summoner_id(nickname):
    api = f'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{nickname}?api_key={api_key}'
    data = requests.get(api)
    if data.status_code != 200:
        return False
    return data.json()


def get_summoner_data(encrypt_id):
    api = f'https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/{encrypt_id}?api_key={api_key}'
    data = requests.get(api)
    return data.json()


class TFT(APIView) :



    def post(self, request , format=None):
        data = request.data
        summoner_id = data['action']['params']['summoner']
        print(summoner_id)
        summoner = get_summoner_id(summoner_id)
        print(summoner)
        if summoner == False :
            return Response(data={
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "simpleText": {
                                "text": '소환사가 존재하지 않습니다.'
                                }
                            }
                        ]
                    }
        })
        encrypt_id = summoner['id']
        summoner_data = get_summoner_data(encrypt_id)
        print(summoner_data)
        for i in summoner_data:
           if i['queueType'] == 'RANKED_TFT':
                return Response(data={
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "basicCard": {
                                "title" : i["summonerName"],
                                "description" : f'티어 : {i["tier"]} {i["rank"]}    {i["leaguePoints"]}점\n승리 : {i["wins"]}\n패배 : {i["losses"]}'
                                },
                                "thumbnail" : f'http://ddragon.leagueoflegends.com/cdn/9.17.1/img/profileicon/{summoner["profileIconId"]}.png'
                            }
                        ]
                    }
        })

        return Response(data={
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "simpleText": {
                                "text": '전적 검색 결과가 없습니다.'
                                }
                            }
                        ]
                    }
        })

class Rank(APIView):

    def post(self, request):
        data = request.data
        summoner_id = data['action']['params']['summoner']
        print(summoner_id)
        summoner = get_summoner_id(summoner_id)
        if summoner == False:
            return Response(data={
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "simpleText": {
                                "text": '소환사가 존재하지 않습니다.'
                            }
                        }
                    ]
                }
            })
        encrypt_id = summoner['id']
        summoner_data = get_summoner_data(encrypt_id)
        for i in summoner_data:
            if i['queueType'] == 'RANKED_SOLO_5x5':
                return Response(data={
                    "version": "2.0",
                    "template": {
                        "outputs": [
                            {
                                "basicCard": {
                                "title" : i["summonerName"],
                                "description" : f'티어 : {i["tier"]} {i["rank"]}    {i["leaguePoints"]}점\n승리 : {i["wins"]}\n패배 : {i["losses"]}'
                                },
                                "thumbnail" : f'http://ddragon.leagueoflegends.com/cdn/9.17.1/img/profileicon/{summoner["profileIconId"]}.png'
                            }
                        ]
                    }
                })

        return Response(data={
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": '전적 검색 결과가 없습니다.'
                        }
                    }
                ]
            }
        })


