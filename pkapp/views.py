from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Players, Torneios, Etapas, Ranking
from .forms import PlayersForm, TorneiosForm, EtapasForm, TorneiosRanking
# Create your views here.

#def home(request):
#	return HttpResponse('index.html')
def pkapp_index(request):
	vlrtemplate = 'Envio de valor teste para template pela View 12345'
	return render(request, 'pkapp/index.html', {'vlrtemplate': vlrtemplate})

def pkapp_players(request):
	players = Players.objects.all()
	return render(request, 'pkapp/players.html', {'players': players})


def pkapp_etapas(request):
	etapas = Etapas.objects.all()
	return render(request, 'pkapp/etapas.html', {'etapas': etapas})

def pkapp_admetapa(request):
	form = AdmEtapa(request.POST or None)
	if form.is_valid():
		form.save()
	return redirect('pkapp_admetapa')

def pkapp_torneios(request):
	torneios = Torneios.objects.all()
	return render(request, 'pkapp/torneios.html', {'torneios': torneios})

def pkapp_ranking(request):
	teste = 'Conteudo de ranking'
	return render(request, 'pkapp/ranking.html', {'teste': teste})