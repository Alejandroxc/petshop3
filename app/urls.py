from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('registro/', registro, name='registro'),
    path('ingresar/', ingresar, name='ingresar'),
    path('menu-superior/', menuSuperior, name='menu-superior'),
    path('administracion/', administracion, name='administracion'),
    path('bodega/', bodega, name= 'bodega'),
    path('boleta/', boleta, name='boleta'),
    path('boletaCli/', boletaCli, name='boletaCli'),
    path('carrito/', carrito, name='carrito'),
    path('cerrarSesion/', cerrarSesion, name='cerrarSesion'),
    path('ficha/', ficha, name='ficha'),
    path('footer/', footer, name='footer'),
    path('misCompras/', misCompras, name='misCompras'),
    path('misDatos/', misDatos, name='misDatos'),
    path('nosotros/', nosotros, name='nosotros'),
    path('productos/', producto, name='productos'),
    path('ropa/', ropa, name='ropa'),
    path('usuarios/', ropa, name='usuarios'),
    path('ventas/', ventas, name='ventas'),


]