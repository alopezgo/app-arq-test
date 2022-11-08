from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, HttpResponseNotFound
from .models import Producto, Categoria

# Create your views here.

def index(request):

    categorias = Categoria.objects.all()    
    return render(request, 'index.html', { 'categorias': categorias })

def tienda(request):
    page_number = request.GET.get('page')
    allproducts_page = Paginator(Producto.objects.all(), 10)
    
    try:
        allproducts = allproducts_page.page(page_number)
    except PageNotAnInteger:
        allproducts = allproducts_page.page(1)
    except EmptyPage:
        allproducts = allproducts_page.page(1)        
    
    return render(request, 'tienda.html', { 'productos': allproducts })

def show(request, id):
    
    try:
        producto = Producto.objects.get(idProducto=id)
    except Producto.DoesNotExist:
         return HttpResponse(status=404)
    
    return render(request, 'show.html', { 'producto': producto })
    