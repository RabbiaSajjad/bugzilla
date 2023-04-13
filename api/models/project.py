from django.db import models

from api.models.user import User

class Project(models.Model):
  title = models.CharField(max_length=20)
  details = models.CharField(max_length=100)
  manager = models.ForeignKey(User, on_delete=models.CASCADE)
  developer = models.ManyToManyField(User, related_name="project_developer", null=True)
  quality_assurance = models.ManyToManyField(User, related_name="project_qa", null=True)
