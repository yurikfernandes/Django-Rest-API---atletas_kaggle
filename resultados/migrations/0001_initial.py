# Generated by Django 4.0.4 on 2022-05-09 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('sex', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1)),
                ('height', models.IntegerField(default=None)),
                ('weight', models.IntegerField(default=None)),
                ('team', models.CharField(max_length=50)),
                ('noc', models.CharField(max_length=3)),
            ],
        ),
    ]
