from django.shortcuts import render, get_object_or_404, redirect
from .models import Animal, Desenvolvedor
from .forms import AnimalForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomLoginForm

def index(request):
    animais = Animal.objects.order_by('?').all()
    return render(request, 'doguinhos.html', {'animais': animais})

def doacoes(request):
    return render(request, 'doacoes.html')

def saiba_mais(request):
    return render(request, 'saiba_mais.html')

def contato(request):
    desenvolvedores = Desenvolvedor.objects.all()
    return render(request, 'contato.html', {'voluntarios': desenvolvedores})

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Redirecione para a página inicial ou protegida
        else:
            messages.error(request, "Login inválido")
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')

def add_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  # Ajuste para a URL desejada
    else:
        form = AnimalForm()
    return render(request, 'add_animal.html', {'form': form})