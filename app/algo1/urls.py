from django.urls import path
from . import views

urlpatterns = [
    path('algo1/', views.muestra_datos, name='algo1'),
]
