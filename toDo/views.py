from django.shortcuts import render

# Create your views here.
def all_tasks(request):
    return render (request, 'todo.html')