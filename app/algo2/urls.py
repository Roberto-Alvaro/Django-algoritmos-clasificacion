from django.urls import path
from . import views

urlpatterns = [
    path('algo2/', views.algoKNN_list, name='algo2'),
]
