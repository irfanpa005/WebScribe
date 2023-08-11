from django.urls import path
from . import views

app_name = "toDo"

urlpatterns = [
    path('',views.all_tasks, name='allTasks'),
]

