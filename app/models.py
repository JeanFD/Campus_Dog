from django.db import models
from stdimage.models import StdImageField

# class Raça(models.Model):

# class Genero(models.Model):

# class Vacinas(models.Model):

class Animal(models.Model):
    nome = models.CharField(max_length=100)
    raca = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    idade = models.IntegerField()
    vacinado = models.BooleanField(default=False)
    descricao = models.TextField()
    descricao_completa = models.TextField()
    foto = StdImageField('Fotos', upload_to='fotos_animais/', variations={'thumb': (1080, 1080, True)})
    def __str__(self):
        return self.nome

