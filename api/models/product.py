from django.db import models

# Definição do modelo Product, que representa um produto na aplicação
class Product(models.Model):
    # Campo para o título do produto, com um limite máximo de 100 caracteres
    title = models.CharField(max_length=100)

    # Campo para a descrição do produto, com um limite máximo de 300 caracteres
    # Este campo é opcional (blank=True) e tem um valor padrão de string vazia (default="")
    description = models.TextField(max_length=300, blank=True, default="")

    # Campo para o preço do produto, que deve ser um número inteiro positivo
    # Este campo é opcional tanto no formulário (blank=True) quanto no banco de dados (null=True)
    price = models.PositiveIntegerField(blank=True, null=True)
