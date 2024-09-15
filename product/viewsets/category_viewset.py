from rest_framework.viewsets import ModelViewSet  # Importa o ModelViewSet do Django REST framework

from product.models import Category  # Importa o modelo Category do app product
from product.serializers.category_serializer import CategorySerializer  # Importa o serializer para Category

# Define o ViewSet para o modelo Category
class CategoryViewSet(ModelViewSet):
    # Define o serializer a ser usado para este ViewSet
    serializer_class = CategorySerializer

    # Método estático para obter o queryset de categorias
    @staticmethod
    def get_queryset():
        # Retorna todas as categorias ordenadas por ID
        return Category.objects.all().order_by("id")
