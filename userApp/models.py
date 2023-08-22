from typing import Optional
from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager

# Create your models here.
class CustomUserManager(UserManager):
    def get_by_natural_key(self, username):
        # case_insensitive_username_field = '{}__iexact'.format(self.model.USERNAME_FIELD)
        # return self.get(**{case_insensitive_username_field: username})
        return self.get(**{self.model.USERNAME_FIELD + '__iexact': username})

class User(AbstractUser):
    objects = CustomUserManager()

    def __str__(self):
        return self.username