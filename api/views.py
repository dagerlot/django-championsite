from django.shortcuts import render
# from django.http import HttpResponse
from .models import ChampionSkill, ChampionList
from django.shortcuts import get_object_or_404


def index(request):
    names = ChampionList.objects.all()
    return render(request, 'index.html', {'names': names})


def champion_view(request, champion_name):
    champion = get_object_or_404(ChampionSkill, name=champion_name)
    return render(request, 'troll_builds.html', {'champion': champion})


def static(request):
    return render(request, 'index.html')
