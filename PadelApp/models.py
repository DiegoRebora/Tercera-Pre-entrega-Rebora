from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType



# Create your models here.
class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    titulo = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario}, {self.titulo}"
class Jugadores(models.Model):
    nombre =  models.CharField(max_length=64)
    apellido =  models.CharField(max_length=64)
    nacionalidad =  models.CharField(max_length=64)
    edad = models.IntegerField()
    circuito = models.CharField(max_length=64)
    marca = models.CharField(max_length=64, blank=True)
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.nombre}, {self.apellido}"

class Circuito(models.Model):
    nombre = models.CharField(max_length=64)
    alcance = models.CharField(max_length=64)
    ranking_premios = models.IntegerField()
    cant_torneos = models.IntegerField(null=True, blank=True)
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"{self.nombre} | {self.alcance}"
    

class Marca(models.Model):
    nombre = models.CharField(max_length=64)
    origen = models.CharField(max_length=64)
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
   
    
    def __str__(self):
        return f"{self.nombre}"
 
