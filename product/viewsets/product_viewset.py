from rest_framework.viewsets import ModelViewSet  # Importa o ModelViewSet do Django REST framework

from product.models import Product  # Importa o modelo Product do app product
from product.serializers.product_serializer import ProductSerializer  # Importa o serializer para Product

# Define o ViewSet para o modelo Product
class ProductViewSet(ModelViewSet):
    # Define o serializer a ser usado para este ViewSet
    serializer_class = ProductSerializer

    # Método estático para obter o queryset de produtos
    @staticmethod
    def get_queryset():
        # Retorna todos os produtos ordenados por ID
        return Product.objects.all().order_by("id")
