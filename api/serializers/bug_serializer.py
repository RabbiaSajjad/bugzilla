from rest_framework import serializers

from api.models import Bug

class BugSerializer(serializers.ModelSerializer):
  class Meta:
    model = Bug
    fields = ['id','title', 'details', 'project', 'creator', 'assignee']
