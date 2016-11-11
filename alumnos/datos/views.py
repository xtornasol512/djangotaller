from django.shortcuts import render
from django.http import HttpResponse


def hola(request):
    return render(request, "index.html", {"nombre": "Chucho A Garzón"})

def formulario(request):
    form = "Hola este es mi formulario"
    return render(request, "formulario.html", {"formulario": form})
# Create your views here.
