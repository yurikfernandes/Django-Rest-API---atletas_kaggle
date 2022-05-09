from django_filters import rest_framework as filters

from resultados.models import Resultado


class ResultadoFilter(filters.FilterSet):
    age = filters.CharFilter(field_name='age', lookup_expr='icontains')
    games = filters.CharFilter(field_name='games', lookup_expr='icontains')
    year = filters.CharFilter(field_name='year', lookup_expr='icontains')
    season = filters.CharFilter(field_name='season', lookup_expr='icontains')
    city = filters.CharFilter(field_name='city', lookup_expr='icontains')
    sport = filters.CharFilter(field_name='sport', lookup_expr='icontains')
    event = filters.CharFilter(field_name='event', lookup_expr='icontains')
    medal = filters.CharFilter(field_name='medal', lookup_expr='icontains')

    class Meta:
        model = Resultado
        fields = ('age', 'games', 'year', 'season',
                  'city', 'sport', 'event', 'medal')
