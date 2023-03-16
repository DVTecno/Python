# tienda_de_celulares//views.py
from django.shortcuts import render

def home(request):
    return render(request, 'tienda_de_celulares//home.html')

def contacto(request):
    return render(request, 'tienda_de_celulares//contacto.html')

def productos(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'tienda_de_celulares//productos.html', context)

# tienda_de_celulares/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('productos/', views.productos, name='productos'),
    path('contacto/', views.contacto, name='contacto'),