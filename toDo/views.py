from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from . models import Task
from .forms import TaskForm

# Create your views here.
def add_task(request,userName):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.instance.owner = request.user
            form.save()
    return redirect('toDo:allTasks', userName=request.user.username)




def edit_task(request,task_id):
    task = get_object_or_404(Task, pk=task_id)
    # form = TaskForm(request.POST or None, instance =task)
    # if form.is_valid():
    #     form.instance.owner = request.user
    #     form.save()
    #     return redirect('toDo:allTasks', userName=request.user.username)
    # else:
    form = TaskForm(instance=task)
    passvalue = [1,2,3,4,5]
    print(form)
    return JsonResponse (passvalue, safe=False)
    # return redirect('toDo:allTasks', userName=request.user.username, form=form)





def all_tasks(request,userName):
    current_user = request.user
    tasks = Task.objects.filter(owner=current_user)
    form = TaskForm()
    return render (request, 'todo.html', {'alltasks' : tasks,'form':form})

def prioritized_tasks(request,userName):
    current_user = request.user
    tasks = Task.objects.filter(owner=current_user).order_by('priority')
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
        form = TaskForm()

    return render(request, 'todo.html', {'grouped_tasks': grouped_tasks, 'form':form})


def sort_tasks_asc(request,userName):
    current_user = request.user
    tasks_ascending = Task.objects.filter(owner=current_user).order_by('due_date')
    form = TaskForm()
    return render (request, 'todo.html', {'alltasks' : tasks_ascending, 'form':form})

def sort_tasks_desc(request,userName):
    current_user = request.user
    tasks_descending = Task.objects.filter(owner=current_user).order_by('-due_date')
    form = TaskForm()
    return render (request, 'todo.html', {'alltasks' : tasks_descending, 'form':form})