from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    your_role = (
        ('user', 'Аутентифицированный пользователь'),
        ('moderator', 'Модератор '),
        ('admin', 'Администратор '),
        ('django_adm', 'Администратор Django'),
        ('AnonymousUser', 'Неизвестный')
    )
    bio = models.TextField(max_length=500, blank=True)
    role = models.CharField(max_length=500, choices=your_role, default='user')
    confirmation_code = models.CharField(max_length=10, blank=True)
    token = models.CharField(max_length=30, blank=True)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)

    # USERNAME_FIELD = 'email'

