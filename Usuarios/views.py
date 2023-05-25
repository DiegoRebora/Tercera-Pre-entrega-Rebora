
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView

from Usuarios.forms import UserRegisterForm, UserUpdateForm, AvatarFormulario
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate
from Usuarios.models import Avatar

from Usuarios.forms import UserRegisterForm

def registro(request):
   if request.method == "POST":
       formulario = UserRegisterForm(request.POST)

       if formulario.is_valid():
           formulario.save()  # Esto lo puedo usar porque es un model form
           url_exitosa = reverse('inicio')
           return redirect(url_exitosa)
   else:  # GET
       formulario = UserRegisterForm()
   return render(
       request=request,
       template_name='Usuarios/registro.html',
       context={'form': formulario},
   )

def login_view(request):
   next_url = request.GET.get('next')
   if request.method == "POST":
       form = AuthenticationForm(request, data=request.POST)

       if form.is_valid():
           data = form.cleaned_data
           usuario = data.get('username')
           password = data.get('password')
           user = authenticate(username=usuario, password=password)
           # user puede ser un usuario o None
           if user:
               login(request=request, user=user)
               if next_url:
                   return redirect(next_url)
               url_exitosa = reverse('inicio')
               return redirect(url_exitosa)
   else:  # GET
       form = AuthenticationForm()
   return render(
       request=request,
       template_name='Usuarios/login.html',
       context={'form': form},
   )



class CustomLogoutView(LogoutView):
   template_name = 'Usuarios/logout.html'

class MiPerfilUpdateView(LoginRequiredMixin, UpdateView):
   form_class = UserUpdateForm
   success_url = reverse_lazy('inicio')
   template_name = 'Usuarios/formulario_perfil.html' ##RECORDAR CAMBIAR ESTE TEMPLATE

   def get_object(self, queryset=None):
       return self.request.user


"""def agregar_avatar(request):
    if request.method == 'POST':
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            avatar, created = Avatar.objects.get_or_create(user=request.user)

            # Verificar si se ha cargado un archivo de imagen en el formulario
            if form.cleaned_data['imagen']:
                avatar.imagen = form.cleaned_data['imagen']
            else:
                # Asignar una imagen predeterminada si no se ha cargado ninguna imagen
                avatar.imagen = 'static/pame.jpg'
                print(avatar.imagen)

            avatar.save()
            return redirect('inicio')
    else:
        form = AvatarFormulario()
    return render(request, 'Usuarios/agregar_avatar.html', {'form': form})
"""
def agregar_avatar(request):
    if request.method == 'POST':
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            avatar, created = Avatar.objects.get_or_create(user=request.user)
            # Verificar si se ha cargado un archivo de imagen en el formulario
            if form.cleaned_data['imagen']:
                avatar.imagen = form.cleaned_data['imagen']
            else:
                # Asignar una imagen predeterminada si no se ha cargado ninguna imagen
                avatar.imagen = 'default_avatar.jpg'
                print(avatar.imagen)
            avatar.save()
            return redirect('inicio')
    else:
        form = AvatarFormulario()
    return render(request, 'Usuarios/agregar_avatar.html', {'form': form})