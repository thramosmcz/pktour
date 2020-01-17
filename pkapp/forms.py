from django.forms import ModelForm
from .models import Players, Etapas, Torneios, Ranking

class PlayersForm(ModelForm):
	class Meta:
		model = Players
		fields = '__all__'

class EtapasForm(ModelForm):
	class Meta:
		model = Etapas
		fields = '__all__'

class TorneiosForm(ModelForm):
	class Meta:
		model = Torneios
		fields = '__all__'

class TorneiosRanking(ModelForm):
	class Meta:
		model = Ranking
		fields = '__all__'

# class AdmEtapa(ModelForm):
# 	class Meta: