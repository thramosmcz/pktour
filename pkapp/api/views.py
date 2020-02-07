from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

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

    def create(self, request):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
