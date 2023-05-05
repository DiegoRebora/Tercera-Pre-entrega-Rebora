from django.db import models

# Create your models here.
class Jugadores(models.Model):
    nombre =  models.CharField(max_length=64)
    apellido =  models.CharField(max_length=64)
    nacionalidad =  models.CharField(max_length=64)
    edad = models.DateField()
    circuito = models.CharField(max_length=64)
    marca = models.CharField(max_length=64)

class Circuito(models.Models):
    nombre = models.CharField(max_length=64)
    alcance = models.CharField(max_length=64)
    ranking_premios = models.IntegerField()
    cant_torneos = models.IntegerField()

class Marca(models.Model):
    nombre = models.CharField(max_length=64)
    origen = models.CharField(max_length=64)
