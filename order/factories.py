import factory
from django.contrib.auth.models import User
from order.models import Order

# Fábrica para criar instâncias do modelo User
class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Faker("pystr")  # Gera um email aleatório usando o Faker
    username = factory.Faker("pystr")  # Gera um nome de usuário aleatório usando o Faker

    class Meta:
        model = User  # Define o modelo associado a esta fábrica

# Fábrica para criar instâncias do modelo Order
class OrderFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)  # Associa um usuário à ordem usando a UserFactory

    @factory.post_generation
    def product(self, create, extracted, **kwargs):
        # Verifica se a instância está sendo criada
        if not create:
            return

        # Se produtos foram extraídos, adiciona-os à ordem
        if extracted:
            for product in extracted:
                self.product.add(product)  # Adiciona produtos à ordem após a criação

    class Meta:
        model = Order  # Define o modelo associado a esta fábrica
        skip_postgeneration_save = True  # Evita salvar automaticamente após hooks
