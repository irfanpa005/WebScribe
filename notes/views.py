from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Note, Tutorial
from .forms import NoteForm
import json
from django.http import JsonResponse
from django.core.paginator import Paginator


# Create your views here.
def notes(request):
    notes = Note.objects.all()
    return render(request, 'notes.html',{'notes': notes})


def note_display(request,note_id):
    try:
        note = Note.objects.get(id=note_id)
        data = {
            'id': note.pk,
            'title': note.title,
            'created_at':note.created_at,
            'content':note.content,
        }
        return JsonResponse(data)
    except Note.DoesNotExist:
        return JsonResponse({'error': 'Object not found'}, status=404)
    

def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes:notes')
    else:
        form = NoteForm()
    return render(request, 'createnote.html', {'form': form})

def tutorials(request):
    tutorials = Tutorial.objects.filter(is_shared=True)
    paginator_t = Paginator(tutorials,10)
    page_no_t = request.GET.get('page')
    single_page_tutorials = paginator_t.get_page(page_no_t)
    return render(request, 'tutorials.html', {'tutorials' :single_page_tutorials})

def user_note_search(request):
    if request.method == "POST":
        data = json.loads(request.body)
        search_keyword = data['search_keyword']

    if search_keyword:
        filtered_notes = Note.objects.filter(title__icontains=search_keyword)
    else:
        filtered_notes = Note.objects.all()

    notes_data = []
    for note in filtered_notes:
        notes_data.append({'pk': note.pk, 'title': note.title})

    return JsonResponse(notes_data, safe=False)