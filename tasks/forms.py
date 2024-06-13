from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    start_time = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M']
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'start_time', 'completed']
