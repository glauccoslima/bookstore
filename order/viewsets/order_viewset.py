from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication,
    TokenAuthentication,
)
from rest_framework.permissions import IsAuthenticated

from order.models import Order
from order.serializers import OrderSerializer

# ViewSet para o modelo Order
class OrderViewSet(ModelViewSet):
    # Define as classes de autenticação permitidas
    authentication_classes = [
        SessionAuthentication,  # Autenticação de sessão
        BasicAuthentication,  # Autenticação básica
        TokenAuthentication,  # Autenticação por token de acesso
    ]
    # Define as permissões necessárias para acessar o ViewSet
    permission_classes = [IsAuthenticated]  # Requer que o usuário esteja autenticado

    # Define o serializer a ser usado para este ViewSet
    serializer_class = OrderSerializer
    # Define o queryset padrão para este ViewSet, ordenado por ID
    queryset = Order.objects.all().order_by("id")
