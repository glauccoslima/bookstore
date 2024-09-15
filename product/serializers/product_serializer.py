from rest_framework import serializers  # Importa o módulo serializers do Django REST framework

from product.models.product import Category, Product  # Importa os modelos Category e Product do app product
from product.serializers.category_serializer import CategorySerializer  # Importa o serializer para Category

# Define o serializer para o modelo Product
class ProductSerializer(serializers.ModelSerializer):
    # Serializa as categorias associadas ao produto usando CategorySerializer
    category = CategorySerializer(required=False, many=True)
    # Campo para associar categorias ao produto usando seus IDs
    categories_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), write_only=True, many=True
    )

    # Metadados do serializer
    class Meta:
        model = Product  # Modelo associado ao serializer
        fields = [
            "id",
            "title",
            "description",
            "price",
            "active",
            "category",
            "categories_id",
        ]  # Campos incluídos no serializer

    # Método para criar um novo produto
    @staticmethod  # Indica que este método pode ser convertido em um método estático
    def create(validated_data):
        # Extrai os dados das categorias dos dados validados
        category_data = validated_data.pop("categories_id")

        # Cria uma nova instância de Product
        product = Product.objects.create(**validated_data)
        # Adiciona as categorias ao produto
        for category in category_data:
            product.category.add(category)

        return product
