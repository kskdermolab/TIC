from django.db import models

class Form(models.Model):
    Nombre = models.CharField(max_length=20)
    Apellido = models.CharField(max_length=20)
    DNI = models.IntegerField(max_length=8)

