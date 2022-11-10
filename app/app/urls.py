
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prueba1/', include('prueba1.urls')),
    path('', include('inicio.urls')),
    path('', include('algo1.urls')),
    path('', include('algo2.urls')),
    path('', include('algo3.urls')),
]