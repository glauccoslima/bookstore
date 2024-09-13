import pytest
from api.serializers import ProductSerializer

# Marca o teste para usar o banco de dados do Django
@pytest.mark.django_db
def test_product_serializer():
    # Dados de exemplo para testar o serializer
    data = {
        "title": "Teste serializer",
        "description": "Testando o serializer",
        "price": 999
    }

    # Testando a deserialização (entrada de dados no serializer)
    serializer = ProductSerializer(data=data)
    # Verifica se os dados são válidos de acordo com o serializer
    assert serializer.is_valid(), f"Erros: {serializer.errors}"
    # Salva o objeto deserializado no banco de dados
    product = serializer.save()

    # Verifica se os dados deserializados correspondem aos dados de entrada
    assert product.title == data["title"]
    assert product.description == data["description"]
    assert product.price == data["price"]

    # Testando a serialização (conversão do objeto para dados JSON)
    serializer = ProductSerializer(product)
    serialized_data = serializer.data

    # Verifica se os dados serializados correspondem aos dados do objeto
    assert serialized_data["title"] == data["title"]
    assert serialized_data["description"] == data["description"]
    assert serialized_data["price"] == data["price"]
