from django.urls import path
from . import views

urlpatterns = [
    path('', views.muestra_datos, name='prueba1'),
]
