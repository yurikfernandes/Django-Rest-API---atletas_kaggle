from django.contrib import admin
from django.urls import path, include

from resultados import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'atletas', views.AtletaViewSet, basename='Atletas')

urlpatterns = [
    path('', include(router.urls))
]
