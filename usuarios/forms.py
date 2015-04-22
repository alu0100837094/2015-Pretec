from django import forms
from django.db import models


class RegistroForm(forms.Form):
  nombre = forms.CharField(label='Nombre', max_length=30, min_length=2)
  apellidos = forms.CharField(label = 'Aplellidos', max_length = 50)
  pseudonimo = forms.CharField(label= 'Pseudonimo', max_length='20', min_length='5')
  correo = forms.EmailField(label='correo')
  password1 = forms.CharField(label='Contrasena', widget=forms.PasswordInput)
  password2 = forms.CharField(label='Repita la contrasena', widget=forms.PasswordInput)
  date = forms.DateField() #---> Esta dando fallos, dice que no hay atributo dateField() en models
