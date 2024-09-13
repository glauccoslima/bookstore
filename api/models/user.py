from django.db import models

# Definição do modelo User, que representa um usuário na aplicação
class User(models.Model):
    # Campo para o email do usuário, com um limite máximo de 50 caracteres
    email = models.CharField(max_length=50)

    # Campo para o nome de usuário, com um limite máximo de 20 caracteres
    username = models.CharField(max_length=20)

    # Campo para a senha do usuário, com um limite máximo de 20 caracteres
    user_pass = models.CharField(max_length=20)

    # Campo para o primeiro nome do usuário, com um limite máximo de 30 caracteres
    first_name = models.CharField(max_length=30)

    # Campo para o sobrenome do usuário, com um limite máximo de 30 caracteres
    last_name = models.CharField(max_length=30)

    # Campo para o país do usuário, com um limite máximo de 40 caracteres
    country = models.CharField(max_length=40)

    # Campo para o estado do usuário, com um limite máximo de 40 caracteres
    state = models.CharField(max_length=40)

    # Campo para a cidade do usuário, com um limite máximo de 60 caracteres
    city = models.CharField(max_length=60)

    # Campo para o código postal do usuário, com um limite máximo de 12 caracteres
    postal_code = models.CharField(max_length=12)

    # Campo para o endereço do usuário, sem limite de caracteres
    address = models.TextField()

    # Campo para o segundo endereço do usuário, opcional (blank=True) e com valor padrão de string vazia (default="")
    address_2 = models.TextField(blank=True, default="")
