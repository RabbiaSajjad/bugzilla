from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer

from api.models import User

class UserSerializer(BaseUserCreateSerializer):
  class Meta(BaseUserCreateSerializer.Meta):
    model = User
    fields = ['id', 'username','email', 'first_name', 'last_name', 'password', 'role']
