from django.contrib.auth.models import AbstractUser
from django.db import models

from api.models.enumerations.user_role import UserRole

# Create your models here.

class User(AbstractUser):
  username = models.CharField(max_length=10, unique=True)
  email=models.EmailField(unique=True)
  first_name = models.CharField(max_length=10)
  last_name = models.CharField(max_length=10, blank=True, null=True)
  password = models.CharField(max_length=128)
  role = models.PositiveSmallIntegerField(choices=UserRole.choices, default=UserRole.DEVELOPER)
