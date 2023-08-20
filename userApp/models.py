from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username