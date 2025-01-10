from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('doacoes', views.doacoes, name='doacoes'),
    path('saiba_mais', views.saiba_mais, name='saiba_mais'),
    path('contato', views.contato, name='contato'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add-animal/', views.add_animal, name='add_animal'),
    path('excluir-animal/', views.excluir_animal, name='excluir_animal'),
]
