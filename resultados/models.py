from django.db import models

class Atleta(models.Model):
    SEX_OPTIONS = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )

    name = models.CharField(max_length=150, null=False)
    sex = models.CharField(max_length=1, choices=SEX_OPTIONS, null=False)
    height = models.IntegerField(default=None)
    weight = models.IntegerField(default=None)
    team = models.CharField(max_length=50, null=False)
    noc = models.CharField(max_length=3, null=False)

    def __str__(self):
        return self.name