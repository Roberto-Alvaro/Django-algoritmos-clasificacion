from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
    path('post_list/', views.post_list, name='post_list'),
    path('algoritmo_knn/', views.algoritmo_knn, name='algoritmo_knn'),
    path('algoritmo_cbi/', views.algoritmo_cbi, name='algoritmo_cbi')
]
