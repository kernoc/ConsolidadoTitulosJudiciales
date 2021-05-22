from django.db import models

# Create your models here.
class identificationType(models.Model):
    idIdentificationType = models.AutoField(primary_key= True)
    codeIdentificationType = models.CharField(max_length=5)
    descriptionIdentificationType = models.CharField(max_length=50)

    def __str__(self):
        return self.codeIdentificationType
    