from django.contrib import admin
from django.urls import path
from PadelApp.views import inicio, listar_marca, listar_jugadores, listar_circuito, crear_jugador, \
    buscar_jugador, crear_circuito, buscar_circuito, crear_marca, buscar_marca, inicio2, borrar_jugadores, \
    editar_jugadores, CircuitoCreateView, CircuitoUpdateView, CircuitoDeleteView, \
    CircuitoDetailView, CircuitoListView
    
    
    
urlpatterns = [
    path("inicio/", inicio2, name="inicio" ),
    path("marcas/", listar_marca, name="listar_marcas" ),
    path("jugadores/", listar_jugadores, name="listar_jugadores" ),
    #path("circuitos/", listar_circuito, name="listar_circuitos" )#,
    path("crear_jugador/", crear_jugador, name="crear_jugador"),
    path("buscar_jugador/", buscar_jugador, name="buscar_jugador"),
    #path("crear_circuito/", crear_circuito, name="crear_circuito" ),
    path("buscar_circuito/", buscar_circuito, name="buscar_circuito" ),
    path("crear_marca/", crear_marca, name="crear_marca" ),
    path("buscar_marca/", buscar_marca, name="buscar_marca" ),
    path("borrar_jugadores/<int:id>/", borrar_jugadores, name="borrar_jugadores" ),
    path("editar_jugadores/<int:id>/", editar_jugadores, name="editar_jugadores" ),
    #URLS DE CLASES DE VISTA
    path("circuitos/", CircuitoListView.as_view(), name="listar_circuitos" ),
    path("crear-circuitos/", CircuitoCreateView.as_view(), name="crear_circuito" ),
    path("ver-circuitos/<int:pk>/", CircuitoDetailView.as_view(), name="detalle_circuito" ),
    path("editar-circuitos/<int:pk>/", CircuitoUpdateView.as_view(), name="editar_circuito" ),
    path("borrar-circuitos/<int:pk>/", CircuitoDeleteView.as_view(), name="borrar_circuito" ),
]
