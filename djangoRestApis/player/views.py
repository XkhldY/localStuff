from django.shortcuts import render, redirect
from gameplay.models import Game
from django.contrib.auth.decorators import login_required
from .forms import InvitationForm


# Create your views here.
def home(request):
    # games_fp = Game.objects.filter(first_player=request.user)
    # game_sp = Game.objects.filter(second_player=request.user)
    # all_games = list(games_fp) + list(game_sp)
    if request.user.is_authenticated:
        all_games = list(Game.objects.games_for_user(request.user))
        all_games.sort(key=lambda x: x.id)

        return render(request, 'player/home.html', {'game_name': 'motherfucker', 'games': all_games})
    else:
        return render(request, 'welcome.html')


@login_required
def welwel(request):
    return render(request, 'welcome.html')


@login_required
def new_invitation(request):
    form = InvitationForm()
    return render(request, 'player/new_invitation_form.html', {'form': form})
