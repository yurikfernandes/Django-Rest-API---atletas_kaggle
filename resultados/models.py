from django.db import models


class Atleta(models.Model):
    SEX_OPTIONS = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )

    name = models.CharField(max_length=150, null=False)
    sex = models.CharField(max_length=1, choices=SEX_OPTIONS, null=False)
    height = models.PositiveSmallIntegerField(default=None, help_text='Valor em centímetros. Ex.: 170.')
    weight = models.PositiveSmallIntegerField(default=None, help_text='Valor em kilos. Ex.: 80.')
    team = models.CharField(max_length=50, null=False)
    noc = models.CharField(max_length=3, null=False, help_text='NOC: National Olympic Committee.')

    def __str__(self):
        return self.name


class Resultado(models.Model):

    SEASON_OPTIONS = (
        ('S', 'Summer'),
        ('W', 'Winter'),
    )

    MEDAL_OPTIONS = (
        ('G', 'Gold'),
        ('S', 'Silver'),
        ('B', 'Bronze'),
        ('', 'Sem medalhas'),
    )

    atleta_id = models.ForeignKey(
        'Atleta', on_delete=models.CASCADE, verbose_name='Athlete', related_name='resultados')
    age = models.PositiveSmallIntegerField()
    games = models.CharField(max_length=20, editable=False, null=False)
    year = models.PositiveSmallIntegerField(blank=False, null=False)
    season = models.CharField(max_length=6, choices=SEASON_OPTIONS, null=False)
    city = models.CharField(max_length=30, null=False)
    sport = models.CharField(max_length=30, null=False)
    event = models.CharField(max_length=100, null=False)
    medal = models.CharField(
        max_length=10, choices=MEDAL_OPTIONS, null=True, default='')

    def save(self, *args, **kwargs):
        self.games = str(self.year) + ' ' + self.season
        super(Resultado, self).save(*args, **kwargs)

    def __str__(self):

        medal = ''
        if self.medal == '':
            medal = 'No medal'
        else:
            medal = self.medal
        return self.event + ' - ' + medal