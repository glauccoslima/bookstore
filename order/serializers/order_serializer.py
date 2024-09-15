from rest_framework import serializers
from order.models import Order
from product.models import Product
from product.serializers.product_serializer import ProductSerializer

# Serializer para o modelo Order
class OrderSerializer(serializers.ModelSerializer):
    # Serializa os produtos associados ao pedido usando ProductSerializer
    product = ProductSerializer(required=False, many=True)
    # Campo para associar produtos ao pedido usando seus IDs
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), write_only=True, many=True
    )
    # Campo para calcular o total do pedido
    total = serializers.SerializerMethodField()

    # Método estático para calcular o total do pedido
    @staticmethod
    def get_total(instance):
        # Usando um gerador em vez de uma lista para calcular o total
        total = sum(product.price for product in instance.product.all())
        return total

    # Metadados do serializer
    class Meta:
        model = Order  # Modelo associado ao serializer
        fields = ["product", "total", "user", "product_id"]  # Campos incluídos no serializer
        extra_kwargs = {"product": {"required": False}}  # Define que o campo product não é obrigatório

    # Método estático para criar um pedido
    @staticmethod
    def create(validated_data):
        # Extrai os dados dos produtos e do usuário dos dados validados
        product_data = validated_data.pop("product_id")
        user_data = validated_data.pop("user")

        # Cria uma nova instância de Order
        order = Order.objects.create(user=user_data)
        # Adiciona os produtos ao pedido
        for product in product_data:
            order.product.add(product)

        return order
