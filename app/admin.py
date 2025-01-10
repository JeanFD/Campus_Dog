from django.contrib import admin
from .models import *

class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'raca', 'idade', 'vacinado')
    search_fields = ('nome', 'raca')

admin.site.register(Animal)
admin.site.register(Desenvolvedor)
admin.site.register(CustomUsuario)