from django.db import models

# Create your models here.
class Person(models.Model):
    idPerson = models.AutoField(primary_key= True)
    idType = models.CharField(max_length=20)
    idNumber = models.CharField(max_length=30)
    firstName = models.CharField(max_length=50)
    secondName = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    secondSurname = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    address = models.CharField(max_length=500)
    countryOfBirth = models.CharField(max_length=100)
    cityOfBirth = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    role = models.CharField(max_length=30)

    def __str__(self):
        return self.numberId