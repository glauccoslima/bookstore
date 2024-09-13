from rest_framework import serializers
from api.models.product import Product

# Definição do serializer para o modelo Product
class ProductSerializer(serializers.ModelSerializer):
    # Meta classe para definir o comportamento do serializer
    class Meta:
        # Especifica o modelo que será serializado
        model = Product
        # Inclui todos os campos do modelo no serializer
        fields = '__all__'
