from django.db import models


# Create your models here.
class EcuacionesNoLineales(models.Model):
    objects = None
    funcion = models.TextField(max_length=50, default='x')
    extremo_sup = models.IntegerField(default=1)
    extremo_inf = models.IntegerField(default=1)
    tol = models.DecimalField(max_digits=10, decimal_places=5, default=1)
    iter = models.IntegerField(default=1)
