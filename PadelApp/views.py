from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from datetime import datetime

from PadelApp.models import Jugadores, Circuito, Marca
from PadelApp.forms import JugadoresForm, CircuitoForm, MarcaForm
# Create your views here.

def inicio(request):
    contexto = {}
    return render(
        request=request,
        template_name='PadelApp/base.html',
        context=contexto,
    )
def inicio2(request):
    contexto = {}
    return render(
        request=request,
        template_name='PadelApp/inicio.html',
        context=contexto,
    )

def listar_jugadores(request):
    jugadores = Jugadores.objects.all()
    context = {'jugadores':jugadores}
    return render(request, 'PadelApp/jugadores.html', context)

def listar_circuito(request):
    circuito = Circuito.objects.all()
    context = {'circuitos':circuito}
    return render(request, 'PadelApp/circuito.html', context)

def listar_marca(request):
    contexto = {'marcas': Marca.objects.all()}
    return render (request, 
                    template_name='PadelApp/marca.html', 
                    context=contexto)

def crear_jugador(request):
    if request.method == "POST":
        formulario = JugadoresForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data["nombre"]
            apellido = data["apellido"]
            nacionalidad = data["nacionalidad"]
            edad = data["edad"]
            circuito = data["circuito"]
            marca = data["marca"]
            jugador = Jugadores(nombre=nombre, apellido=apellido, nacionalidad=nacionalidad, edad=edad, circuito=circuito,  marca=marca)
            jugador.save()  

            
            url_exitosa = reverse('listar_jugadores') 
            return redirect(url_exitosa)
    else: 
         formulario = JugadoresForm()
    http_response = render(
        request=request,
        template_name='PadelApp/crear_jugador.html',
        context={'formulario': formulario}
    )
    return http_response


def buscar_jugador(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        jugadores = Jugadores.objects.filter(apellido__icontains=busqueda)
        contexto = {
            "jugadores": jugadores
        }
        http_response = render(
            request=request,
            template_name='Padelapp/jugadores.html',
            context=contexto,
        )
        return http_response

def crear_circuito(request):
    if request.method == "POST":
        formulario = CircuitoForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data["nombre"]
            alcance = data["alcance"]
            ranking_premios = data["ranking_premios"]
            cant_torneos = data["cant_torneos"]
            circuito = Circuito(nombre=nombre, alcance=alcance,  ranking_premios=ranking_premios, cant_torneos=cant_torneos) # lo crean solo en RAM
            circuito.save() 

            url_exitosa = reverse('listar_circuitos')
            return redirect(url_exitosa)
    else: 
        formulario = CircuitoForm()
    http_response = render(
        request=request,
        template_name='PadelApp/crear_circuito.html',
        context={'formulario': formulario}
    )
    return http_response


def buscar_circuito(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        circuitos = Circuito.objects.filter(nombre__icontains=busqueda)
        contexto = {
            "circuitos": circuitos
        }
        http_response = render(
            request=request,
            template_name='Padelapp/circuito.html',
            context=contexto,
        )
        return http_response

def crear_marca(request):
    if request.method == "POST":
        formulario = MarcaForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  
            nombre = data["nombre"]
            origen = data["origen"]
            marca = Marca(nombre=nombre, origen=origen)
            marca.save()  

            url_exitosa = reverse('listar_marcas')  
            return redirect(url_exitosa)
    else: 
        formulario = MarcaForm()
    http_response = render(
        request=request,
        template_name='PadelApp/crear_marca.html',
        context={'formulario': formulario}
    )
    return http_response


def buscar_marca(request):
     if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        marcas = Marca.objects.filter(nombre__icontains=busqueda)
        contexto = {
            "marcas": marcas
        }
        http_response = render(
            request=request,
            template_name='Padelapp/marca.html',
            context=contexto,
        )
        return http_response


