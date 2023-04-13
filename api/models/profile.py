from django.db import models

from api.models.user import User


class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE) # Delete profile when user is deleted
  image = models.ImageField(default='default.jpg', upload_to='profile_pics')
