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
        fields = ['nome', 'raca', 'genero', 'idade', 'vacinado', 'descricao', 'descricao_completa', 'local', 'foto']


class CustomUsuarioForm(forms.ModelForm):
    class Meta:
        model = CustomUsuario
        fields = ['email', 'first_name', 'last_name','fone', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
            'fone': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUsuario.objects.filter(email=email).exists():
            raise forms.ValidationError("Este e-mail já está em uso.")
        return email