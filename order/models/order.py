from django.db import models
from django.contrib.auth.models import User
from product.models import Product

# Define o modelo Order para representar um pedido
class Order(models.Model):
    # Campo ManyToMany para associar múltiplos produtos a um pedido
    product = models.ManyToManyField(Product, blank=False)
    # Campo ForeignKey para associar um pedido a um usuário
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Método para representar o objeto Order como uma string
    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
