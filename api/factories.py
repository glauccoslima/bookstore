import factory
from django.contrib.auth.models import User
from api.models import Product

# Definição da fábrica para o modelo Product
class ProductFactory(factory.django.DjangoModelFactory):
    # Gera um título aleatório usando o Faker
    title = factory.Faker("pystr")
    # Gera uma descrição aleatória usando o Faker
    description = factory.Faker("pystr")
    # Gera um preço aleatório usando o Faker
    price = factory.Faker("pyint")

    # Meta classe para definir o modelo associado à fábrica
    class Meta:
        # Especifica que a fábrica cria instâncias do modelo Product
        model = Product

# Definição da fábrica para o modelo User
class UserFactory(factory.django.DjangoModelFactory):
    # Gera um nome de usuário aleatório usando o Faker
    username = factory.Faker("pystr")
    # Gera um email aleatório usando o Faker
    email = factory.Faker("pystr")

    # Meta classe para definir o modelo associado à fábrica
    class Meta:
        # Especifica que a fábrica cria instâncias do modelo User
        model = User
