from django.urls import path
from . import views

app_name = "userApp"

urlpatterns=[
    path('',views.index,name='index'),
    path('shared_notes/',views.shared_notes, name="sharedNotes"),
    path('shared_tutorials/',views.shared_tutorials, name="sharedTutorials"),
    path('view_note/<int:note_id>/',views.view_note, name="viewNote"),
    path('user/',views.user_index, name="userIndex"),
]