from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget


class NoteForm(forms.ModelForm):
    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(widget=CKEditorWidget(attrs={'class': 'my-ckeditor-class',}))
    class Meta:
        model = Note
        fields = '__all__'
