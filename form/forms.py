from django.forms import ModelForm
from .models import userPreference
from django import forms


class modelCreateForm(ModelForm):
    class Meta:
        model = userPreference
        fields = ['name','favourite_colour','cat_or_dog']
       