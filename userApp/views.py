from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import login,logout, authenticate
from django.urls import reverse
from notes.models import Note,Tutorial, User
from django.core.paginator import Paginator
from .forms import RegistrationForm
from django.contrib import messages


# Create your views here.
def index(request):
    notes = Note.objects.filter(is_shared=True).order_by('-created_at')
    paginator_n = Paginator(notes,3)
    page_no_n = request.GET.get('page')
    single_page_notes = paginator_n.get_page(page_no_n)

    tutorials = Tutorial.objects.filter(is_shared=True).order_by('-created_at')
    paginator_t = Paginator(tutorials,3)
    page_no_t = request.GET.get('page')
    single_page_tutorials = paginator_t.get_page(page_no_t)

    return render(request, 'index.html',{'notes':single_page_notes, 'tutorials' :single_page_tutorials})


def registration(request):
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
    if password != confirmation:
        messages.error(request, "! Password missmatch.")
        return redirect("userApp:index")
    try:
        user = User.objects.create_user(username, email, password)
        user.save()
    except IntegrityError:
        messages.error(request, "! username or email exists")
        return redirect("userApp:index")
    login(request, user)
    return redirect('notes:notes', userName = username)
       

def index_login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('notes:notes', userName = username)
            else:
                messages.error(request, "Invalid credentials")

        except Exception as e:
            messages.error(request, f"Authentication failed: {e}")
            return redirect('userApp:indexLogin')

        else:
            return redirect('userApp:indexLogin')
    else:     
        notes = Note.objects.filter(is_shared=True).order_by('-created_at')
        paginator_n = Paginator(notes,3)
        page_no_n = request.GET.get('page')
        single_page_notes = paginator_n.get_page(page_no_n)

        tutorials = Tutorial.objects.filter(is_shared=True).order_by('-created_at')
        paginator_t = Paginator(tutorials,3)
        page_no_t = request.GET.get('page')
        single_page_tutorials = paginator_t.get_page(page_no_t)

    return render(request, 'index_login.html',{'notes':single_page_notes, 'tutorials' :single_page_tutorials})


def logout_user(requset):
    logout(requset)
    return redirect('userApp:index')

def view_note(request,note_id):
    note = Note.objects.get(pk=note_id)
    return render(request, 'viewnote.html',{'note':note,})


def shared_notes(request):
    notes = Note.objects.filter(is_shared=True)
    paginator_n = Paginator(notes,10)
    page_no_n = request.GET.get('page')
    single_page_notes = paginator_n.get_page(page_no_n)
    return render(request, 'sharednotes.html',{'notes':single_page_notes,})

def shared_tutorials(request):
    tutorials = Tutorial.objects.filter(is_shared=True)
    paginator_t = Paginator(tutorials,10)
    page_no_t = request.GET.get('page')
    single_page_tutorials = paginator_t.get_page(page_no_t)

    return render(request, 'sharedtutorials.html',{'tutorials' :single_page_tutorials})

def user_shared_notes(request):
    notes = Note.objects.filter(is_shared=True)
    paginator_n = Paginator(notes,10)
    page_no_n = request.GET.get('page')
    single_page_notes = paginator_n.get_page(page_no_n)
    return render(request, 'usersharednotes.html',{'notes':single_page_notes,})

def user_shared_tutorials(request):
    tutorials = Tutorial.objects.filter(is_shared=True)
    paginator_t = Paginator(tutorials,10)
    page_no_t = request.GET.get('page')
    single_page_tutorials = paginator_t.get_page(page_no_t)

    return render(request, 'usersharedtutorials.html',{'tutorials' :single_page_tutorials})