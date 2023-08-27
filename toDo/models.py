import datetime
from django.db import models
from userApp.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator
# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    details = models.CharField(max_length=255,null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='allTasks')
    is_Active = models.BooleanField(default=True)
    created_at = models.DateField(default=timezone.now)
    due_date = models.DateField(null=False, default=None,validators=[MinValueValidator(limit_value=timezone.now().date())])
    priority = models.CharField(
        max_length=32,
        choices=[
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
        ],
    )

    def __str__(self):
        return self.title
    
    def remaining_days(self):
        if self.due_date:
            today = timezone.now().date()
            remaining_days = (self.due_date - today).days
            return remaining_days
        else:
            return None
