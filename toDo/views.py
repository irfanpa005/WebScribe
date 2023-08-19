from django.shortcuts import render
from . models import Task

# Create your views here.
def all_tasks(request):
    tasks = Task.objects.all()
    return render (request, 'todo.html', {'tasks' : tasks})