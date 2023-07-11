from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Prodcuto(models.Model):
    nombre = models.CharField(max_length=50)
    disponibilidad = models.BooleanField("stock",null=True)
    precio = models.IntegerField()
    descripcion = models.TextField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombre
    
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    es_administrador = models.BooleanField(default=False) # Aquí es donde se realizó el cambio
    rut = models.CharField(max_length=12)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    correo = models.EmailField(max_length=100)
    direccion = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="usuarios", null=True)
    suscripcion = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"