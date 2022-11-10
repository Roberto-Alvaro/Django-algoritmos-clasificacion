from django.urls import path
from . import views

urlpatterns = [
    path('algo2/', views.muestra_datos, name='algo2'),
]
