from django import forms
from django.contrib.auth import get_user_model
from .models import *
from ckeditor.widgets import CKEditorWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.core.validators import MinValueValidator

class TaskForm(forms.ModelForm):
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit','Add Note'))


    due_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), validators=[MinValueValidator(limit_value=timezone.now().date())])
    class Meta:
        model = Task
        fields = ['title', 'details', 'is_Active', 'priority','due_date']

    # def save(self, commit=True):
    #     # Get the current user
    #     user = self.instance.owner if self.instance.owner else self.initial.get('owner')
    #     if user is None:
    #         # If noteowner is not provided, use the currently logged-in user
    #         user = self.initial.get('user')
        
    #     # Create a new Note instance with the user as the note owner
    #     task = super().save(commit=False)
    #     task.owner = user

    #     if commit:
    #         task.save()

    #     return task
