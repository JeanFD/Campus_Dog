from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('doacoes', views.doacoes, name='doacoes'),
    path('saiba_mais', views.saiba_mais, name='saiba_mais'),
    path('contato', views.contato, name='contato'),
    path('animal/<int:id>', views.detalhes_animal, name='detalhes_animal'),
    path('teste', views.teste, name='teste'),
]
