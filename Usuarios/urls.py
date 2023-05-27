from django.contrib import admin
from django.urls import path
from Usuarios.views import registro
from Usuarios.views import login_view, CustomLogoutView, MiPerfilUpdateView, agregar_avatar


    
    
urlpatterns = [
    path("registro/", registro, name="registro" ),
    path("login/", login_view, name="login" ),
    path("logout/", CustomLogoutView.as_view(), name="logout" ),
    path("profile/", MiPerfilUpdateView.as_view(), name="editar_usuario" ),
    path("agregar_avatar/", agregar_avatar, name="agregar_avatar" ),

]
