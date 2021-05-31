from django.db import models

# Create your models here.

class DailyBookAccounting(models.Model):
    idBook = models.AutoField("Id Interno", primary_key= True)
    idPerson = models.BigIntegerField("Id Interno Persona")
    title = models.CharField("Titulo", max_length=30)
    registrationDate = models.DateTimeField("Fecha Registro", auto_now=False, auto_now_add=False)
    registrationNumber = models.BigIntegerField("Numero Radicado")
    incomeValue = models.DecimalField("Valor Ingreso", max_digits=19, decimal_places=2)
    outputValue = models.DecimalField("Valor Egreso", max_digits=19, decimal_places=2)
    balance = models.DecimalField("Saldo", max_digits=19, decimal_places=2)
    observations = models.CharField("Observaciones", max_length=50)

    def __str__(self):
        return self.idBook
