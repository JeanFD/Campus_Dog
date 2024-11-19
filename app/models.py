from django.db import models
from stdimage.models import StdImageField

class Pessoas(models.Model):
    nome = models.CharField(max_length=100, default='')
    email = models.CharField(max_length=100, default = '')
    telefone = models.CharField(max_length=15, default = 0)
    img = StdImageField('Fotos', upload_to='fotos_voluntarios/', variations={'thumb': (1080, 1080, True)})
    class Meta:
        abstract = True
    def __str__(self):
        return self.nome
    


# desenvolvedores

class Desenvolvedor(Pessoas):
    linkedin = models.CharField(max_length=100, default='')
    class Meta:
        verbose_name = "Desenvolvedor"
        verbose_name_plural = "Desenvolvedores"


class Raca(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Raça")
# class Genero(models.Model):

# class Vacinas(models.Model):

class Animal(models.Model):
    nome = models.CharField(max_length=20)
    raca = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    idade = models.IntegerField()
    vacinado = models.BooleanField(default=False)
    descricao = models.TextField(max_length=56)
    descricao_completa = models.TextField()
    foto = StdImageField('Fotos', upload_to='fotos_animais/', variations={'thumb': (1080, 1080, True)})
    class Meta:
        verbose_name = "Doguinho"
        verbose_name_plural = "Doguinhos"
    def __str__(self):
        return self.nome

