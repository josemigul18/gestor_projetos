from django.forms import ModelForm
from .models import Person
from django import forms

class PersonForm(ModelForm):
    class Meta:
        model=Person
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields='__all__'




