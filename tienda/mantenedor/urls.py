from django.urls import path
from . import views

app_name = 'mantenedor'

urlpatterns = [
    path('listar', views.listar, name="listar"),
    path('crear', views.crear_producto, name="crear"),
    path('modificar/<int:id>', views.modificar_producto, name="modificar"),
    path('eliminar/<int:id>', views.eliminar_producto, name="eliminar"),
    ]