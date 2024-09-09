from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class Department(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    dept = models.TextField(max_length=20)