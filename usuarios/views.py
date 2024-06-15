from django.shortcuts import render, redirect
from django.http import HttpResponse
from ecommerce.models import Categoria, Plato
from .models import Proveedor, Venta
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.

banderaPlatoActivo = True

def home(request):
    context={} 
    return render(request, 'usuarios/home.html')

def main(request):
    context={} 
    return render(request, 'usuarios/main.html')

def perfilProveedores(request):
    
    plato = Plato.objects.all()
    categoria = Categoria.objects.all()
    proveedor = Proveedor.objects.all()
    context = {"listaPlatos":plato, "listaCategorias":categoria, "listaProveedores":proveedor}
    return render(request, 'usuarios/proveedor.html', context)


def listarPlatosPorProv(request,prov):  
    replace = prov.replace("-"," ") #se reemplaza el guion por un espacio 
    
    #nombre de la categoria como parametro de entrada
    proveedor = Proveedor.objects.get(nombre_proveedor=prov)
    proveedor = proveedor.id_proveedor
    
    #provedor -> plato -> categoria
    banderaProv = prov
    #platos de la categoria seleccionada comparandola con el id de la categoria
    plato = Plato.objects.filter(id_proveedor=proveedor)
    
    #si proveedor = true -> plato = true -> categoria = true
    context = {"listaPlatos":plato, "listarProveedor":proveedor, "banderaProv":banderaProv}
    return render(request, 'usuarios/proveedor.html', context)


#metodo incompleto
def pausarPlato(request):
    banderaPlatoActivo = True
    plato = Plato.objects.all()
    
    plato = plato.filter(plato_activo=False)
    
    if plato is None:
        banderaPlatoActivo = False
    
    context = {"platos":plato, "banderaPlatoActivo":banderaPlatoActivo}
    #debug para revisar el estado de los platos
    for plato in context['platos']:
        print(f'estado plato: {plato.plato_activo}')
    
    #context = {"listaPlatos": plato, "banderaPlatoActivo": banderaPlatoActivo}
    return render(request, 'usuarios/proveedor.html', context)