from django.urls import path, include
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name="index"),
    path('supermercado', views.tienda, name="supermercado"),
    path('contacto', views.contacto, name="contacto"),
    path('nosotros', views.nosotros, name="nosotros"),
    path('miperfil', views.perfil, name="perfil"),
    path('detalle/<int:idProducto>/',views.vista_producto, name="detalle")
    ]