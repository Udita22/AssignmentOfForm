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
            #form = request.POST
            print(form)
            print("It should print form")
            newForm = form.save(commit = False)
            newForm.save()
            return render(request, 'form/successfulCreation.html')
        except ValueError:
            return render(request, 'form/createform.html',{"form": modelCreateForm(),"error": "Name already exists, try using another name"})

def showForm(request):
    allForms = userPreference.objects.all()
    return render(request, 'form/allForms.html',{"allForms":allForms})
