from secrets import token_bytes
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Game, Dev
from .forms import PlaytimeForm


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def games_index(request):
  games = Game.objects.all()
  return render(request, 'games/index.html', {'games': games})

def games_detail(request, game_id):
  game = Game.objects.get(id=game_id)
  playtime_form = PlaytimeForm()
  dev_ids = game.devs.all().values_list('id')
  devs = Dev.objects.exclude(id__in=dev_ids)
  return render(request, 'games/detail.html', {
    'game': game,
    'playtime_form': playtime_form,
    'devs': devs
  })

class GameCreate(CreateView):
  model = Game
  fields = ['name', 'genre', 'description', 'release']

class GameUpdate(UpdateView):
  model = Game
  fields = ['genre', 'description', 'release']

class GameDelete(DeleteView):
  model = Game
  success_url = '/games/'

def add_playtime(request, game_id):
  form = PlaytimeForm(request.POST)
  if form.is_valid():
    new_playtime = form.save(commit=False)
    new_playtime.game_id = game_id
    new_playtime.save()
  return redirect('detail', game_id=game_id)

class DevList(ListView):
  model = Dev

class DevDetail(DetailView):
  model = Dev

class DevCreate(CreateView):
  model = Dev
  fields = '__all__'

class DevUpdate(UpdateView):
  model = Dev
  fields = ['name', 'description']

class DevDelete(DeleteView):
  model = Dev
  success_url = '/devs/'

def assoc_dev(request, game_id, dev_id):
  game = Game.objects.get(id=game_id)
  game.devs.add(dev_id)
  return redirect('detail', game_id=game_id)

def unassoc_dev(request, game_id, dev_id):
  game = Game.objects.get(id=game_id)
  game.devs.remove(dev_id)
  return redirect('detail', game_id=game_id)

