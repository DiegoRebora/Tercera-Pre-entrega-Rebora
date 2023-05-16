from django.contrib import admin
from django.urls import path
from Usuarios.views import registro
from Usuarios.views import login_view, CustomLogoutView

    
    
urlpatterns = [
    path("registro/", registro, name="registro" ),
    path("login/", login_view, name="login" ),
    path("logout/", CustomLogoutView.as_view(), name="logout" ),

]
