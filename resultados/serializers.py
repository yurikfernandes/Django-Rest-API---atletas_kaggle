from rest_framework import serializers

from resultados.models import Atleta


class AtletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atleta
        fields = '__all__'
