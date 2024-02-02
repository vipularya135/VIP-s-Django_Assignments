# django_app/models.py
import uuid
from django.db import models
from django.contrib.auth.models import User

class UserDetails(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=True, blank=True, default='Not Specified')
    age = models.IntegerField(blank=True, null=True, default=0)
    gender = models.CharField(max_length=255, null=True, default='Not Specified', blank=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class UserQualifications(models.Model):
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    education = models.CharField(max_length=255, blank=True, null=True, default='Not Specified')
    hobbies = models.TextField(blank=True, null=True, default='Not Specified')

    def __str__(self):
        return f"Qualifications for {self.user_details.name}"
