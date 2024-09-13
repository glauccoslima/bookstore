import pytest
from api.models import Product

# Marca o teste para usar o banco de dados do Django
@pytest.mark.django_db
def test_create_product():
    # Cria um novo produto com os dados fornecidos
    product = Product.objects.create(
        title="Titulo teste do produto",
        description="Descrição de teste",
        price=999
    )

    # Verifica se os campos do produto criado correspondem aos dados fornecidos
    assert product.title == "Titulo teste do produto"
    assert product.description == "Descrição de teste"
    assert product.price == 999
    # Verifica se o produto criado possui um ID (foi salvo no banco de dados)
    assert product.id is not None
