from django.core.management.base import BaseCommand
from riotwatcher import LolWatcher
import requests
from api.models import ChampionList, ChampionSkill
from os import getenv

api_key = getenv('RIOT_API_KEY')


class Command(BaseCommand):
    help = 'Synchronizowanie z RiotAPI'

    def handle(self, *args, **options):
        watcher = LolWatcher(api_key)
        latest = watcher.data_dragon.versions_for_region('na1')['n']['champion']
        static_champ_list = watcher.data_dragon.champions(latest, False, 'en_US')

        for champion_name in static_champ_list['data']:
            if not ChampionList.objects.filter(name=champion_name).exists():
                ChampionList.objects.create(name=champion_name)

                # Skile
                link = f"http://ddragon.leagueoflegends.com/cdn/{latest}/data/en_US/champion/{champion_name}.json"
                r = requests.get(link)
                data = r.json()
                ChampionSkill.objects.create(
                    name=champion_name,
                    skill_0=data['data'][champion_name]['spells'][0]['id'],
                    skill_1=data['data'][champion_name]['spells'][1]['id'],
                    skill_2=data['data'][champion_name]['spells'][2]['id'],
                    skill_3=data['data'][champion_name]['spells'][3]['id'],
                )
                print(f"[+] {champion_name}")
