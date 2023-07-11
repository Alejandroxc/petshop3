from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Prodcuto(models.Model):
    nombre = models.CharField(max_length=50)
    disponibilidad = models.BooleanField("stock",null=True, default=False)
    precio = models.IntegerField()
    descripcion = models.TextField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombre
    
class Usuario(models.Model):
    es_administrador = models.BooleanField(default=False, null=True)
    rut = models.CharField(max_length=12, null=True)
    nombre = models.CharField(max_length=50, null=True)
    apellido = models.CharField(max_length=50, null=True)
    correo = models.EmailField(max_length=254, null=True)
    direccion = models.CharField(("dirección"),max_length=50, null=True)
    contrasena = models.CharField(("contraseña"), max_length=50, null=True)
    imagen = models.ImageField(upload_to="usuarios", null=True)
    suscripcion = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.nombre
    
class Boleta(models.Model):
    categoria = models.CharField(max_length=100)
    producto = models.ForeignKey(Prodcuto, on_delete=models.PROTECT)
    precio_unitario = models.IntegerField("precio unitario")
    porc_descto_subscriptor = models.IntegerField("% descuento subscriptor")
    porc_descto_oferta = models.IntegerField("% descuento oferta")
    porc_descto_total = models.IntegerField("% descuento total")
    descto_total = models.IntegerField("descuento total")
    valor_final = models.IntegerField("valor final")

    def str(self):
        return f"{self.producto} - {self.valor_final}"