from django.db import models  # Importa o módulo models do Django para definição de modelos


# Define o modelo Category para representar uma categoria de produtos
class Category(models.Model):
    # Campo title para o título da categoria, com limite de 100 caracteres
    title = models.CharField(max_length=100)
    # Campo slug para o slug da categoria, deve ser único
    slug = models.SlugField(unique=True)
    # Campo description para a descrição da categoria, pode ser vazio mas não nulo
    description = models.CharField(max_length=200, blank=True)  # Remover null=True para evitar inconsistência
    # Campo active para indicar se a categoria está ativa, padrão é True
    active = models.BooleanField(default=True)

    # Método para representar o objeto Category como uma string
    def __unicode__(self):
        return self.title
