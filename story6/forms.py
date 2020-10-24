from django.db.models import fields
from django import forms
from django.forms import ModelForm, Textarea, TextInput, DateInput
from django.forms import widgets
from .models import People, Activities

# Form Class
gender= (('Male','Male'),('Female','Female'))
class PeopleForm(ModelForm):
    class Meta:
        model = People
        fields = ['full_name','nickname','gender','birthday','activities_registered']
        widgets = {
            'full_name': TextInput(attrs={'placeholder': 'ex: Ren Amamiya', 'required': True}),
            'nickname': TextInput(attrs={'placeholder': 'ex: Ren', 'required': True}),
            'gender': forms.Select(choices=gender, attrs={'class': 'form-control', 'required': True}),
            'birthday':DateInput(attrs={'placeholder': 'YYYY-MM-DD', 'required': True}),
            }

class ActivitiesForm(ModelForm):
    class Meta:
        model = Activities
        fields = ['name','date']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'ex: Lunch ', 'required': True}),
            'date':DateInput(attrs={'placeholder': 'YYYY-MM-DD', 'required': True}),
        }