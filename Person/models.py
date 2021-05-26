from django.db import models
from identificationType.models import identificationType

# Create your models here.
class Person(models.Model):
    IDENTIFICATION_TYPES = (
        ('CC', 'Cedula'),
        ('CE', 'Cedula Extranjeria'),
        ('P', 'Pasaporte'),
        ('T', 'Tarjeta Identidad'),
        ('NUI', 'Numero Unico Identificacion'),
    )

    GENDER_TYPES = (
        ('F', 'Femenino'),
        ('M', 'Masculino'),
        ('O', 'Otro'),
    )

    ROL_TYPES = (
        ('U', 'Usuario Sistema'),
        ('J', 'Juez'),
        ('DM', 'Demandado'),
        ('DMT', 'Demandante'),
    )

    idPerson = models.AutoField("Id Interno", primary_key= True)
    idType = models.CharField("Tipo Identificación", max_length=5, choices=IDENTIFICATION_TYPES, default="CC")
    idNumber = models.CharField("Numero Identificación", max_length=30)
    firstName = models.CharField("Primer Nombre", max_length=50)
    secondName = models.CharField("Segundo Nombre", max_length=50)
    surname = models.CharField("Primer Apellido", max_length=50)
    secondSurname = models.CharField("Segundo Apellido", max_length=50)
    gender = models.CharField("Sexo", max_length=20, choices=GENDER_TYPES, default="F")
    address = models.CharField("Direccion Residencia", max_length=500)
    countryOfBirth = models.CharField("Pais Nacimiento", max_length=100)
    cityOfBirth = models.CharField("Ciudad Nacimiento", max_length=100)
    email = models.EmailField("Correo Electronico", max_length=150)
    role = models.CharField("Rol", max_length=30, choices=ROL_TYPES, default="DM")

    def __str__(self):
        return self.numberId