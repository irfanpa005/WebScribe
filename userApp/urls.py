from django.urls import path,include
from . import views
from django.contrib.auth.decorators import login_required

app_name = "userApp"

urlpatterns=[
    path('',views.index,name='index'),
    path('index/login',views.index_login,name='indexLogin'),
    path('registration/',views.registration,name='registration'),
    path('google/redirect', login_required(views.google_redirect), name='google_redirect'),
    path('logout/',views.logout_user,name="logout"),
    path('shared_notes/',views.shared_notes, name="sharedNotes"),
    path('shared_tutorials/',views.shared_tutorials, name="sharedTutorials"),
    path('view_note/<int:note_id>/',views.view_note, name="viewNote"),
    path('shared_notes/<str:userName>/',views.user_shared_notes, name="userSharedNotes"),
    path('shared_tutorials/<str:userName>/',views.user_shared_tutorials, name="userSharedTutorials"),

]