"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
        path('', views.index, name='index'),
        path('estudiante/<int:id>', views.obtener_estudiante,
            name='obtener_estudiante'),
        path('crear/estudiante', views.crear_estudiante,
            name='crear_estudiante'),
        path('editar/estudiante/<int:id>', views.editar_estudiante,
            name='editar_estudiante'),
        path('eliminar/estudiante/<int:id>', views.eliminar_estudiante,
            name='eliminar_estudiante'),
        # Rutas para el manejo de paises   
        path('paises/', views.listar_paises, 
             name='listar_paises'),
        path('paises/crear/', views.crear_pais, 
             name='crear_pais'),
 ]
