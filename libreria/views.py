from django.shortcuts import render
from django.http import HttpResponse
from .models import Libro

# Create your views here.
def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/index.html', {'libros': libros})

def descuentos(request):
    return render(request, 'paginas/descuentos.html')

def actividades(request):
    return render(request, 'paginas/actividades.html')

def crear(request):
    return render(request, 'libros/crear.html')

def editar(request):
    return render(request, 'libros/editar.html')

