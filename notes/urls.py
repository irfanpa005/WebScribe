from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('<str:userName>',views.notes,name="notes"),
    path('create/', views.create_note, name='create_note'),
    path('note_display/<int:note_id>/', views.note_display, name='note_display'),
    path('edit_note/<int:note_id>/', views.edit_note, name='editNote'),
    path('delete_note/<int:note_id>/', views.delete_note, name='deleteNote'),
    path('user/search/', views.user_note_search, name='userNoteSearch'),
    path('tutorials/', views.tutorials, name='tutorials'),
    path('notesharestatus/<int:note_id>',views.note_share_status,name='noteShareStatus')
]

