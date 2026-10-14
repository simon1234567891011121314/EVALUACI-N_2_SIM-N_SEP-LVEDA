from django.db import models

# Create your models here.
class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    

    def __str__(self):
        return self.nombre

class Arriendo(models.Model):
    descripcion = models.CharField(max_length=50)
    precio = models.IntegerField()
    nombre = models.ForeignKey(Equipo, on_delete=models.CASCADE)

    