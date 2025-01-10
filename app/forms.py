from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Animal, CustomUsuario

class CustomLoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Senha',
    }))

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['nome', 'raca', 'genero', 'idade', 'vacinado', 'descricao', 'descricao_completa', 'foto']


class CustomUsuarioForm(forms.ModelForm):
    class Meta:
        model = CustomUsuario
        fields = ['email', 'fone', 'first_name', 'last_name', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'fone': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUsuario.objects.filter(email=email).exists():
            raise forms.ValidationError("Este e-mail já está em uso.")
        return email