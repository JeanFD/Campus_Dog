from django.urls import path
from . import views

urlpatterns = [
    path('lista', views.lista_animais, name='lista_animais'),
    path('animal/<int:id>', views.detalhes_animal, name='detalhes_animal'),
    path('doacoes', views.doacoes, name='doacoes'),
    path('saiba_mais', views.saiba_mais, name='saiba_mais'),
    path('contato', views.contato, name='contato'),
    path('', views.index, name='index'),
]
