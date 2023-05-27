from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from .models import Comentario, Marca
from django.test import TestCase

class ComentarioTest(TestCase):

    def setUp(self):
        # Crear un usuario "Prueba" para utilizar como autor
        self.user = User.objects.create_user(
            username='Prueba', password='Prueba')

    def test_creacion_comentario(self):
        comentario = Comentario(usuario=self.user, titulo="Título prueba", texto="Contenido prueba")
        comentario.save()

        self.assertEqual(Comentario.objects.count(), 1)
        # Comprobar que el usuario es el usuario "Prueba"
        self.assertEqual(comentario.usuario, self.user)
        # Resto de las aserciones...

    def test_comentario_str(self):
        comentario = Comentario(usuario=self.user, titulo="Título prueba", texto="Contenido prueba")
        comentario.save()

        self.assertEqual(str(comentario),
                         "Prueba, Título prueba")

class MarcaTest(TestCase):
    def setUp(self):
        # Crear un usuario "Prueba" para utilizar como creador
        self.user = User.objects.create_user(
            username='Prueba', password='Prueba')

    def test_creacion_marca(self):
        marca = Marca(nombre="Marca de prueba", origen="Origen de prueba", creador=self.user)
        marca.save()

        self.assertEqual(Marca.objects.count(), 1)
        # Comprobar que el creador es el usuario "Prueba"
        self.assertEqual(marca.creador, self.user)
        # Resto de las aserciones...

    def test_marca_str(self):
        marca = Marca(nombre="Marca de prueba", origen="Origen de prueba", creador=self.user)
        marca.save()

        self.assertEqual(str(marca), "Marca de prueba")

