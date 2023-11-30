# app/forms.py
from django import forms
from .models import FormData

class FormDataForm(forms.ModelForm):
    class Meta:
        model = FormData
        fields = ['question', 'answer1', 'answer2', 'answer3', 'answer4', 'answer5', 'selected_answer']

