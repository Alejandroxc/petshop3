from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Prodcuto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.models.TextField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    fecha = models.models.DateField()

    def __str__(self):
        return self.nombre