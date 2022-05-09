from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from resultados import views

router = DefaultRouter()
router.register(r'atletas', views.AtletaViewSet, basename='Atletas')
router.register(r'resultados', views.ResultadoViewSet, basename='Resultados')


urlpatterns = [
    path('', include(router.urls))
]
