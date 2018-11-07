from django.forms import ModelForm
from .models import Project
from .models import Assignment
from django.contrib.auth.forms import UserCreationForm

class ProjectForm(ModelForm):
    class Meta:
        model=Project
        fields=('name', 'budget',)


class AssigmentForm(ModelForm):
    class Meta:
        model=Assignment
        fields=('name', 'date', 'description')

