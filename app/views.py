from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def registro(request):
    return render(request, 'app/registro.html')

def ingresar(request):
    return render(request, 'app/ingresar.html')

def menuSuperior(request):
    return render(request, 'app/menu-superior.html')