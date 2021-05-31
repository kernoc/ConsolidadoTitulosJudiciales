from IdentificationType.models import IdentificationType
from django.contrib import admin

# Register your models here.
from .models import Person

admin.site.register(Person)