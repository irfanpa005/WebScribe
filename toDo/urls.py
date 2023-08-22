from django.urls import path
from . import views

app_name = "toDo"

urlpatterns = [
    path('<str:userName>',views.all_tasks, name='allTasks'),
    path('prioritized_tasks/<str:userName>',views.prioritized_tasks,name='groupedTasks'),
    path('sort_tasks_asc/<str:userName>',views.sort_tasks_asc,name='sortTaskAsc'),
    path('sort_tasks_desc/<str:userName>',views.sort_tasks_desc,name='sortTaskDesc'),


]

