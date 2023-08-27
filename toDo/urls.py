from django.urls import path
from . import views

app_name = "toDo"

urlpatterns = [
    path('add_task/<str:userName>',views.add_task, name='addTask'),
    path('edit_task/<int:task_id>',views.edit_task, name='editTask'),
    path('delete_task/<int:task_id>',views.delete_task, name='deleteTask'),
    path('alltasks/<str:userName>',views.all_tasks, name='allTasks'),
    path('prioritized_tasks/<str:userName>',views.prioritized_tasks,name='groupedTasks'),
    path('sort_tasks_asc/<str:userName>',views.sort_tasks_asc,name='sortTaskAsc'),
    path('sort_tasks_desc/<str:userName>',views.sort_tasks_desc,name='sortTaskDesc'),



]

