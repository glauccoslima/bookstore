from django.urls import path, include  # Importa funções para definição de URLs e inclusão de outras configurações de URL
from rest_framework import routers  # Importa o módulo de roteamento do Django REST framework

from product import viewsets  # Importa os viewsets do app 'product'

# Cria um roteador simples para registrar as rotas dos viewsets
router = routers.SimpleRouter()
# Registra o viewset de produtos com o roteador
# O prefixo da URL será 'product' e o viewset associado é ProductViewSet
router.register(r"product", viewsets.ProductViewSet, basename="product")
# Registra o viewset de categorias com o roteador
# O prefixo da URL será 'category' e o viewset associado é CategoryViewSet
router.register(r"category", viewsets.CategoryViewSet, basename="category")

# Define as URLs que serão incluídas no projeto
urlpatterns = [
    # Inclui todas as URLs registradas no roteador
    path("", include(router.urls)),
]
