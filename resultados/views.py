from django.shortcuts import render
from rest_framework import viewsets

from resultados.models import Atleta
from resultados.serializers import AtletaSerializer


class AtletaViewSet(viewsets.ModelViewSet):
    queryset = Atleta.objects.all()
    serializer_class = AtletaSerializer
