from django import forms
from .models import Todolist

class TodolistForm(forms.ModelForm):
    class Meta:
        model = Todolist
        fields = ['title', 'description', 'important', 'target_day']
    
    title = forms.CharField(label='해야할 일', widget=forms.TextInput())
    description = forms.CharField(label='설명', widget=forms.Textarea())
    important = forms.CharField(label='중요한일', widget=forms.CheckboxInput(), required=False)
    target_day = forms.CharField(label='목표 기간', widget = forms.SelectDateWidget())
