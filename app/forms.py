from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Animal, CustomUsuario

class CustomLoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email',
    }))

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['nome', 'raca', 'genero', 'idade', 'vacinado', 'descricao', 'descricao_completa', 'foto']


class CustomUsuarioForm(forms.ModelForm):
    class Meta:
        model = CustomUsuario
        fields = ['email', 'fone', 'first_name', 'last_name', 'password']

    # Adicionando a senha de forma que o usuário não veja ao preencher o formulário
    password = forms.CharField(widget=forms.PasswordInput())

    # Validações adicionais podem ser adicionadas conforme necessário
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUsuario.objects.filter(email=email).exists():
            raise forms.ValidationError("Este e-mail já está em uso.")
        return email