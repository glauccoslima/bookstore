from django.urls import path, include  # Importa funções para definição de URLs
from rest_framework import routers  # Importa o módulo de roteamento do Django REST framework
from order import viewsets  # Importa os viewsets do app 'order'

# Cria um roteador simples para registrar as rotas dos viewsets
router = routers.SimpleRouter()
# Registra o viewset de pedidos com o roteador
# O prefixo da URL será 'order' e o viewset associado é OrderViewSet
router.register(r"order", viewsets.OrderViewSet, basename="order")

# Define as URLs que serão incluídas no projeto
urlpatterns = [
    # Inclui todas as URLs registradas no roteador
    path("", include(router.urls)),
]
