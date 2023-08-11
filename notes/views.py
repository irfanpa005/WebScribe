from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm


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
    return render(request, 'tutorials.html')
