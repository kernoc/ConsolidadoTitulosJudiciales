from django.db import models

# Create your models here.
class DailyBookAccounting(models.Model):
    idBook = models.AutoField("Id Interno", primary_key= True)
    idPerson = models.IntegerField("Id Interno Persona", 20)
    title= models.CharField("Titulo", max_length=30)
    registrationDate= models.DateField("Fecha Registro")
    registrationNumber= models.IntegerField("Numero Radicado", 20)
    incomeValue = models.FloatField("Valor Ingreso")
    outputValue = models.FloatField("Valor Egreso")
    balance = models.FloatField("Saldo")
    observations= models.CharField("Observaciones", max_length=50)
