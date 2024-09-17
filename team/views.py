from django.shortcuts import render
from .models import *


# Create your views here.
def teams(request):
    all_teams = Team.objects.all()
    context = {
        'all_teams': all_teams,
    }
    return render(request, 'our_team.html', context)
