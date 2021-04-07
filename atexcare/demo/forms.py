# Django forms
from django.forms import ModelForm
from django import forms
# Django creación de User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Modelos
from .models import Profile


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("username", "password", "email", "first_name", "last_name")
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Ingresa un nombre de usuario',
                'type': 'text',
                'name': 'username'
            }),
            'password': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Ingresa una nueva contraseña',
                'type': 'password',
                'name': 'password'
            }),
            'email': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Ingresa tu correo electrónico',
                'type': 'email',
                'name': 'email'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Ingresa tu(s) nombre(s)',
                'type': 'text',
                'name': 'first_name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Ingresa tu(s) apellido(s)',
                'type': 'text',
                'name': 'last_name'
            }),
        }


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ("user",)
        widgets = {
            'tel_1': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Ingresa tu número de celular',
                'type': 'text'
            }),
            'razon_social': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Ingresa tu razón social',
                'type': 'text'
            }),
            'rfc': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Ingresa tu RFC',
                'type': 'text'
            }),
            'direccion_fiscal': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Ingresa tu dirección fiscal',
                'type': 'text'
            }),
            'ciudad': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Ingresa tu la ciudad de tu dirección fiscal',
                'type': 'text'
            }),
            'estado_fact': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Ingresa el estado de tu dirección fiscal',
                'type': 'text'
            }),
            'tel_2': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Ingresa el número de tu razón social',
                'type': 'text'
            }),
            'correo_fact': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Ingresa el correo electrónico de tu razón social',
                'type': 'text'
            }),
            'cfdi': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Ingresa tu CFDI',
                'type': 'text'
            }),
            'direccion': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Ingresa la dirección de envío',
                'type': 'text'
            }),
            'municipio': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Ingresa el municipio de envío',
                'type': 'text'
            }),
            'estado': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Ingresa el estado de envío',
                'type': 'text'
            }),
            'cp': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Ingresa el código postal a donde se hará el envío',
                'type': 'text'
            }),
            'numero_ext': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Número interior',
                'type': 'number'
            }),
            'numero_int': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Número interior',
                'type': 'number'
            }),
            'entre_calle': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Entre la calle',
                'type': 'text'
            }),
            'entre_calle_2': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Y la calle',
                'type': 'text'
            }),
        }
