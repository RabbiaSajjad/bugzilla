import resource
from django.http import HttpResponse
from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist
from api.models import Bug, Project

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from inflect import engine
from rest_framework import status
import re as regex

from api.models.factories.serializer import serializer
# from api.utils.error_responses import not_found_response, unauthenticated_response, \
#                                       unauthorized_response, unprocessable_entity_response, object_already_exists, cannot_update_this_entity

class BaseView(APIView, LimitOffsetPagination):

  def get(self, request, id=None):
    if id:
      resource=self._find_resource(id)
      return Response({ self._model_name: serializer(self._model_name, resource).data })
    else:
      attribute_value = request.GET.get('role')
      data=self._model.objects.all()
      if self._model==Project:
        data=data.prefetch_related('developer', 'quality_assurance')
      if attribute_value:
        data = data.filter(role=attribute_value)
      db_data = serializer(self._model_name, self.paginate_queryset(data, request, view=self), many=True)
      return Response({ engine().plural(self._model_name): self.get_paginated_response(db_data.data).data })

  def delete(self, request, id):
    try:
      resource=self._find_resource(id)
      resource.delete()
      return Response({"message":"Resource deleted successfully" })
    except ObjectDoesNotExist:
      pass

  def post(self, request, id=None):
    return self._save_resource(serializer(self._model_name,data=request.data), request, status.HTTP_201_CREATED)

  def put(self, request, id):
    resource=self._find_resource(id)
    import pdb;
    pdb.set_trace()
    if resource:
      return self._save_resource(serializer(self._model_name,resource,data=request.data, partial=True), request)

  def _find_resource(self, id):
    try:
      return self._model.objects.get(id=id)
    except ObjectDoesNotExist:
      pass

  def _save_resource(self, resource, request, success_status=status.HTTP_200_OK):
    if resource.is_valid():
      resource.save()
      return Response({ engine().plural(self._model_name): resource.data, "message": "Resource saved successfully" }, status=success_status)
    import pdb;
    pdb.set_trace()
    print(resource.errors)
    return HttpResponse("Uprocessable entity")

  def _authenticate(self, request):
    if not request.user.is_authenticated:
      return Response({ 'errors': { 'user': ['Login required to perform this action.'] } }, status=status.HTTP_401_UNAUTHORIZED)

  def _developer(self, request):
    if not request.user.role == 1:
      return Response({ 'errors': { 'user': ['You are unauthorized to perform this action.'] } }, status=status.HTTP_403_FORBIDDEN)

  def _manager(self, request):
    if not request.user.role == 2:
      return Response({ 'errors': { 'user': ['You are unauthorized to perform this action.'] } }, status=status.HTTP_403_FORBIDDEN)

  def _qa(self, request):
    if not request.user.role == 3:
      return Response({ 'errors': { 'user': ['You are unauthorized to perform this action.'] } }, status=status.HTTP_403_FORBIDDEN)

  def _admin(self, request):
    if not request.user.role == 0:
      return Response({ 'errors': { 'user': ['You are unauthorized to perform this action.'] } }, status=status.HTTP_403_FORBIDDEN)

  def _check_owner(self, model, user_id, resource_id):
    if model == 'bug':
      resource = Bug.objects.filter(creator_id=user_id, id=resource_id)
    elif model == 'project':
      resource = Project.objects.filter(manager_id=user_id, id=resource_id)
    if not resource:
      return Response({ 'errors': { 'user': ['You are unauthorized to perform this action.'] } }, status=status.HTTP_403_FORBIDDEN)

  def _owner(self, request, id):
    return self._check_owner(self._model_name, request.user.id, id)


  @property
  def _model(self):
    return apps.get_model('api', self._model_class_name, require_ready=True)
    # return eval(self._model_class_name)

  @property
  def _model_class_name(self):
    return type(self).__name__.replace('View', '')

  @property
  def _model_name(self):
    name = regex.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', self._model_class_name)
    return regex.sub(r'([a-z0-9])([A-Z])', r'\1_\2', name).lower()
    # return camel_to_snake(self._model_class_name)

