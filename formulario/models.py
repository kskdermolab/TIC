from django.db import models

class Form(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)

