from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('all_notes/<str:userName>',views.notes,name="notes"),
    path('create/', views.create_note, name='create_note'),
    path('note_display/<int:note_id>/', views.note_display, name='note_display'),
    path('edit_note/<int:note_id>/', views.edit_note, name='editNote'),
    path('delete_note/<int:note_id>/', views.delete_note, name='deleteNote'),
    path('user/search/', views.user_note_search, name='userNoteSearch'),
    path('notesharestatus/<int:note_id>',views.note_share_status,name='noteShareStatus'),

    path('tutorials/<str:userName>/', views.tutorials, name='tutorials'),
    path('add_tutorial/<str:userName>/',views.add_tutorial,name='addTutorial'),
    path('edit_tutorial/<int:tuto_id>',views.edit_tutorial,name='editTutorial'),
    path('delete_tutorial/<int:tuto_id>',views.delete_tutorial,name='deleteTutorial'),
    path('search_tutorial/',views.user_search_tutorial,name='searchTutorial'),
    path('tutorial_sharestatus/<int:tuto_id>',views.tutorial_share_status,name='tutoShareStatus'),
    
]

