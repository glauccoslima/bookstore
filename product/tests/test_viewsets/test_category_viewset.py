import json  # Importa o módulo json para manipulação de dados JSON

from rest_framework.test import APITestCase, APIClient  # Importa classes para testes de API
from rest_framework.views import status  # Importa o módulo de status para verificar códigos de resposta

from django.urls import reverse  # Importa a função reverse para resolver URLs a partir de seus nomes

from product.factories import CategoryFactory  # Importa a fábrica para criar instâncias de Category
from product.models import Category  # Importa o modelo Category

# Define a classe de testes para o ViewSet de Category
class CategoryViewSet(APITestCase):
    client = APIClient()  # Inicializa o cliente de teste da API

    # Configuração inicial para os testes
    def setUp(self):
        # Cria uma instância de Category usando a fábrica
        self.category = CategoryFactory(title="books")

    # Testa a obtenção de todas as categorias
    def test_get_all_category(self):
        # Faz uma requisição GET para a lista de categorias
        response = self.client.get(reverse("category-list", kwargs={"version": "v1"}))

        # Verifica se o status da resposta é 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Carrega os dados da resposta em formato JSON
        category_data = json.loads(response.content)

        # Verifica se o título da primeira categoria na resposta é igual ao título da categoria criada
        self.assertEqual(category_data["results"][0]["title"], self.category.title)

    # Testa a criação de uma nova categoria
    def test_create_category(self):
        # Define os dados da nova categoria em formato JSON
        data = json.dumps(
            {
                "title": "technology",
            }
        )

        # Faz uma requisição POST para criar uma nova categoria
        response = self.client.post(
            reverse("category-list", kwargs={"version": "v1"}),
            data=data,
            content_type="application/json",
        )

        # Verifica se o status da resposta é 201 CREATED
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Obtém a categoria criada a partir do banco de dados
        created_category = Category.objects.get(title="technology")

        # Verifica se o título da categoria criada é igual ao título fornecido
        self.assertEqual(created_category.title, "technology")
