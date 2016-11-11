from django.shortcuts import render
from django.http import HttpResponse
from .forms import InfoGeneralForm
from .models import InfoGeneral

def hola(request):
    return render(request, "index.html", {"nombre": "Chucho A Garzón"})

def formulario(request):
    form = InfoGeneralForm()
    if request.method == "POST":
        form = InfoGeneralForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "formulario.html", {"formulario": "Gracias ya esta guardado tus datos"})

    return render(request, "formulario.html", {"formulario": form})
# Create your views here.
