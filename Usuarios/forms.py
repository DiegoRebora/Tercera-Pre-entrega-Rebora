
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Usuarios.models import Avatar


class UserRegisterForm(UserCreationForm):
   # Esto es un ModelForm
   password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
   password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

   class Meta:
       model = User
       fields = ['last_name', 'first_name', "username", 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    change_password = forms.BooleanField(label='Cambiar contraseña', required=False)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'email', 'change_password', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        change_password = cleaned_data.get('change_password')
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if change_password:
            if not password1 or not password2:
                raise forms.ValidationError('Debe ingresar una contraseña')
            if password1 != password2:
                raise forms.ValidationError('Las contraseñas no coinciden')

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        change_password = self.cleaned_data.get('change_password')
        password = self.cleaned_data.get('password1')

        if change_password and password:
            user.set_password(password)

        if commit:
            user.save()

        return user

"""class UserUpdateForm(forms.ModelForm):

   class Meta:
       model = User
       fields = ['last_name', 'first_name', 'email']"""

class AvatarFormulario(forms.ModelForm):

   class Meta:
       model = Avatar
       fields = ['imagen']