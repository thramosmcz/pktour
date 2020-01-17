from django.urls import path
from . import views

urlpatterns = [
    path('players', views.pkapp_players, name='pkapp_players'),
    path('etapas', views.pkapp_etapas, name='pkapp_etapas'),
    path('admetapa', views.pkapp_admetapa, name='pkapp_admetapa'),
    path('torneios', views.pkapp_torneios, name='pkapp_torneios'),
    path('ranking', views.pkapp_ranking, name='pkapp_ranking'),   
    path('', views.pkapp_index, name='pkapp_index'),
]