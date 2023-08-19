from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('',views.notes,name="notes"),
    path('create/', views.create_note, name='create_note'),
    path('note_display/<int:note_id>/', views.note_display, name='note_display'),
    path('user/search/', views.user_note_search, name='userNoteSearch'),
    path('tutorials/', views.tutorials, name='tutorials'),
]

