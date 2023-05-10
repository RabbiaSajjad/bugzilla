from rest_framework import serializers
from api.serializers.user_serializer import UserSerializer

from api.models import Project

class ProjectSerializer(serializers.ModelSerializer):
  manager = UserSerializer(read_only=True)
  developer = UserSerializer(many=True, read_only=True)
  quality_assurance = UserSerializer(many=True, read_only=True)
  class Meta:
    model = Project
    fields = ['id','title', 'details', 'manager', 'developer', 'quality_assurance']

  def get_manager(self, obj):
    manager = obj.manager
    if manager.role == 'manager':
      return UserSerializer(manager).data
    else:
      return None

  def get_developers(self, obj):
    developers = obj.developers.filter(role='developer')
    return UserSerializer(developers, many=True).data
