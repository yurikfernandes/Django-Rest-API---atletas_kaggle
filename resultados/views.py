from django.shortcuts import render
from rest_framework import viewsets

from resultados.models import Atleta, Resultado
from resultados.serializers import AtletaSerializer, ResultadoSerializer


class AtletaViewSet(viewsets.ModelViewSet):
    queryset = Atleta.objects.all()
    serializer_class = AtletaSerializer


class ResultadoViewSet(viewsets.ModelViewSet):
    queryset = Resultado.objects.all()
    serializer_class = ResultadoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = ResultadoFilter
    filterset_fields = ('age', 'year', 'season', 'city', 'sport', 'event', 'medal')
