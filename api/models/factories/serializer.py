
from api.serializers.user_serializer import UserSerializer
from api.serializers.project_serializer import ProjectSerializer
from api.serializers.bug_serializer import BugSerializer

def serializer(model, *args, **params):
  if model == 'user':
    return UserSerializer(*args, **params)
  elif model == 'project':
    return ProjectSerializer(*args, **params)
  elif model == 'bug':
    return BugSerializer(*args, **params)
