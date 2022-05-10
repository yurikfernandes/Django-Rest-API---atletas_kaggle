# Generated by Django 4.0.4 on 2022-05-10 02:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resultados', '0002_resultado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atleta',
            name='height',
            field=models.PositiveSmallIntegerField(default=None, help_text='Valor em centímetros. Ex.: 170.'),
        ),
        migrations.AlterField(
            model_name='atleta',
            name='noc',
            field=models.CharField(help_text='NOC: National Olympic Committee.', max_length=3),
        ),
        migrations.AlterField(
            model_name='atleta',
            name='weight',
            field=models.PositiveSmallIntegerField(default=None, help_text='Valor em kilos. Ex.: 80.'),
        ),
        migrations.AlterField(
            model_name='resultado',
            name='age',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='resultado',
            name='atleta_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resultados.atleta', verbose_name='Athlete'),
        ),
        migrations.AlterField(
            model_name='resultado',
            name='games',
            field=models.CharField(editable=False, max_length=20),
        ),
        migrations.AlterField(
            model_name='resultado',
            name='year',
            field=models.PositiveSmallIntegerField(),
        ),
    ]