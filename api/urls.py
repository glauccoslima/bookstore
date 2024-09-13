from django.urls import path, include
from rest_framework import routers
from api import viewsets

# Cria um roteador simples para registrar as rotas dos viewsets
router = routers.SimpleRouter()
# Registra o viewset de produtos com o roteador
# O prefixo da URL será 'product' e o viewset associado é ProductViewSet
router.register(r'product', viewsets.ProductViewSet, basename='product')

# Define as URLs que serão incluídas no projeto
urlpatterns = [
    # Inclui todas as URLs registradas no roteador
    path('', include(router.urls))
]
