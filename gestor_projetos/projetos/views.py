from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm
from .forms import AssigmentForm
from .models import Project
from .models import Assignment
from pessoas.models import Person

# Create your views here.
@login_required
def proj_new(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        project = Project(name=form.data.get('name'), username_manager=request.user.username, budget=form.data.get('budget'))
        project.save()
        return redirect('proj_list')
    return render(request, 'proj_new.html', {'form': form, 'proj_id': -1})

@login_required
def proj_list(request):
    projects = Project.objects.all()
    return render(request, 'projects_list.html', {'projects': projects, 'user':request.user.username})


@login_required
def proj_detail(request, id):
    project = get_object_or_404(Project, pk=id)
    assignments = Assignment.objects.all()

    return render(request, 'project_detail.html', {'project': project, 'assignments': assignments})


@login_required
def proj_edit(request, id):
    project = get_object_or_404(Project, pk=id)
    form = ProjectForm(request.POST or None, instance=project)
    if form.is_valid():
        form.save()
        return redirect('proj_list')
    return render(request, 'proj_new.html', {'form': form, 'proj_id':id})


@login_required
def proj_delete(request, id):
    project = get_object_or_404(Project, pk=id)

    if request.method=='POST':
        assignments = Assignment.objects.all()
        for assignment in assignments:
            print(assignment.name)
            if(assignment.project_id == project.id):
                assignment.delete()
                print(assignment.name)
        project.delete()

        return redirect('proj_list')
    return render(request, 'proj_delete_confirm.html', {'project': project})



@login_required
def assignment_new(request, id):
    form = AssigmentForm(request.POST or None)
    persons = Person.objects.all()
    if form.is_valid():
        assignment = Assignment(name=form.data.get('name'), programer_id=request.POST.get('id_prog'), project_id=id, date=form.data.get('date'), description=form.data.get('description'))
        assignment.save()
        return redirect('proj_detail', id)
    return render(request, 'assignment_new.html', {'form': form, 'persons':persons})


@login_required
def assignment_detail(request, id):
    assignment = get_object_or_404(Assignment, pk=id)
    project = get_object_or_404(Project, pk=assignment.project_id)
    programer = get_object_or_404(Person, pk=assignment.programer_id)
    user= request.user.username
    return render(request, 'assignment_detail.html', {'assignment': assignment, 'project':project, 'programer':programer, 'user':user})


@login_required
def programer_page(request):
    programer = get_object_or_404(Person, username=request.user.username)
    assignments = Assignment.objects.all()
    return render(request, 'programer_page.html', {'assignments': assignments, 'programer':programer})

@login_required
def assignment_mark_finished_confirm(request, id):
    assignment = get_object_or_404(Assignment, pk=id)
    if request.method=='POST':
        assignment.finished = True
        assignment.save()
        return redirect('programer_page')
    return render(request, 'assignment_mark_finished_confirm.html', {'assignment': assignment})