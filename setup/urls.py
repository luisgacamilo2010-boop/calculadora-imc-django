from django.contrib import admin
from django.urls import path, include # Importamos o 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculadora/', include('calculadora_imc.urls')), # Incluímos o app
    path('contletras/', include('contletras.urls')), # Incluímos o app
]