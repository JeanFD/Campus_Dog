from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Animal

class CustomLoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email',
    }))

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['nome', 'raca', 'genero', 'idade', 'vacinado', 'descricao', 'descricao_completa', 'foto']