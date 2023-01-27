from django import forms
from .models import Proprietar
from .models import Animal


class FormularProprietar(forms.ModelForm):
    class Meta:
        model = Proprietar
        fields = ["nume", ]
        labels = {'nume': "Nume", }


class FormularAnimal(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ["nume", "varsta", "specie", "proprietar", ]
        labels = {'nume': "Nume", 'varsta': "Varsta", 'specie': "Specie", 'proprietar': "Proprietar"}
