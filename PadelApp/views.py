from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from datetime import datetime
from typing import Dict
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from PadelApp.models import Jugadores, Circuito, Marca
from PadelApp.forms import JugadoresForm, CircuitoForm, MarcaForm

# Create your views here.

## VISTAS DE INICIO, VER CUAL Q
def inicio(request):
    contexto = {}
    return render(
        request=request,
        template_name='PadelApp/inicio.html',
        context=contexto,
    )


class JugadorListView(ListView):
    model = Jugadores
    template_name = 'PadelApp/jugadores2.html'


class SearchJugador(ListView):
    model = Jugadores
    template_name = 'PadelApp/jugadores2.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Jugadores.objects.filter(apellido__icontains=query)
        return object_list  
    

class JugadorCreateView(LoginRequiredMixin, CreateView):
    model = Jugadores
    fields = ["nombre", "apellido", "nacionalidad", "edad","circuito",  "marca"]
    success_url = reverse_lazy("listar_jugadores")

    def form_valid(self, form):
        form.instance.creador = self.request.user
        return super().form_valid(form)


class JugadorDetailView(DetailView):
    model = Jugadores
    success_url = reverse_lazy('listar_jugadores')


class JugadorUpdateView(LoginRequiredMixin, UpdateView):
    model = Jugadores
    fields = ("nombre", "apellido", "nacionalidad", "edad","circuito",  "marca" )
    success_url = reverse_lazy('listar_jugadores')

class JugadorDeleteView(LoginRequiredMixin, DeleteView):
    model = Jugadores
    success_url = reverse_lazy('listar_jugadores')




##CLASES BASADAS EN VISTAS, DE CIRCUITOS
class CircuitoListView(ListView):
    model = Circuito
    template_name = 'PadelApp/circuito.html'

class SearchCircuito(ListView):
    model = Circuito
    template_name = 'PadelApp/circuito.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Circuito.objects.filter(nombre__icontains=query)
        return object_list

class CircuitoCreateView(LoginRequiredMixin, CreateView):
    model = Circuito
    fields = ['nombre', 'alcance', 'ranking_premios', 'cant_torneos']
    success_url = reverse_lazy('listar_circuitos')

    def form_valid(self, form):
        form.instance.creador = self.request.user
        return super().form_valid(form)

class CircuitoDetailView(DetailView):
    model = Circuito
    success_url = reverse_lazy('listar_circuitos')

class CircuitoUpdateView(LoginRequiredMixin, UpdateView):
    model = Circuito
    fields = ( "nombre", "alcance", "ranking_premios", "cant_torneos" )
    success_url = reverse_lazy('listar_circuitos')

class CircuitoDeleteView(LoginRequiredMixin, DeleteView):
    model = Circuito
    success_url = reverse_lazy('listar_circuitos')






##CLASES BASADAS EN VISTAS MARCA

class MarcaListView(ListView):
    model = Marca
    template_name = 'PadelApp/marca.html'

class SearchMarca(ListView):
    model = Marca
    template_name = 'PadelApp/marca.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Marca.objects.filter(nombre__icontains=query)
        return object_list

class MarcaCreateView(LoginRequiredMixin, CreateView):
    model = Marca
    fields = [ 'nombre', 'origen' ]
    success_url = reverse_lazy('listar_marcas')

    def form_valid(self, form):
        form.instance.creador = self.request.user
        return super().form_valid(form)

class MarcaDetailView(DetailView):
    model = Marca
    success_url = reverse_lazy('listar_marcas')

class MarcaUpdateView(LoginRequiredMixin, UpdateView):
    model = Marca
    fields = ( "nombre", "origen" )
    success_url = reverse_lazy('listar_marcas')

class MarcaDeleteView(LoginRequiredMixin, DeleteView):
    model = Marca
    success_url = reverse_lazy('listar_marcas')

"""
def listar_marca(request):
    contexto = {'marcas': Marca.objects.all()}
    return render (request, 
                    template_name='PadelApp/marca.html', 
                    context=contexto)







@login_required
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
        return http_response"""


