from django.contrib import admin
from .models import *

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'raca', 'idade', 'vacinado')
    search_fields = ('nome', 'raca')
