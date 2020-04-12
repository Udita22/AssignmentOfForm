from django.forms import ModelForm
from .models import createForm
from django import forms

class modelCreateForm(ModelForm):
    class Meta:
        model = createForm
        fields = ['name','favourite_colour','cat','dog']
       