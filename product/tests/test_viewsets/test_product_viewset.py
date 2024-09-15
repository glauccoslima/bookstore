import json  # Importa o módulo json para manipulação de dados JSON

from rest_framework.test import APITestCase, APIClient  # Importa classes para testes de API
from rest_framework.views import status  # Importa o módulo de status para verificar códigos de resposta
from rest_framework.authtoken.models import Token  # Importa o modelo Token para autenticação

from django.urls import reverse  # Importa a função reverse para resolver URLs a partir de seus nomes

from product.factories import CategoryFactory, ProductFactory  # Importa as fábricas para criar instâncias de Category e Product
from order.factories import UserFactory  # Importa a fábrica para criar instâncias de User
from product.models import Product  # Importa o modelo Product

# Define a classe de testes para o ViewSet de Product
class TestProductViewSet(APITestCase):
    client = APIClient()  # Inicializa o cliente de teste da API

    # Configuração inicial para os testes
    def setUp(self):
        # Cria um usuário para autenticação nos testes
        self.user = UserFactory()

        # Cria um produto para os testes
        self.product = ProductFactory(
            title="pro controller",
            price=200.00,
        )
        # Cria um token de autenticação para o usuário
        token = Token.objects.create(user=self.user)
        token.save()

    # Testa a obtenção de todos os produtos
    def test_get_all_product(self):
        # Obtém o token de autenticação do usuário
        token = Token.objects.get(user__username=self.user.username)
        # Define as credenciais de autenticação para o cliente de teste
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
        # Faz uma requisição GET para a lista de produtos
        response = self.client.get(reverse("product-list", kwargs={"version": "v1"}))

        # Verifica se o status da resposta é 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Carrega os dados da resposta em formato JSON
        product_data = json.loads(response.content)

        # Verifica se os dados do produto na resposta estão corretos
        self.assertEqual(product_data["results"][0]["title"], self.product.title)
        self.assertEqual(product_data["results"][0]["price"], self.product.price)
        self.assertEqual(product_data["results"][0]["active"], self.product.active)

    # Testa a criação de um novo produto
    def test_create_product(self):
        # Obtém o token de autenticação do usuário
        token = Token.objects.get(user__username=self.user.username)
        # Define as credenciais de autenticação para o cliente de teste
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
        # Cria uma nova categoria para o produto
        category = CategoryFactory()
        # Define os dados do novo produto em formato JSON
        data = json.dumps(
            {"title": "notebook", "price": 800.00, "categories_id": [category.id]}
        )

        # Faz uma requisição POST para criar um novo produto
        response = self.client.post(
            reverse("product-list", kwargs={"version": "v1"}),
            data=data,
            content_type="application/json",
        )

        # Verifica se o status da resposta é 201 CREATED
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Obtém o produto criado a partir do banco de dados
        created_product = Product.objects.get(title="notebook")

        # Verifica se o título e o preço do produto criado estão corretos
        self.assertEqual(created_product.title, "notebook")
        self.assertEqual(created_product.price, 800.00)
