from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status

from api.serializers.bug_serializer import BugSerializer
from api.views.base_view import BaseView


class BugView(BaseView):
  def get(self, request, id=None):
    return super().get(request,id)

  def post(self, request):
    return super().post(request)

  def delete(self, request, id):
    return super().delete(request,id)

  def put(self, request, id):
    return super().put(request,id)

