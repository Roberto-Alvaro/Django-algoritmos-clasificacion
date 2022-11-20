


"""from django.shortcuts import render
from prueba1.models import Dato

def muestra_datos(request):
    consulta = Dato.objects.all()
    LisSum = suma(consulta)
    contexto = zip(consulta, LisSum)

    return render(request, 'prueba1/index_algo1.html', {'contexto':contexto})

def suma(val):
    listSum = []
    for i in val:
        listSum.append(i.x1 + i.x3 + i.x4)
    return listSum"""