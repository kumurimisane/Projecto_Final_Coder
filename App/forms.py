from django import forms
from .models import *
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class CartasFormulario(forms.ModelForm):
    class Meta:
        model = Cartas
        fields = ['nombre', 'tipo', 'nivel','ataque', 'defensa','descripcion','imagen']

class MazoFormulario(forms.ModelForm):
    class Meta:
        model = Mazo
        fields = ['nombre', 'tipo', 'carta_principal', 'cantidad_de_cartas', 'descripcion','imagen']

class TorneoFormulario(forms.ModelForm):
    class Meta:
        model = Torneo
        fields = ['nombre_torneo', 'cantidad_participantes', 'lugar_del_torneo', 'premio', 'codigo_de_torneo', 'imagen']

class UserEditForm(UserChangeForm):
   
    password = forms.CharField(
       help_text="",
       widget=forms.HiddenInput, required=False
   )
    
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Password", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']
        
class ContactenosFormulario(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'apellido', 'email', 'mensaje']
        
def clean_password(self):
    print(self.cleaned_data)
    
    password2 = self.cleaned_data['password2']
    if password2 != self.cleaned_data['password1']:
        raise forms.ValidationError('Los password no coinciden!')
    return password2