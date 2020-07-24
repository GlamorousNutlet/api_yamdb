from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    role = models.CharField(max_length=30, blank=True)
    confirmation_code = models.CharField(max_length=10, blank=True)
