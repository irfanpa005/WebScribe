from django.db import models
from userApp.models import User
from django.utils import timezone
# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='allTasks')
    is_Active = models.BooleanField()
    created_at = models.DateField(default=timezone.now)
    priority = models.CharField(
        max_length=32,
        choices=[
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
        ],
    )
