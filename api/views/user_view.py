from api.serializers.project_serializer import ProjectSerializer
from api.views.base_view import BaseView


class UserView(BaseView):
  def get(self, request, id=None):
    return self._admin(request) or \
           super().get(request,id)

  def post(self, request):
    return self._admin(request) or \
      super().post(request)

  def delete(self, request, id):
    return self._admin(request) or \
      super().delete(request,id)

  def put(self, request, id):
    return self._admin(request) or \
      super().put(request,id)
