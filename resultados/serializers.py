from rest_framework import serializers

from resultados.models import Atleta, Resultado
from resultados.validators import (valid_age, valid_city, valid_event,
                                   valid_height, valid_name, valid_noc,
                                   valid_season, valid_sex, valid_sport,
                                   valid_team, valid_weight, valid_year)


class AtletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atleta
        fields = '__all__'

    def validate(self, data):
        if not valid_name(data['name']):
            raise serializers.ValidationError(
                {'name', 'O campo name não deve conter números.'})
        if not valid_sex(data['sex']):
            raise serializers.ValidationError(
                {'sex', 'O campo sex deve ser preenchido com "M" ou "F".'})
        if not valid_height(data['height']):
            raise serializers.ValidationError(
                {'height', 'Digite um número válido. Entre 0 e 250.'})
        if not valid_weight(data['weight']):
            raise serializers.ValidationError(
                {'weight', 'Digite um número válido.'})
        if not valid_team(data['team']):
            raise serializers.ValidationError(
                {'team', 'O campo name não deve conter números.'})
        if not valid_noc(data['noc']):
            raise serializers.ValidationError(
                {'noc', 'O campo name não deve conter números.'})
        return data


class ResultadoSerializer(serializers.ModelSerializer):

    nome_atleta = serializers.ReadOnlyField(source='atleta.name')

    class Meta:
        model = Resultado
        exclude = []

    def validate(self, data):
        if not valid_age(data['age']):
            raise serializers.ValidationError(
                {'age', 'O campo idade não pode ter mais que 2 digitos.'})
        if not valid_year(data['year']):
            raise serializers.ValidationError(
                {'year', 'O campo year estar entre 0 e 2023.'})
        if not valid_season(data['season']):
            raise serializers.ValidationError(
                {'season', 'O campo season deve ser preenchido com "S" (summer) ou "W" (winter).'})
        if not valid_city(data['city']):
            raise serializers.ValidationError(
                {'city', 'O campo city não deve conter números.'})
        if not valid_sport(data['sport']):
            raise serializers.ValidationError(
                {'sport', 'O campo sport não deve conter números.'})
        if not valid_event(data['event']):
            raise serializers.ValidationError(
                {'event', 'O campo event não deve conter apenas números.'})

        return data
