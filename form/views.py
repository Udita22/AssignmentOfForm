from django.shortcuts import render
from .forms import modelCreateForm
from .models import userPreference
import json


def createForm(request):
    if request.method == 'GET':
         return render(request, 'form/createform.html',{"form": modelCreateForm()})
    else:
        try:
            form = modelCreateForm(request.POST)
            newForm = form.save(commit = False)
            newForm.save()
            return render(request, 'form/successfulCreation.html')
        except ValueError:
            return render(request, 'form/createform.html',{"form": form})


def showForm(request):
    users = userPreference.objects.all()
    return render(request, 'form/allForms.html',{"users":users})
