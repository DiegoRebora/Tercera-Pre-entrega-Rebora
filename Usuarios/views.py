
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
           formulario.save()  
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
           
           if user:
               login(request=request, user=user)
               if next_url:
                   return redirect(next_url)
               url_exitosa = reverse('inicio')
               return redirect(url_exitosa)
   else:  
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
   template_name = 'Usuarios/formulario_perfil.html' 

   def get_object(self, queryset=None):
       return self.request.user


def agregar_avatar(request):
    if request.method == 'POST':
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            avatar, created = Avatar.objects.get_or_create(user=request.user)
            
            if form.cleaned_data['imagen']:
                avatar.imagen = form.cleaned_data['imagen']
            else:
                
                avatar.imagen = 'avatares/default_avatar.jpg'
                print(avatar.imagen)
            avatar.save()
            return redirect('inicio')
    else:
        form = AvatarFormulario()
    return render(request, 'Usuarios/agregar_avatar.html', {'form': form})