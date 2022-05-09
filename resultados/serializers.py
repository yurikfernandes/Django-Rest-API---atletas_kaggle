from rest_framework import serializers

from resultados.models import Atleta, Resultado


class AtletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atleta
        fields = '__all__'

class ResultadoSerializer(serializers.ModelSerializer):
    
    nome_atleta = serializers.ReadOnlyField(source='atleta.name')

    class Meta:
        model = Resultado        
        exclude = []