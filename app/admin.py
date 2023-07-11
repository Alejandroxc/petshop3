from django.contrib import admin
from .models import *

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display=["nombre", "precio", "disponibilidad", "marca"]
    list_editable= ["precio"]
    search_fields= ["nombre"]
    list_filter= ["marca", "disponibilidad"]

admin.site.register(Marca)
admin.site.register(Prodcuto, ProductoAdmin)
admin.site.register(Usuario)
admin.site.register(Boleta)