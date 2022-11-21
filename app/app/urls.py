
from django.contrib import admin
from django.urls import path, include
#from algo1 import views
#from alg1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('prueba3.urls')),
]