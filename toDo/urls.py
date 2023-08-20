from django.urls import path
from . import views

app_name = "toDo"

urlpatterns = [
    path('',views.all_tasks, name='allTasks'),
    path('prioritized_tasks/',views.prioritized_tasks,name='groupedTasks'),
    path('sort_tasks_asc/',views.sort_tasks_asc,name='sortTaskAsc'),
    path('sort_tasks_desc/',views.sort_tasks_desc,name='sortTaskDesc'),


]

