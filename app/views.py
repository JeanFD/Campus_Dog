from django.shortcuts import render, get_object_or_404
from .models import Animal

def index(request):
    animais = Animal.objects.all()
    return render(request, 'doguinhos.html', {'animais': animais})

def doacoes(request):
    return render(request, 'doacoes.html')

def saiba_mais(request):
    return render(request, 'saiba_mais.html')

def contato(request):
    return render(request, 'contato.html')