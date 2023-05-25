from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from datetime import datetime
from typing import Dict
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from PadelApp.models import Jugadores, Circuito, Marca, Comentario
from PadelApp.forms import JugadoresForm, CircuitoForm, MarcaForm, ComentarioForm
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
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
    

class JugadorCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Jugadores
    permission_required = "jugadores.add_jugador"
    template_name = "PadelApp/jugadores_form.html"
    fields = ["nombre", "apellido", "nacionalidad", "edad","circuito",  "marca"]
    success_url = reverse_lazy("listar_jugadores")

    def form_valid(self, form):
        form.instance.creador = self.request.user
        return super().form_valid(form)


class JugadorDetailView(DetailView):
    model = Jugadores
    success_url = reverse_lazy('listar_jugadores')


class JugadorUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Jugadores
    permission_required = "jugadores.change_jugador"
    template_name = "PadelApp/jugadores_form.html"
    fields = ("nombre", "apellido", "nacionalidad", "edad","circuito",  "marca" )
    success_url = reverse_lazy('listar_jugadores')

class JugadorDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Jugadores
    permission_required = "jugadores.delete_jugador"
    template_name = "PadelApp/jugadores_confirm_delete.html"
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
    
def about_me(request):
    return render(request, '´PadelApp/about_me.html')

class CircuitoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Circuito
    permission_required = "circuito.add_circuito"
    template_name = "PadelApp/circuito_form.html"
    fields = ['nombre', 'alcance', 'ranking_premios', 'cant_torneos']
    success_url = reverse_lazy('listar_circuitos')

    def form_valid(self, form):
        form.instance.creador = self.request.user
        return super().form_valid(form)

class CircuitoDetailView(DetailView):
    model = Circuito
    success_url = reverse_lazy('listar_circuitos')

class CircuitoUpdateView(LoginRequiredMixin, PermissionRequiredMixin , UpdateView):
    model = Circuito
    permission_required = "circuito.change_circuito"
    template_name = "PadelApp/circuito_form.html"
    fields = ( "nombre", "alcance", "ranking_premios", "cant_torneos" )
    success_url = reverse_lazy('listar_circuitos')

class CircuitoDeleteView(LoginRequiredMixin, PermissionRequiredMixin , DeleteView):
    model = Circuito
    permission_required = "circuito.delete_circuito"
    template_name = "PadelApp/circuito_confirm_delete.html" 
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

class MarcaCreateView(LoginRequiredMixin, PermissionRequiredMixin  , CreateView):
    model = Marca
    permission_required = "marca.add_marca"
    template_name = "PadelApp/marca_form.html"
    fields = [ 'nombre', 'origen' ]
    success_url = reverse_lazy('listar_marcas')

    def form_valid(self, form):
        form.instance.creador = self.request.user
        return super().form_valid(form)

class MarcaDetailView(DetailView):
    model = Marca
    success_url = reverse_lazy('listar_marcas')

class MarcaUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Marca
    permission_required = "marca.change_marca"
    template_name = "PadelApp/marca_form.html"
    fields = ( "nombre", "origen" )
    success_url = reverse_lazy('listar_marcas')

class MarcaDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Marca
    permission_required = "marca.delete_marca"
    template_name = "PadelApp/marca_confirm_delete.html"
    success_url = reverse_lazy('listar_marcas')


#VISTAS COMENTARIO




class ComentarioCreateView(LoginRequiredMixin, CreateView):
    model = Comentario
    fields = ['titulo', 'texto', 'imagen']
    template_name = 'Padelapp/comentario_form.html'
    
    success_url = reverse_lazy('listar_comentarios')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)




class ComentarioListView(ListView):
    model = Comentario
    template_name = 'PadelApp/comentario.html'


class ComentarioDetailView(DetailView):
    model = Comentario
    success_url = reverse_lazy('listar_comentarios')

class ComentarioUpdateView(LoginRequiredMixin, UpdateView):
    model = Comentario
    fields = ['titulo', 'texto', 'imagen']
    template_name = 'PadelApp/comentario_form.html'
    success_url = reverse_lazy('listar_comentarios')

class ComentarioDeleteView(LoginRequiredMixin, DeleteView):
    model = Comentario
    template_name = 'PadelApp/comentario_confirm_delete.html'
    success_url = reverse_lazy('listar_comentarios')

class SearchComentarioTitulo(ListView):
    model = Comentario
    template_name = 'PadelApp/comentario.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Comentario.objects.filter(titulo__icontains=query)
        return object_list



class SearchComentarioTexto(ListView):
    model = Comentario
    template_name = 'PadelApp/comentario.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Comentario.objects.filter(texto__icontains=query)
        return object_list



##FALTA LA VISTA DE BUSQUEDA DE COMENTARIOS, PODEMOS HACER UN PAR, POR USUARIO Y POR ICONTAIN, GENERAL. 
## VER COMO ESTÁN HECHOS EL RESTO, QUE ESTÁ PASANDO AHI. 
## VER PORQUE NO ESTOY PUDIENDO BORRAR. 
