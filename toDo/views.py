from django.shortcuts import render
from . models import Task

# Create your views here.


def all_tasks(request):
    tasks = Task.objects.all()
    return render (request, 'todo.html', {'alltasks' : tasks})

def prioritized_tasks(request):
    tasks = Task.objects.all().order_by('priority')
    grouped_tasks = {
        'high_priority' : [],
        'medium_priority' :[],
        'low_priority' : []
    }

    for task in tasks:
        if task.priority == 'high':
            grouped_tasks['high_priority'].append(task)
        elif task.priority == 'medium':
            grouped_tasks['medium_priority'].append(task)
        elif task.priority == 'low':
            grouped_tasks['low_priority'].append(task)

    return render(request, 'todo.html', {'grouped_tasks': grouped_tasks})


def sort_tasks_asc(request):
    tasks_ascending = Task.objects.all().order_by('due_date')
    return render (request, 'todo.html', {'alltasks' : tasks_ascending})

def sort_tasks_desc(request):
    tasks_descending = Task.objects.all().order_by('-due_date')
    return render (request, 'todo.html', {'alltasks' : tasks_descending})