# models.py

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    age = models.IntegerField(null=True, default=0)
    gender = models.CharField(max_length=10, null=True, default='Not Specified')
    address = models.TextField(blank=True, null=True)
    education = models.CharField(max_length=255, blank=True, null=True)
    hobbies = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
