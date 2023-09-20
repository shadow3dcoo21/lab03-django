
from django.shortcuts import render
from .models import Proveedor

def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'ventas/proveedores_list.html', {'proveedores': proveedores})

# Create your views here.
