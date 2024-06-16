from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager  # Import vášho vlastného manažéra

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = None  # Odstránenie poľa username

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()  # Pridanie vlastného manažéra
