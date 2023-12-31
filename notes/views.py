from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Note, Tutorial
from userApp.models import User
from .forms import NoteForm,TutorialForm
import json
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


# Create your views here.
def notes(request, userName):
    current_user = request.user
    notes = Note.objects.filter(noteowner = current_user)
    return render(request, 'notes.html',{'notes': notes})


def note_display(request,note_id):
    try:
        note = Note.objects.get(id=note_id)
        data = {
            'id': note.pk,
            'title': note.title,
            'created_at':note.created_at,
            'content':note.content,
            'is_shared':note.is_shared,
        }
        return JsonResponse(data)
    except Note.DoesNotExist:
        return JsonResponse({'error': 'Object not found'}, status=404)


def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.instance.noteowner = request.user
            form.save()
            return redirect('notes:notes', userName=request.user.username)
    else:
        form = NoteForm()
    return render(request, 'createnote.html', {'form': form})

def edit_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    form = NoteForm(request.POST or None, instance=note)
    if form.is_valid():
        form.instance.noteowner = request.user
        form.save()
        return redirect('notes:notes', userName=request.user.username)

    return render(request, 'updatenote.html', {'form': form})

def delete_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    note.delete()
    return redirect('notes:notes', userName=request.user.username)


def note_share_status(request, note_id):
    note = get_object_or_404(Note,pk=note_id)
    if request.method == "POST":
        data = json.loads(request.body)
        is_shared = data['isShared']
        note.is_shared = is_shared
        note.save()
    # note = get_object_or_404(Note,pk=note_id)
    # is_shared = request.POST.get('isShared', False)
    # print(is_shared)
    # note.is_shared = is_shared
    # note.save()
    return JsonResponse({'message': 'Note shared status updated successfully'})


def user_note_search(request):
    if request.method == "POST":
        data = json.loads(request.body)
        search_keyword = data['search_keyword']
        current_user = request.user

    if search_keyword:
        filtered_notes = Note.objects.filter(noteowner=current_user).filter(title__icontains=search_keyword)
    else:
        filtered_notes = Note.objects.filter(noteowner=current_user)

    notes_data = []
    for note in filtered_notes:
        notes_data.append({'pk': note.pk, 'title': note.title})

    return JsonResponse(notes_data, safe=False)


def tutorials(request, userName):
    current_user = request.user
    tutorials = Tutorial.objects.filter(tutorial_owner =current_user).order_by('-created_at')
    paginator_t = Paginator(tutorials,10)
    page_no_t = request.GET.get('page')
    single_page_tutorials = paginator_t.get_page(page_no_t)
    form = TutorialForm()
    return render(request, 'tutorials.html', {'tutorials' :single_page_tutorials, 'form': form })


def add_tutorial(request, userName):
    if request.method == "POST":
        form = TutorialForm(request.POST)
        if form.is_valid():
            form.instance.tutorial_owner = request.user
            form.save()
    return redirect('notes:tutorials', userName=request.user)


def edit_tutorial(request, tuto_id):
    if request.method == 'GET':
        tuto = get_object_or_404(Tutorial, pk=tuto_id)
        form = TutorialForm(instance=tuto)
        form_data = {
                'title': form['title'].value(),
                'short_descr': form['short_descr'].value(),
                'link': form['link'].value(),
                'is_shared': form['is_shared'].value(),
            }
        return JsonResponse (form_data, safe=False)
    else:
        tuto = get_object_or_404(Tutorial, pk=tuto_id)
        form = TutorialForm(request.POST or None, instance = tuto)
        if form.is_valid():
            form.instance.tutorial_owner = request.user
            form.save()
            return redirect('notes:tutorials', userName=request.user.username)
        
def delete_tutorial(request, tuto_id):
    tuto = get_object_or_404(Tutorial, pk= tuto_id)
    tuto.delete()
    return redirect('notes:tutorials', userName=request.user.username)

def user_search_tutorial(request):
    current_user = request.user
    if request.method == "POST":
        search_keyword = request.POST.get('searchtuto','')

    if search_keyword:
        tutorials = Tutorial.objects.filter(tutorial_owner=current_user).filter(title__icontains=search_keyword)
        paginator_t = Paginator(tutorials,10)
        page_no_t = request.GET.get('page')
        single_page_tutorials = paginator_t.get_page(page_no_t)
    else:
        tutorials = Tutorial.objects.filter(tutorial_owner=current_user)

    form = TutorialForm()

    return render(request, 'tutorials.html', {'tutorials' :single_page_tutorials, 'form': form , 'search_keyword':search_keyword})

def tutorial_share_status(request, tuto_id):
    tuto = get_object_or_404(Tutorial, pk=tuto_id)
    if request.method == 'POST':
        data = json.loads(request.body)
        is_shared = data['isShared']
        tuto.is_shared = is_shared
        tuto.save()
    return JsonResponse({'message': 'Tutorial shared status updated successfully'})


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)




