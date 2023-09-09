from django.urls import path
from .views import *

urlpatterns = [
    path('agrega_curso/<nombre>/<camada>', curso),
    path('lista-cursos/', listar_cursos, name='ListaCursos'),
    path('', inicio, name='Inicio'),
    path('cursos/', cursos, name='Cursos'),
    path('profesores/', profesores, name='Profesores'),
    path('estudiantes/', estudiantes, name='Estudiantes'),
    path('entregables/', entregables, name='Entregables'),
    path('curso-Formulario/', cursoFormulario, name='CursoFormulario'),
    path('busqueda-Camada/', busquedaCamada, name='BusquedaCamada'),
    path('buscar/', buscar, name='Buscar'),
    
]
