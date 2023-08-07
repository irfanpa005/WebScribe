from django.db import models
from ckeditor.fields import RichTextField
from userApp.models import User
from django.utils import timezone


# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    created_at = models.DateField(default=timezone.now)
    noteowner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='allNote')
    is_shared = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    
class Tutorial(models.Model):
    title = models.CharField(max_length=200)
    short_descr = models.CharField(max_length=200,blank=True)
    link = models.URLField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='allTutorials')
    is_shared = models.BooleanField(default=False)
    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title