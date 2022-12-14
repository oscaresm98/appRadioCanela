from WebAdminRadio.models import Encuesta, Pregunta, OpcionPregunta, Emisora
from WebAdminRadio.forms import EncuestaForm, PreguntaEncuestaForm, OpcionPreguntaEncuestaForm
from WebAdminRadio.views import agregarImagen

from api.serializers import PreguntaAdminSerializer

from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.forms.utils import ErrorDict

from typing import List
import json


def _agregar_preguntas_encuesta(encuesta: Encuesta, preguntas_diccionario: List[dict]):
    """
    
    """

    for pregunta in preguntas_diccionario:
        pregunta['id_encuesta'] = encuesta.id # Actualizamos el id de la encuesta a la que pertenecera esta pregunta
        pregunta_form = PreguntaEncuestaForm(pregunta)
        opciones: List[dict] = pregunta.get('opciones')

        if not pregunta_form.is_valid():
            return pregunta_form.errors
        
        nueva_pregunta = pregunta_form.save()

        for opcion_preg in opciones:
            opcion_preg['pregunta'] = nueva_pregunta.id # Actualizamos el id de la pregunta a la que pertenecera esta opcion
            opcion_form = OpcionPreguntaEncuestaForm(opcion_preg)

            if not opcion_form.is_valid():
                return opcion_form.errors
            
            opcion_form.save()

    return encuesta

def encuestas(request):
    list_emisoras = Emisora.objects.filter(estado=True)
    context = {
        'title': 'Encuestas',
        'emisoras': list_emisoras,
    }
    return render(request, 'webAdminRadio/encuestas.html', context)

def ver_encuesta(request: HttpRequest, id_encuesta):
    encuesta = Encuesta.objects.get(id=id_encuesta)

    context = {
        'title': 'Ver Encuesta',
        'encuesta': encuesta
    }

    return render(request, 'webAdminRadio/ver_encuesta.html', context)

def agregar_encuesta(request: HttpRequest):
    context = {
        'title': 'Agregar Encuesta',
        'emisoras': Emisora.objects.filter(estado=True)
    }

    if request.method == 'POST':
        preguntas = json.loads(request.POST.get('preguntas'))
        encuesta_form = EncuestaForm(request.POST)
        
        if not encuesta_form.is_valid(): # Si el formulario no es valido enviamos un mensaje de errores a la pagina
            context['error'] = encuesta_form.errors            
            return render(request, 'webAdminRadio/agregar_encuesta.html', context)

        nueva_encuesta: Encuesta = encuesta_form.save()
        nueva_encuesta.imagen = agregarImagen(request, str(nueva_encuesta.id), 'imagenes-encuesta/')
        nueva_encuesta.save()

        resultado = _agregar_preguntas_encuesta(nueva_encuesta, preguntas)

        if isinstance(resultado, ErrorDict):
            context['error'] = resultado
            nueva_encuesta.delete()
            return render(request, 'webAdminRadio/agregar_encuesta.html', context)

        context['success'] = 'Se agregó la encuesta con éxito'
                
    return render(request, 'webAdminRadio/agregar_encuesta.html', context)


def editar_encuesta(request: HttpRequest, id_encuesta):
    encuesta_editar = Encuesta.objects.get(id=id_encuesta)
    # print(json.dumps(PreguntaAdminSerializer(instance=encuesta_editar.preguntas_set.all(), many=True).data, indent=4))

    context = {
        'title': 'Editar Encuesta',
        'emisoras': Emisora.objects.filter(estado=True),
        'encuesta': encuesta_editar,        
        'preguntas': json.dumps(PreguntaAdminSerializer(instance=encuesta_editar.preguntas_set.all(), many=True).data)
    }

    if request.method == 'POST':
        preguntas = json.loads(request.POST.get('preguntas'))
        encuesta_form = EncuestaForm(request.POST, instance=encuesta_editar)
        
        if not encuesta_form.is_valid(): # Si el formulario no es valido enviamos un mensaje de errores a la pagina
            context['error'] = encuesta_form.errors
            return render(request, 'webAdminRadio/editar_encuesta.html', context)

        encuesta_editada = encuesta_form.save()

        if(request.FILES.get('archivo', 'no') != 'no'):
            encuesta_editada.imagen = agregarImagen(request, str(encuesta_editada.id), 'imagenes-encuesta/')
            encuesta_editada.save()

        encuesta_editada.preguntas_set.all().delete() # Borramos las preguntas anteriores para insertar y actualizar nuevas

        resultado = _agregar_preguntas_encuesta(encuesta_editada, preguntas)

        if isinstance(resultado, ErrorDict):
            context['error'] = resultado
            return render(request, 'webAdminRadio/editar_encuesta.html', context)

        context['success'] = 'Se editó la encuesta con éxito'
                
    return render(request, 'webAdminRadio/editar_encuesta.html', context)

def eliminar_encuesta(request: HttpRequest, id_encuesta):
    encuesta_eliminar = Encuesta.objects.get(id=id_encuesta)
    encuesta_eliminar.estado = False
    encuesta_eliminar.delete()
    messages.success(request, 'La encuesta ha sido eliminada')
    return redirect('encuestas')