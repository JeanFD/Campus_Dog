from django.shortcuts import render, get_object_or_404
from .models import Animal, Desenvolvedor

def index(request):
    animais = Animal.objects.all()
    return render(request, 'doguinhos.html', {'animais': animais})

def doacoes(request):
    return render(request, 'doacoes.html')

def saiba_mais(request):
    return render(request, 'saiba_mais.html')

def contato(request):
    desenvolvedores = Desenvolvedor.objects.all()
    return render(request, 'contato.html', {'voluntarios': desenvolvedores})