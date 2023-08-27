from django import forms
from django.contrib.auth import get_user_model
from .models import *
from ckeditor.widgets import CKEditorWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


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

class TutorialForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit','Add Tutorial'))

    class Meta:
        model = Tutorial
        fields = ['title', 'short_descr', 'link', 'is_shared']

    def save(self, commit=True):
        # Get the current user
        user = self.instance.tutorial_owner if self.instance.tutorial_owner else self.initial.get('tutorial_owner')
        if user is None:
            # If tutorial_owner is not provided, use the currently logged-in user
            user = self.initial.get('user')
        
        # Create a new Note instance with the user as the note owner
        note = super().save(commit=False)
        note.tutorial_owner = user

        if commit:
            note.save()

        return note