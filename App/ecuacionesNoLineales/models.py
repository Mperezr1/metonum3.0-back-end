from django.db import models

# Create your models here.


class EcuacionesNoLineales(models.Model):
    funcion = models.CharField(max_length=60, blank=True, null=False)
    valorInicial = models.IntegerField(blank=True, null=True)
    delta = models.IntegerField(blank=True, null=True)
    iter = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.funcion
