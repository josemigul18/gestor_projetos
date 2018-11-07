from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Person
from .forms import PersonForm
from django.contrib.auth.models import User

# Create your views here.
@login_required
def persons_list(request):
    persons = Person.objects.all()
    return render(request, 'persons_list.html', {'persons': persons})


def person_new(request):
    form=PersonForm(request.POST)
    if form.is_valid():
        u=User(username=form.data.get('username'))
        u.set_password(form.data.get('password'))
        u.is_superuser = True
        u.is_staff=True
        person = Person(username=form.data.get('username'), first_name=form.data.get('first_name'), last_name=form.data.get('last_name'), type_person=form.data.get('type_person'))
        try:
            u.save()
            person.save()
        except:
            return render(request, 'person_form.html', {'form': form})

        return redirect('login')
    return render(request, 'person_form.html', {'form':form})


@login_required
def person_decide(request):
    person = Person.objects.get(username=request.user.username)
    if(person.type_person == 'M'):
        return redirect('proj_list')
    else:
        return redirect('programer_page')

