# Generated by Django 4.0.4 on 2022-05-09 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resultados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('games', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
                ('season', models.CharField(choices=[('S', 'Summer'), ('W', 'Winter')], max_length=6)),
                ('city', models.CharField(max_length=30)),
                ('sport', models.CharField(max_length=30)),
                ('event', models.CharField(max_length=100)),
                ('medal', models.CharField(choices=[('G', 'Gold'), ('S', 'Silver'), ('B', 'Bronze'), ('', 'Sem medalhas')], default='', max_length=10, null=True)),
                ('atleta_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resultados.atleta', verbose_name='atleta.name')),
            ],
        ),
    ]
