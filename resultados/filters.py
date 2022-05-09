from tabnanny import verbose

from django_filters import rest_framework as filters

from resultados.models import Atleta, Resultado


class ResultadoFilter(filters.FilterSet):
    age = filters.CharFilter(field_name='age', lookup_expr='iexact')
    year = filters.CharFilter(field_name='year', lookup_expr='iexact')
    games = filters.CharFilter(field_name='games', lookup_expr='icontains')
    season = filters.CharFilter(field_name='season', lookup_expr='icontains')
    city = filters.CharFilter(field_name='city', lookup_expr='icontains')
    sport = filters.CharFilter(field_name='sport', lookup_expr='icontains')
    event = filters.CharFilter(field_name='event', lookup_expr='icontains')
    medal = filters.CharFilter(field_name='medal', lookup_expr='icontains')

    class Meta:
        model = Resultado
        fields = ('age', 'year', 'games', 'season',
                  'city', 'sport', 'event', 'medal')


class AtletaFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    sex = filters.CharFilter(field_name='sex', lookup_expr='iexact')
    height = filters.CharFilter(field_name='height', lookup_expr='iexact')
    weight = filters.CharFilter(field_name='weight', lookup_expr='iexact')
    team = filters.CharFilter(field_name='team', lookup_expr='icontains')
    noc = filters.CharFilter(field_name='noc', lookup_expr='icontains')

    class Meta:
        model = Atleta
        fields = ('height', 'weight', 'sex', 'name',
                  'team', 'noc')
