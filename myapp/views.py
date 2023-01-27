from django.http import HttpResponse
from django.shortcuts import render
from .models import Proprietar
from .models import Animal
from .forms import FormularProprietar
from .forms import FormularAnimal


# Create your views here.

def homepage(request):
    print(type(render))
    return render(request, 'homepage.html', {
        "name": "DJANGO"
    })


def formularproprietar(request):
    if request.method == "POST":
        form = FormularProprietar(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Proprietar adaugat cu succes!")
    else:
        form = FormularProprietar()
    return render(request, 'adauga_proprietar.html', {'form': form})


def formularanimal(request):
    if request.method == "POST":
        form = FormularAnimal(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Animal adaugat cu succes!")
    else:
        form = FormularAnimal()
    return render(request, 'adauga_animal.html', {'form': form})


def afiseazaproprietari(request):
    proprietari = Proprietar.objects.all()
    return render(request, 'afiseazaproprietari.html', {'proprietari': proprietari})


def afiseazaanimale(request):
    animale = Animal.objects.all()
    return render(request, 'afiseazaanimale.html', {'animale': animale})