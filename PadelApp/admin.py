from django.contrib import admin

# Register your models here.
from PadelApp.models import Jugadores, Circuito, Marca, Comentario

from django.contrib.contenttypes.models import ContentType

admin.site.register(ContentType)

admin.site.register(Jugadores)
admin.site.register(Circuito)
admin.site.register(Marca)
admin.site.register(Comentario)

