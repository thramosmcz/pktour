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


class RankingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ranking
        fields = ['id', 'id_torneio_id', 'id_etapa_id', 'id_player_id', 'buy_inn', 'qtd_rebuy', 'posicao', 'pontuacao', 'premio']


class TorneioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Torneios
        fields = ['id', 'torneio', 'qtd_rebuy', 'qtd_players', 'vlr_buyinn', 'vlr_rebuy', 'vlr_jackpot']
