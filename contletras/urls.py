from django.urls import path
from . import views

urlpatterns = [
    path('numero_letras/', views.contar_as_letras, name='contador_de_letras'),
]