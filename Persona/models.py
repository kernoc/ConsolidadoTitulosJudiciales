from django.db import models

# Create your models here.
class persona(models.Model):
    idPerson = models.AutoField(primary_key= True)
    typeId = models.CharField(max_length=20)
    numberId = models.CharField(max_length=30)
    firstName = models.CharField(max_length=50)
    secondName = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    secondSurname = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    address = models.CharField(max_length=500)
    email = models.EmailField(max_length=150)
    countryOfBirth = models.CharField(max_length=100)
    cityOfBirth = models.CharField(max_length=100)
    role = models.CharField(max_length=30)