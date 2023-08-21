from django import forms
from django.contrib.auth import get_user_model
from .models import *
from ckeditor.widgets import CKEditorWidget


class NoteForm(forms.ModelForm):
    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(widget=CKEditorWidget(attrs={'class': 'my-ckeditor-class',}))

    class Meta:
        model = Note
        fields = ['title', 'content', 'is_shared']

    def save(self, commit=True):
        # Get the current user
        user = self.instance.noteowner if self.instance.noteowner else self.initial.get('noteowner')
        if user is None:
            # If noteowner is not provided, use the currently logged-in user
            user = self.initial.get('user')
        
        # Create a new Note instance with the user as the note owner
        note = super().save(commit=False)
        note.noteowner = user

        if commit:
            note.save()

        return note
