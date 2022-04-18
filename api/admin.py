from django.contrib import admin

from .models import ChampionList
from .models import ChampionSkill
# Register your models here.


class ChampionListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ['id']
    search_fields = ['name']


class ChampionSkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'skill_0', 'skill_1', 'skill_2', 'skill_3')
    ordering = ['id']
    search_fields = ['name']


admin.site.register(ChampionList, ChampionListAdmin)
admin.site.register(ChampionSkill, ChampionSkillAdmin)
