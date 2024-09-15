import json

from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token

from django.urls import reverse

from product.factories import CategoryFactory, ProductFactory
from order.factories import UserFactory, OrderFactory

from order.models import Order


class TestOrderViewSet(APITestCase):

    client = APIClient()

    def setUp(self):
        # Cria uma categoria de produto para os testes
        self.category = CategoryFactory(title="technology")
        # Cria um produto associado à categoria criada
        self.product = ProductFactory(
            title="mouse", price=100, category=[self.category]
        )
        # Cria um pedido associado ao produto criado
        self.order = OrderFactory(product=[self.product])
        # Cria um usuário para autenticação nos testes
        self.user = UserFactory()
        # Cria um token de autenticação para o usuário
        token = Token.objects.create(user=self.user)
        token.save()

    def test_order(self):
        # Obtém o token de autenticação do usuário
        token = Token.objects.get(user__username=self.user.username)
        # Define as credenciais de autenticação para o cliente de teste
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
        # Faz uma requisição GET para a lista de pedidos
        response = self.client.get(reverse("order-list", kwargs={"version": "v1"}))

        # Verifica se o status da resposta é 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Carrega os dados da resposta em formato JSON
        order_data = json.loads(response.content)
        # Verifica se os dados do produto no pedido estão corretos
        self.assertEqual(
            order_data["results"][0]["product"][0]["title"], self.product.title
        )
        self.assertEqual(
            order_data["results"][0]["product"][0]["price"], self.product.price
        )
        self.assertEqual(
            order_data["results"][0]["product"][0]["active"], self.product.active
        )
        self.assertEqual(
            order_data["results"][0]["product"][0]["category"][0]["title"],
            self.category.title,
        )

    def test_create_order(self):
        # Obtém o token de autenticação do usuário
        token = Token.objects.get(user__username=self.user.username)
        # Define as credenciais de autenticação para o cliente de teste
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
        # Cria um novo produto para o pedido
        product = ProductFactory()
        # Define os dados do novo pedido em formato JSON
        data = json.dumps({"product_id": [product.id], "user": self.user.id})

        # Faz uma requisição POST para criar um novo pedido
        response = self.client.post(
            reverse("order-list", kwargs={"version": "v1"}),
            data=data,
            content_type="application/json",
        )

        # Verifica se o status da resposta é 201 CREATED
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verifica se o pedido foi criado corretamente no banco de dados
        self.assertTrue(Order.objects.filter(user=self.user).exists())
