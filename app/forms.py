# app/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import FormData 

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'password1', 'password2']

class FormDataForm(forms.ModelForm):
    class Meta:
        model = FormData
        fields = ['question', 'answer1', 'answer2', 'answer3', 'answer4', 'answer5','selected_answer']

