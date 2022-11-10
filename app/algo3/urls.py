from django.urls import path
from . import views

urlpatterns = [
    path('algo3/', views.muestra_datos, name='algo3'),
]
