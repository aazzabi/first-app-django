from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from App.models import Project ,MembershipInProject
from App.forms import AddProjectForm
# Create your views here.

def Affiche(request):
    return HttpResponse("bonjour")

def Detail(request, id):
    p = Project.objects.get(id= id)
    membership = MembershipInProject.objects.all()
    listM= []
    for m in membership:
        if m.projet == p:
            listM.append(m)
    return render(request, 'Project/detail.html', {'p': p, 'membership': listM})

def AllProject(request):
    all = Project.objects.all()
    return render(request, 'Project/index.html', {'projects': all})

def AddProject(request):
    form = AddProjectForm()
    form.fields['nom_du_projet'].widget.attrs = {'class': 'form-control'}
    form.fields['duree_du_projet'].widget.attrs = {'class': 'form-control'}
    form.fields['temps_alloue_par_le_createur'].widget.attrs = {'class': 'form-control'}
    form.fields['besoins'].widget.attrs = {'class': 'form-control'}
    form.fields['description'].widget.attrs = {'class': 'form-control'}
    form.fields['superviseur'].widget.attrs = {'class': 'cs-select cs-skin-slide'}
    form.fields['createur'].widget.attrs = {'class': 'cs-select cs-skin-slide'}
    if request.method == "POST":
        form = AddProjectForm(request.POST)
        if (form.is_valid()):
            form.save()
            return HttpResponseRedirect(reverse('project_index'))
    return render(request, 'Project/new.html', {'form': form})

def EditProject(request, id):
    p = Project.objects.get(id= id)
    formEdit = AddProjectForm(instance=p)
    formEdit.fields['nom_du_projet'].widget.attrs = {'class': 'form-control'}
    formEdit.fields['duree_du_projet'].widget.attrs = {'class': 'form-control'}
    formEdit.fields['temps_alloue_par_le_createur'].widget.attrs = {'class': 'form-control'}
    formEdit.fields['besoins'].widget.attrs = {'class': 'form-control'}
    formEdit.fields['description'].widget.attrs = {'class': 'form-control'}
    formEdit.fields['superviseur'].widget.attrs = {'class': 'cs-select cs-skin-slide'}
    formEdit.fields['createur'].widget.attrs = {'class': 'cs-select cs-skin-slide'}
    if request.method == "POST":
        formEdit = AddProjectForm(request.POST, instance= p)
        if formEdit.is_valid():
            formEdit.save()
            return HttpResponseRedirect(reverse('project_index'))
    return render(request, 'Project/new.html', {'form': formEdit})

def DeleteProject(request, id):
    p= Project.objects.get(id=id)
    p.delete()
    return HttpResponseRedirect(reverse('project_index'))
