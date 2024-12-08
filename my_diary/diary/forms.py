from django import forms
from .models import Task
from django.forms import DateInput

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'due_date']
        widgets = {
            'due_date': DateInput(attrs={'type': 'date'}),
        }



