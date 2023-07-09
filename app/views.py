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

def administracion(request):
    return render(request, 'app/administracion.html')

def bodega(request):
    return render(request, 'app/bodega.html')

def boleta(request):
    return render(request, 'app/boleta.cli')

def boletaCli(request):
    return render(request, 'app/boletaCli.html')

def carrito(request):
    return render(request, 'app/carrito.html')

def cerrarSesion(request):
    return render(request, 'app/cerrarSesion.html')

def ficha(request):
    return render(request, 'app/ficha.html')

def misCompras(request):
    return render(request, 'app/misCompras.html')

def misDatos(request):
    return render(request, 'app/misDatos.html')

def producto(request):
    return render(request, 'app/producto.html')

def ropa(request):
    return render(request, 'app/ropa.html')

def usuario(request):
    return render(request, 'app/usuario.html')

def ventas(request):
    return render(request, 'app/ventas.html')

def footer(request):
    return render(request, 'app/footer.html')

def nosotros(request):
    return render(request, 'app/nosotros.html')