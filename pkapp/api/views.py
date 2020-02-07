from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
import json

from pkapp.api.serializers import *
from pkapp.models import *


class EtapaViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Etapas.objects.all()
        serializer = EtapaSerializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Etapas.objects.all()
        etapa = get_object_or_404(queryset, pk=pk)
        serializer = EtapaSerializer(etapa)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def ranking(self, request, pk=None):
        qset_etapa = Etapas.objects.all()
        etapa = get_object_or_404(qset_etapa, pk=pk)

        qset_ranking = Ranking.objects.filter(id_etapa=etapa.id)
        serializer = RankingSerializer(qset_ranking, many=True)

        return Response(serializer.data)

    @ranking.mapping.post
    def update_ranking(self, request, pk=None):
        json_data = json.loads(request.body)
        body_ids = list(map(lambda j: j['id'], json_data))

        qset_etapa = Etapas.objects.all()
        etapa = get_object_or_404(qset_etapa, pk=pk)
        db_ranking = Ranking.objects.filter(id_etapa=etapa.id).values()
        db_ids = list(map(lambda j: j['id'], db_ranking))
        print(body_ids)
        print(db_ids)
        print(set(body_ids).intersection(db_ids))

        return Response("OK")

    @action(detail=True, methods=['post'])
    def inscrito(self, request, pk=None):
        json_data = json.loads(request.body)
        body_players_ids = list(map(lambda j: j['id'], json_data))

        qset_etapa = Etapas.objects.all()
        etapa = get_object_or_404(qset_etapa, pk=pk)

        qset_existing = Ranking.objects.filter(id_etapa=etapa.id,id_player__in=body_players_ids).values()
        to_create = body_players_ids.copy()
        for x in qset_existing:
            try:
                to_create.remove(x['id_player_id'])
            except ValueError:
                pass

        for id in to_create:
            r = Ranking( id_etapa=etapa, id_torneio = etapa.id_torneio, id_player = Players.objects.get(pk=id),
                         buy_inn = 1, qtd_rebuy = 0, posicao = 0, pontuacao = 0, premio = 0)
            r.save()

        print(body_players_ids)
        print(to_create)
        qset_ranking = Ranking.objects.filter(id_etapa=etapa.id,id_player__in=body_players_ids)
        serializer = RankingSerializer(qset_ranking, many=True)

        return Response(serializer.data)

    @inscrito.mapping.delete
    def inscrito_del(self, request, pk=None):
        json_data = json.loads(request.body)
        body_players_ids = list(map(lambda j: j['id'], json_data))

        qset_etapa = Etapas.objects.all()
        etapa = get_object_or_404(qset_etapa, pk=pk)

        qset_existing = Ranking.objects.filter(id_etapa=etapa.id,id_player__in=body_players_ids).delete()

        qset_ranking = Ranking.objects.filter(id_etapa=etapa.id)
        serializer = RankingSerializer(qset_ranking, many=True)

        return Response(serializer.data)

    def create(self, request):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass


class PlayerViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Players.objects.all().order_by('-participacoes')
        serializer = PlayerSerializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Players.objects.all()
        player = get_object_or_404(queryset, pk=pk)
        serializer = PlayerSerializer(player)
        return Response(serializer.data)

    def create(self, request):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass


class RankingViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Torneios.objects.all()
        serializer = TorneioSerializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Torneios.objects.all()
        torneio = get_object_or_404(queryset, pk=pk)
        serializer = TorneioSerializer(torneio)
        return Response(serializer.data)

    @action(methods=['get'], detail=True)
    def etapas(self, request, pk=None):
        qset_torneio = Torneios.objects.all()
        torneio = get_object_or_404(qset_torneio, pk=pk)

        qset_etapa = Etapas.objects.filter(id_torneio=torneio.id)
        serializer = EtapaSerializer(qset_etapa, many=True)

        return Response(serializer.data)

    def create(self, request):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass


class TorneioViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Torneios.objects.all()
        serializer = TorneioSerializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Torneios.objects.all()
        torneio = get_object_or_404(queryset, pk=pk)
        serializer = TorneioSerializer(torneio)
        return Response(serializer.data)

    @action(methods=['get'], detail=True)
    def etapas(self, request, pk=None):
        qset_torneio = Torneios.objects.all()
        torneio = get_object_or_404(qset_torneio, pk=pk)

        qset_etapa = Etapas.objects.filter(id_torneio=torneio.id)
        serializer = EtapaSerializer(qset_etapa, many=True)

        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def ranking(self, request, pk=None):
        qset_torneio = Torneios.objects.all()
        torneio = get_object_or_404(qset_torneio, pk=pk)

        qset_ranking = Ranking.objects.filter(id_torneio=torneio.id).order_by('id_etapa_id')
        serializer = RankingSerializer(qset_ranking, many=True)

        return Response(serializer.data)

    def create(self, request):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
