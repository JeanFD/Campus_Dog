from django.db import models
from stdimage.models import StdImageField

class Animal(models.Model):
    nome = models.CharField(max_length=100)
    raca = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    idade = models.IntegerField()
    vacinado = models.BooleanField(default=False)
    descricao = models.TextField()
    descricao_completa = models.TextField()
    foto = StdImageField('Imagem', upload_to='produtos', variations={'thumb': (124, 124)})
    

    def __str__(self):
        return self.nome

