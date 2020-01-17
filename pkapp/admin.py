from django.contrib import admin
from .models import (
	Players,
	Torneios,
	Etapas,
	Ranking
	)
import math, datetime

class PlayersAdmin(admin.ModelAdmin):
	list_display = ('player', 'email', 'telefone', 'participacoes')
	list_filter = ('player',)
	fields = ['player', 'email', 'telefone', 'participacoes']
	search_fields = ('player',)

class EtapasList(admin.ModelAdmin):
	list_display = ('etapa', 'local', 'data')

class RankingAdmin(admin.ModelAdmin):
	list_display = ('id_torneio', 'id_etapa', 'id_player', 'buy_inn', 
		'qtd_rebuy', 'pontuacao', 'posicao', 'premio')
#	list_filter = ('etapa')

# Register your models here.
admin.site.register(Players, PlayersAdmin)
admin.site.register(Torneios)
admin.site.register(Etapas, EtapasList)
admin.site.register(Ranking, RankingAdmin)