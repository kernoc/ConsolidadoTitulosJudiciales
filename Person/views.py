from Person.models import Person
from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy

# Create your views here.
class PersonList(ListView):
    model = Person

class PersonDetail(DetailView):
    model = Person

class PersonCreation(CreateView):
    model = Person
    success_url = reverse_lazy('Person:list') 
    fields = ['idType', 'idNumber', 'firstName', 'secondName', 'surname', 'secondSurname', 'secondName', 'gender', 'address', 'countryOfBirth', 'cityOfBirth', 'email', 'role']

class PersonUpdate(UpdateView):
    model = Person
    success_url = reverse_lazy('Person:list')
    fields = ['idType', 'idNumber', 'firstName', 'secondName', 'surname', 'secondSurname', 'secondName', 'gender', 'address', 'countryOfBirth', 'cityOfBirth', 'email', 'role']

class PersonDelete(DeleteView):
    #template_name = "templates/Person/person_confirm_delete.html"
    model = Person
    success_url = reverse_lazy('Person:list')