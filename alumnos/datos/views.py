from django.shortcuts import render
from django.http import HttpResponse
from .forms import InfoGeneralForm

def hola(request):
    return render(request, "index.html", {"nombre": "Chucho A Garzón"})

def formulario(request):
    form = InfoGeneralForm()
    return render(request, "formulario.html", {"formulario": form})
# Create your views here.
