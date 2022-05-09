from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from resultados.filters import AtletaFilter, ResultadoFilter
from resultados.models import Atleta, Resultado
from resultados.serializers import AtletaSerializer, ResultadoSerializer


class AtletaViewSet(viewsets.ModelViewSet):
    '''Listagem de todos atletas cadastrados.'''

    queryset = Atleta.objects.all()
    serializer_class = AtletaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = AtletaFilter
    filterset_fields = ('height', 'weight', 'name', 'sex',
                        'team', 'noc')


class ResultadoViewSet(viewsets.ModelViewSet):
    '''Listagem de todos resultados cadastrados.'''
    
    queryset = Resultado.objects.all()
    serializer_class = ResultadoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = ResultadoFilter
    filterset_fields = ('age', 'year', 'season', 'city',
                        'sport', 'event', 'medal')
