from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('registro/', registro, name='registro'),
    path('ingresar/', ingresar, name='ingresar'),
    path('menu-superior/' menuSuperior, name= 'menu-superior'),
]