# five/models.py

from django.db import models
from django.contrib.auth.models import User

class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='Default Name')
    age = models.IntegerField(default=0)  # Add a default value for age
    gender = models.CharField(max_length=10, blank=True)  # Allow blank for gender

    def __str__(self):
        return self.name

class UserQualifications(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    education = models.CharField(max_length=100, default='', blank=True)  # Add a default value for education
    hobbies = models.TextField(default='', blank=True)  # Add a default value for hobbies

    def __str__(self):
        return f"{self.user.username}'s Qualifications"
