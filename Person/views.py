from Person.models import Person
from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from django.core.urlresolvers import reverse_lazy
from models import * 

# Create your views here.
class PersonList(ListView):
    model = Person