from django.contrib import admin
from django.urls import path
from PadelApp.views import inicio, listar_marca, listar_jugadores, listar_circuito, crear_jugador, \
    buscar_jugador, crear_circuito, buscar_circuito, crear_marca, buscar_marca
urlpatterns = [
    path("inicio/", inicio, name="inicio" ),
    path("marcas/", listar_marca, name="listar_marcas" ),
    path("jugadores/", listar_jugadores, name="listar_jugadores" ),
    path("circuitos/", listar_circuito, name="listar_circuitos" ),
    path("crear_jugador/", crear_jugador, name="crear_jugador"),
    path("buscar_jugador/", buscar_jugador, name="buscar_jugador"),
    path("crear_circuito/", crear_circuito, name="crear_circuito" ),
    path("buscar_circuito/", buscar_circuito, name="buscar_circuito" ),
    path("crear_marca/", crear_marca, name="crear_marca" ),
    path("buscar_marca/", buscar_marca, name="buscar_marca" ),
]
