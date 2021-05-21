from django.db import models

# Create your models here.
class persona(models.Model):
    primerNombre = models.CharField(max_length=100)
    segundoNombre = models.CharField(max_length=100)
    primerApellido = models.CharField(max_length=100)
    segundoApellido = models.CharField(max_length=100)