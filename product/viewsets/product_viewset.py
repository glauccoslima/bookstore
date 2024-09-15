from rest_framework.viewsets import ModelViewSet

from product.models import Product
from product.serializers.product_serializer import ProductSerializer


class ProductViewSet(ModelViewSet):

    serializer_class = ProductSerializer

    @staticmethod
    def get_queryset():
        return Product.objects.all().order_by("id")
