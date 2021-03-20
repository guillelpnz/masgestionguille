from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('anadir-cliente', views.anadir_cliente, name='anadir-cliente'),
    path('ver-cliente', views.ver_cliente, name='ver-cliente'),
    path('editar-cliente', views.editar_cliente, name='editar-cliente'),
    path('buscador-clientes', views.buscador_clientes, name='buscador-clientes'),
    path('gestion-comerciales', views.gestion_comerciales, name='gestion-comerciales'),
    path('csv-gestion-comerciales', views.descargar_csv_comerciales, name='csv-gestion-comerciales'),
]

