import os, django
import pandas as pd
from tqdm import tqdm

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from resultados.models import Atleta, Resultado

SRC_DIR = os.getcwd()
csv_path = os.path.join(SRC_DIR, "athlete_events.csv")

df = pd.read_csv(csv_path)
df = df.sort_values(by=['ID'])

df_atletas = df.copy()
df_atletas = df_atletas[['ID','Name', 'Sex', 'Height', 'Weight', 'Team', 'NOC']].drop_duplicates(subset=['ID'])
df_atletas.fillna({'Height': 0, 'Weight': 0}, inplace=True)
dicionario_de_atletas = df_atletas.to_dict('index')

df_resultados = df.copy()
df_resultados = df_resultados[['ID', 'Age', 'Games', 'Year', 'Season', 'City', 'Sport', 'Event', 'Medal']]
df_resultados.fillna({'Age': 0, 'Medal': ''}, inplace=True)
dicionario_de_resultados = df_resultados.to_dict('index')

def importe_atletas(data):
    print('Cadastrando atletas:')   
    for key in tqdm(data):
        lista_valores = []
        for column in data[key]:
            lista_valores.append(data[key][column])
        atleta = Atleta(name=lista_valores[1],
                        sex=lista_valores[2],
                        height=lista_valores[3],
                        weight=lista_valores[4],
                        team=lista_valores[5],
                        noc=lista_valores[6])
        atleta.save()

def importe_resultados(data):
    print('Cadastrando resultados:')   
    for key in tqdm(data):
        lista_valores = []
        for column in data[key]:
            lista_valores.append(data[key][column])
            
        resultado = Resultado(atleta_id=Atleta.objects.get(id=lista_valores[0]),
                        age=lista_valores[1],
                        # games=lista_valores[2],
                        year=lista_valores[3],
                        season=lista_valores[4],
                        city=lista_valores[5],
                        sport=lista_valores[6],
                        event=lista_valores[7],
                        medal=lista_valores[8])
        resultado.save()

importe_atletas(dicionario_de_atletas)
importe_resultados(dicionario_de_resultados)