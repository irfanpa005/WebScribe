from django.shortcuts import render
from notes.models import Note,Tutorial
from django.core.paginator import Paginator

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