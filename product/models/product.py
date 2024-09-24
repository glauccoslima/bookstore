from django.db import models  # Importa o módulo models do Django para definição de modelos
from product.models import Category  # Importa o modelo Category do app product

# Define o modelo Product para representar um produto
class Product(models.Model):
    # Campo title para o título do produto, com limite de 100 caracteres
    title = models.CharField(max_length=100)
    # Campo description para a descrição do produto, com limite de 500 caracteres, pode ser vazio
    description = models.TextField(max_length=500, blank=True, default="Descrição padrão")  # Adicione default para registros existentes
    # Campo price para o preço do produto, deve ser um inteiro positivo, pode ser vazio ou nulo
    price = models.PositiveIntegerField(blank=True, null=True)
    # Campo active para indicar se o produto está ativo, padrão é True
    active = models.BooleanField(default=True)
    # Campo category para associar o produto a múltiplas categorias, pode ser vazio
    category = models.ManyToManyField(Category, blank=True)

    # Método para representar o objeto Product como uma string
    def __str__(self):
        return self.title
