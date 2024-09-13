import pytest
from api.models import User

# Marca o teste para usar o banco de dados do Django
@pytest.mark.django_db
def test_create_user():
    # Cria um novo usuário com os dados fornecidos
    user = User.objects.create(
        email="test@example.com",
        username="testuser",
        user_pass="password123",
        first_name="Test",
        last_name="User",
        country="Brasil",
        state="SP",
        city="São Paulo",
        postal_code="12345-678",
        address="Rua A, 123",
    )

    # Verifica se os campos do usuário criado correspondem aos dados fornecidos
    assert user.username == "testuser"
    assert user.first_name == "Test"
    assert user.country == "Brasil"
    # Verifica se o usuário criado possui um ID (foi salvo no banco de dados)
    assert user.id is not None
