from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status

from api.serializers.project_serializer import ProjectSerializer
from api.views.base_view import BaseView


class ProjectView(BaseView):
  def get(self, request, id=None):
    return self._authenticate(request) or \
        self._manager(request) or \
        super().get(request,id)

  def post(self, request):
    return self._authenticate(request) or \
      self._manager(request) or \
      super().post(request)

  def delete(self, request, id):
    return self._authenticate(request) or \
      self._manager(request) or \
      self._owner(request, id) or \
      super().delete(request,id)

  def put(self, request, id):
    return self._authenticate(request) or \
      self._manager(request) or \
      self._owner(request, id) or \
      super().put(request,id)

