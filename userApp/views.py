from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import login,logout, authenticate
from django.urls import reverse
from notes.models import Note,Tutorial, User
from django.core.paginator import Paginator
from .forms import RegistrationForm
from django.contrib import messages
from allauth.account.auth_backends import AuthenticationBackend as AllAuthBackend


# Create your views here.
def index(request):
    notes = Note.objects.filter(is_shared=True).order_by('-created_at')
    paginator_n = Paginator(notes,3)
    page_no_n = request.GET.get('page_notes')
    single_page_notes = paginator_n.get_page(page_no_n)

    tutorials = Tutorial.objects.filter(is_shared=True).order_by('-created_at')
    paginator_t = Paginator(tutorials,3)
    page_no_t = request.GET.get('page_tutorials')
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

    # Authenticate and log in using allauth backend
    user = authenticate(request, username=username, password=password, backend=AllAuthBackend)
    if user is not None:
        login(request, user)
        return redirect('notes:notes', userName=username)
    else:
        # Handle the case where authentication failed, if necessary
        messages.error(request, "! Authentication failed")
        return redirect("userApp:index")
       

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

def google_redirect(request):
    if request.user.is_authenticated:
        username = request.user.username
        redirect_url = reverse('notes:notes', kwargs={'userName': username})
        return redirect(redirect_url)


def logout_user(request):
    system_messages = messages.get_messages(request)
    for message in system_messages:
        pass
    messages.success(request, 'You have been successfully logged out.')
    logout(request)
    return redirect('userApp:index')

def view_note(request,note_id):
    note = Note.objects.get(pk=note_id)
    return render(request, 'viewnote.html',{'note':note,})


def shared_notes(request):
    search_keyword = request.POST.get('searchnote','')
    if request.method =='POST':
        if search_keyword:
            notes = Note.objects.filter(title__icontains = search_keyword).order_by('-created_at')
    else:
        notes = Note.objects.filter(is_shared=True).order_by('-created_at')
        
    paginator_n = Paginator(notes,10)
    page_no_n = request.GET.get('page')
    single_page_notes = paginator_n.get_page(page_no_n)

    return render(request, 'sharednotes.html',{'notes':single_page_notes,'search_keyword':search_keyword})

def shared_tutorials(request):
    search_keyword = request.POST.get('searchtuto','')
    if request.method =='POST':
        if search_keyword:
            tutorials = Tutorial.objects.filter(title__icontains = search_keyword).order_by('-created_at')
    else:
        tutorials = Tutorial.objects.filter(is_shared=True).order_by('-created_at')

    paginator_t = Paginator(tutorials,10)
    page_no_t = request.GET.get('page')
    single_page_tutorials = paginator_t.get_page(page_no_t)

    return render(request, 'sharedtutorials.html',{'tutorials' :single_page_tutorials,'search_keyword':search_keyword})

def user_shared_notes(request, userName):
    search_keyword = request.POST.get('searchnote','')
    if request.method =='POST':
        if search_keyword:
            notes = Note.objects.filter(title__icontains = search_keyword).order_by('-created_at')
    else:
        notes = Note.objects.filter(is_shared=True).order_by('-created_at')
        
    paginator_n = Paginator(notes,10)
    page_no_n = request.GET.get('page')
    single_page_notes = paginator_n.get_page(page_no_n)

    return render(request, 'usersharednotes.html',{'notes':single_page_notes, 'search_keyword':search_keyword})

def user_shared_tutorials(request,userName):
    search_keyword = request.POST.get('searchtuto','')
    if request.method =='POST':
        if search_keyword:
            tutorials = Tutorial.objects.filter(title__icontains = search_keyword).order_by('-created_at')
    else:
        tutorials = Tutorial.objects.filter(is_shared=True).order_by('-created_at')

    paginator_t = Paginator(tutorials,10)
    page_no_t = request.GET.get('page')
    single_page_tutorials = paginator_t.get_page(page_no_t)

    return render(request, 'usersharedtutorials.html',{'tutorials' :single_page_tutorials, 'search_keyword':search_keyword})