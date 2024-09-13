from rest_framework import serializers
from api.models.user import User

# Definição do serializer para o modelo User
class UserSerializer(serializers.ModelSerializer):
    # Meta classe para definir o comportamento do serializer
    class Meta:
        # Especifica o modelo que será serializado
        model = User
        # Inclui todos os campos do modelo no serializer
        fields = '__all__'
