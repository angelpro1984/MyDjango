"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
        path('', views.listadoParroquiasDos, 
            name='listadoParroquiasDos'),
        path('inicio', views.index, name='index'),
        path('listado-parroquias', views.listadoParroquias, 
            name='listadoParroquias'),
        path('listado-parroquias-dos', views.listadoParroquiasDos, 
            name='listadoParroquiasDos'),
         path('crear-parroquia', views.crearParroquia, 
            name='crearParroquia'),
        path('editar-parroquia/<int:id>', views.editarParroquia, 
            name='editarParroquia'),
 
 
 
 ]