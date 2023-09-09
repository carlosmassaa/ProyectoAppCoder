from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse, HttpRequest
from .forms import CursoFormulario

# Create your views here.
def curso (req, nombre, camada):
    
    curso = Curso(nombre=nombre, camada=camada)
    curso.save()
    
    return HttpResponse(f""" <P> Curso: {curso.nombre} - Camada: {curso.camada} creado con éxito!<P>""")

def listar_cursos(req):

    lista = Curso.objects.all()
    
    return render(req, "lista_cursos.html", {"lista_cursos":lista})

def inicio(req):
    
    return render(req, 'inicio.html')
    return HttpResponse("Vista de Inicio")

def cursos(req):
    return render(req, 'cursos.html')
    return HttpResponse("Vista de Cursos")

def profesores(req):
    return render(req, 'profesores.html')
    return HttpResponse("Vista de Profesores")

def estudiantes(req):
    return render(req, 'estudiantes.html')
    return HttpResponse("Vista de Estudiantes")

def entregables(req):
    return render(req, 'entregables.html')  
    return HttpResponse("Vista de Entregables")

def cursoFormulario(req):
    
    print('method', req.method)
    print('method', req.POST)
    if req.method == 'POST':
        
        miFormulario = CursoFormulario(req.POST)
    
        if miFormulario.is_valid():
            
            data = miFormulario.cleaned_data
            curso = Curso(nombre=data["curso"], camada=data["camada"])
            curso.save()
            return render(req, "inicio.html")
        
    else:
        miFormulario = CursoFormulario()
        return render(req, "cursoFormulario.html", {"miFormulario": miFormulario})

def busquedaCamada(req):
    return render(req, "busquedaCamada.html")

def buscar(req: HttpRequest):
    
    if req.GET["camada"]:
        camada = req.GET["camada"]
        curso = Curso.objects.get(camada=camada)
        return render(req, "resultadosBusqueda.html", {"curso": curso})
    else: 
        return HttpResponse(f"Debe agregar una camada")
        
    return HttpResponse(f"Buscando la camada {req.GET['camada']}")
