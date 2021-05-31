from django.db import models

# Create your models here.
class identificationType(models.Model):
    idIdentificationType = models.AutoField("Id Interno", primary_key= True)
    codeIdentificationType = models.CharField("Codigo Tipo Identificacion", max_length=5)
    descriptionIdentificationType = models.CharField("Descripcion Tipo Identificacion", max_length=50)

    def __str__(self):
        return self.codeIdentificationType

    def getIdentificationsType ():
        identificationType.objects.all()
    