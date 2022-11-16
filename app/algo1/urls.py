from django.urls import path
from . import views

urlpatterns = [
    path('algo1/', views.algoKNN_list, name='algoKNN_list'),
    
]
