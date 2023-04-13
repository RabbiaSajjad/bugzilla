from django.db.models import IntegerChoices

class UserRole(IntegerChoices):
  ADMIN = 0, 'admin'
  DEVELOPER = 1, 'developer'
  MANAGER = 2, 'manager'
  QA = 3, 'QA'
