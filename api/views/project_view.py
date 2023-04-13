from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status

from api.serializers.project_serializer import ProjectSerializer
from api.views.base_view import BaseView


class ProjectView(BaseView):
  def get(self, request, id=None):
    return super().get(request,id)

  def post(self, request):
    return super().post(request)

  def delete(self, request, id):
    return super().delete(request,id)

  def put(self, request, id):
    return super().put(request,id)

