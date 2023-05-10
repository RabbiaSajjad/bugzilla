from multiprocessing import Manager
from django.db import models

from api.models.project import Project
from api.models.user import User

class Bug(models.Model):
  title = models.CharField(max_length=20)
  details = models.CharField(max_length=100)
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  creator = models.ForeignKey(User, related_name='creators', on_delete=models.DO_NOTHING)
  assignee = models.ManyToManyField(User, related_name='assignees', null=True)
