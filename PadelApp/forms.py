from django import forms

class JugadoresForm(forms.Form):
    nombre = forms.CharField(required=True, max_length=64) 
    apellido = forms.CharField(required=True, max_length=64)
    nacionalidad =  forms.CharField(required=True, max_length=64)
    edad = forms.IntegerField(required=True, max_value=100)
    circuito = forms.CharField(max_length=64)
    marca = forms.CharField(max_length=64)

class CircuitoForm(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    alcance = forms.CharField(required=True, max_length=64)
    ranking_premios = forms.IntegerField(required=True, max_value=3)
    cant_torneos = forms.IntegerField(max_value=52)

class MarcaForm(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    origen = forms.CharField(required=True, max_length=64)