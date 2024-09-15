import factory  # Importa o módulo factory_boy para criação de objetos de teste
from product.models import Product, Category  # Importa os modelos Product e Category do app product

# Define a fábrica para criar instâncias do modelo Category
class CategoryFactory(factory.django.DjangoModelFactory):
    # Gera um título aleatório usando o Faker
    title = factory.Faker("pystr")
    # Gera um slug aleatório usando o Faker
    slug = factory.Faker("pystr")
    # Gera uma descrição aleatória usando o Faker
    description = factory.Faker("pystr")
    # Define o campo active com valores alternados entre True e False
    active = factory.Iterator([True, False])

    # Metadados da fábrica
    class Meta:
        model = Category  # Define o modelo associado a esta fábrica
        skip_postgeneration_save = True  # Evita salvar automaticamente após hooks

# Define a fábrica para criar instâncias do modelo Product
class ProductFactory(factory.django.DjangoModelFactory):
    # Gera um preço aleatório usando o Faker
    price = factory.Faker("pyint")
    # Gera um título aleatório usando o Faker
    title = factory.Faker("pystr")

    # Método para adicionar categorias ao produto após a criação
    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        # Verifica se a instância está sendo criada
        if not create:
            return

        # Se categorias foram extraídas, adiciona-as ao produto
        if extracted:
            for category in extracted:
                self.category.add(category)

    # Metadados da fábrica
    class Meta:
        model = Product  # Define o modelo associado a esta fábrica
        skip_postgeneration_save = True  # Evita salvar automaticamente após hooks
