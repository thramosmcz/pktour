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

class AdmEtapaForm(ModelForm):
	class Meta:
		model = Etapas
		fields = '__all__'
		#model = Players
		#fields = '__all__'
		#model = Ranking
		#fields = '__all__'
		#model = Torneios
		#fields = '__all__'

	def create_etapas_adm(self, etapa, etapas_ids):
		for etapa_id in etapas_ids:
			Etapas_Torneio.objects.create(etapa=etapa, etapa_id=etapa_id)
