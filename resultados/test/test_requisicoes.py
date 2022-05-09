from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from resultados.models import Atleta


class AtletasTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Atletas-list')

        self.atleta_1 = Atleta.objects.create(
            name='Yuri Kuvjogi Fernandes',
            sex='M',
            height=170,
            weight=70,
            team='Cross',
            noc='Ant',
        )
        
        self.atleta_2 = Atleta.objects.create(
            name='Roberto Carlos',
            sex='M',
            height=145,
            weight=120,
            team='Cross',
            noc='Ant',
        )

    def test_requisicao_para_listar_atletas(self):
        '''Teste para verificar GET de lista de atletas'''
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_criar_atlet(self):
        '''Teste para verificar POST para criar um atleta'''
        
        data = {
            'name': 'Adriano da Cruz',
            'sex': 'M',
            'height': 140,
            'weight': 60,
            'team': 'Cross',
            'noc': 'Ant'
        }

        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_deletar_resultado(self):
        '''Teste para verificar DELETE de resultado'''

        response = self.client.delete('/atletas/1/')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_requisicao_atualizar_resultado(self):
        '''Teste para verificar PUT para atualizar resultado'''

        data = {
            'name': 'Yuri Kuvjogi Fernandes',
            'sex': 'M',
            'height': 170,
            'weight': 65,
            'team': 'Summer',
            'noc': 'Ant',
        }

        response = self.client.put('/atletas/1/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
