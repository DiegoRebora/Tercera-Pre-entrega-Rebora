from django.contrib import admin

# Register your models here.
from PadelApp.models import Jugadores, Circuito, Marca

admin.site.register(Jugadores)
admin.site.register(Circuito)
admin.site.register(Marca)

