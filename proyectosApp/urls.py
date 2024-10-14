from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index),
    path('proyectos/', views.listadoProyectos),
    path('agregarProyecto/', views.agregarProyecto),
    path('eliminarProyecto/<int:id>', views.eliminarProyecto),
    path('actualizarProyecto/<int:id>', views.actualizarProyecto),
]