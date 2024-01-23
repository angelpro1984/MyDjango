from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render


# Create your views here.
# importar las clases de models.py
from administrativo.models import *

# importar los formularios de forms.py 
from administrativo.forms import *

def index(request):
    return HttpResponse("Hola mundo desde Python<br/>%s" % (request.path))
                        
def listadoParroquias(request):

#Listar los registros del Modelo Parroquias,
#obtenidos de la BBDD
    parroquias = Parroquia.objects.all()

    informacion_template={'parroquias':parroquias,'numero_parroquias':len(parroquias)}                        
    return render(request,'listadoParroquias.html',informacion_template)


def listadoParroquiasDos(request):
    """
    Listar los registros del modelo Parroquia, 
    obtenidos de la base de datos.
    """
    parroquias = Parroquia.objects.all()
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    informacion_template = {'parroquias': parroquias, 'numero_parroquias': len(parroquias)}
    return render(request, 'listadoParroquiasDos.html', informacion_template)


def crearParroquia(request):
    """
    """
    if request.method=='POST':
        formulario = ParroquiaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(listadoParroquiasDos)
    else:
        formulario = ParroquiaForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearParroquia.html', diccionario) 


def editarParroquia(request, id):
    """
    """
    parroquia = Parroquia.objects.get(pk=id)
    if request.method=='POST':
        formulario = ParroquiaForm(request.POST, instance=parroquia)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(listadoParroquiasDos)
    else:
        formulario = ParroquiaForm(instance=parroquia)
        diccionario = {'formulario': formulario}

    return render(request, 'editarParroquia.html', diccionario) 