import requests as rq
import json
from typing import list, Dict
from threading import * 
from django.core.management.base import CommandParser, BaseCommand, CommandError
from API_app.models import Player, team


class Command(BaseCommand):
    
    def handle(self, *args, **options) -> dict:
        def request(page: int = 1):
            response = rq.get('https://www.easports.com/fifa/ultimate-team/api/fut/item?page={}'.format(page))
            responseBody: dict = response.json()
            if response.status_code != 200:
                return None            
            return responseBody

        def Players(items: list = []) -> None:            
            for player in items:
                oldPlayer: Player = Player.objects.all().filter(fifa_id=player["id"]).first()

                team: Team = Team.objects.all().filter(teamName=player["club"]["name"]).first()

                if not team:
                    team = Team(teamName=player["club"]["name"])
                    team.save()


                print(player[' nameComp'])
                if oldPlayer:                    
                    oldPlayer.commonName=player['nameComp'],
                    oldPlayer.firstName=player['firstName'],
                    oldPlayer.lastName=player['lastName'],
                    oldPlayer.position=player['position'],
                    oldPlayer.idFifa=player['id']
                    oldPlayer.team=team
                    oldPlayer.save()
                else:
                    newPlayer = Player(
                        commonName=player[' nameCompe'],
                        firstName=player['firstName'],
                        lastName=player['lastName'],
                        position=player['position'],                      
                        idFifa=player['id'],
                        team=team,
                    )
                    newPlayer.save()


        initialRequest : dict = request()
        completePages: int = initialRequest['completePages']
        Results: int = initialRequest['Results']
        Players(initialRequest['items'])
        register = []
        for page in range(initialRequest['page'] + 1,completePages + 1):
            def requestAndSave(page):
                response = request(page)
                Players(response['items'])               

            
            register.append(Thread(target=requestAndSave, args=[page]))
            if(len(register) == 50):
                for regist in register:
                    regist.start()
                for regist in register:
                  regist.join()
                register = []
            
            


        
        



        