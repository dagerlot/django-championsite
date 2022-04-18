from django.db import models

# Create your models here.


class ChampionList(models.Model):
    name = models.CharField(max_length=30)

    def get_icon(self):
        return f"https://ddragon.leagueoflegends.com/cdn/12.7.1/img/champion/{self.name}.png"
    
    
class ChampionSkill(models.Model):
    name = models.CharField(max_length=30)
    skill_0 = models.CharField(max_length=30)
    skill_1 = models.CharField(max_length=30)
    skill_2 = models.CharField(max_length=30)
    skill_3 = models.CharField(max_length=30)
