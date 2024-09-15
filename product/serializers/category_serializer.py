from rest_framework import serializers  # Importa o módulo serializers do Django REST framework

from product.models.category import Category  # Importa o modelo Category do app product

# Define o serializer para o modelo Category
class CategorySerializer(serializers.ModelSerializer):
    # Metadados do serializer
    class Meta:
        model = Category  # Modelo associado ao serializer
        fields = [
            "title",  # Campo para o título da categoria
            "slug",  # Campo para o slug da categoria
            "description",  # Campo para a descrição da categoria
            "active",  # Campo para indicar se a categoria está ativa
        ]  # Campos incluídos no serializer
        extra_kwargs = {"slug": {"required": False}}  # Define que o campo slug não é obrigatório
