from rest_framework import serializers
from pkapp.models import *


class EtapaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Etapas
        fields = ['id', 'etapa', 'local', 'data', 'status', 'id_torneio_id']


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Players
        fields = ['id', 'player', 'email', 'telefone', 'participacoes']


class TorneioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Torneios
        fields = ['id', 'torneio', 'qtd_rebuy', 'qtd_players', 'vlr_buyinn', 'vlr_rebuy', 'vlr_jackpot']
