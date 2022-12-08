from WebAdminRadio.models import Encuesta, Pregunta, OpcionPregunta, Emisora
from WebAdminRadio.forms import EncuestaForm, PreguntaEncuestaForm, OpcionPreguntaEncuestaForm
from WebAdminRadio.views import agregarImagen

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

def _editar_preguntas_encuesta(encuesta: Encuesta, preguntas_diccionario: List[dict]):
    """
    
    """

    for pregunta in preguntas_diccionario:
        
        if not pregunta['id_encuesta']:
            pregunta['id_encuesta'] = encuesta.id

        pregunta_form = PreguntaEncuestaForm(pregunta, 
            instance=encuesta.preguntas_set.get(id=pregunta.get('id')))

        opciones: List[dict] = pregunta.get('opciones')

        if not pregunta_form.is_valid():
            return pregunta_form.errors
        
        pregunta_editar = pregunta_form.save()

        for opcion_preg in opciones:
            
            if opcion_preg['pregunta']:
                opcion_preg['pregunta'] = pregunta_editar.id

            opcion_form = OpcionPreguntaEncuestaForm(opcion_preg, 
                instance=pregunta_editar.opciones_set.get(id=opcion_preg.get('id')))

            if not opcion_form.is_valid():
                return opcion_form.errors
            
            opcion_form.save()

    return encuesta

def encuestas(request: HttpRequest):
    context = {'title': 'Encuestas'}
    return render(request, 'webAdminRadio/encuestas.html', context)

# def agregar_encuesta(request: HttpRequest):
#     context = {
#         'title': 'Agregar Encuesta',
#         'emisoras': Emisora.objects.filter(estado=True)
#     }

#     if request.method == 'POST':
#         preguntas = json.loads(request.POST.pop('preguntas'))
#         encuesta_form = EncuestaForm(request.POST)
        
#         if not encuesta_form.is_valid(): # Si el formulario no es valido enviamos un mensaje de errores a la pagina
#             context['error'] = encuesta_form.errors
#             return render(request, 'webAdminRadio/agregar_encuesta.html', context)

#         nueva_encuesta = encuesta_form.save()
#         nueva_encuesta.imagen = agregarImagen(request, request, 'imagenes-encuesta/')
#         nueva_encuesta.save()

#         for pregunta_encuesta in preguntas:
#             opciones = pregunta_encuesta.pop('opciones')
            
#             pregunta_encuesta['id_encuesta'] = nueva_encuesta.id
#             pregunta_form = PreguntaEncuestaForm(pregunta_encuesta)
            
#             if pregunta_form.is_valid():
#                 nueva_pregunta = pregunta_form.save()
                
#                 for opcion_pregunta in opciones:
#                     opcion_pregunta['pregunta'] = nueva_pregunta.id
#                     opcion_form = OpcionPreguntaEncuestaForm(opcion_pregunta)
                    
#                     if opcion_form.is_valid():
#                         opcion_form.save()
#                     else:
#                         context['error'] = opcion_form.errors
#                         return render(request, 'webAdminRadio/agregar_encuesta.html', context)

#             else:
#                 context['error'] = pregunta_form.errors
#                 return render(request, 'webAdminRadio/agregar_encuesta.html', context)
                
#     return render(request, 'webAdminRadio/agregar_encuesta.html', context)

def agregar_encuesta(request: HttpRequest):
    context = {
        'title': 'Agregar Encuesta',
        'emisoras': Emisora.objects.filter(estado=True)
    }

    if request.method == 'POST':
        preguntas = json.loads(request.POST.get('preguntas'))

        print(preguntas)

        encuesta_form = EncuestaForm(request.POST)
        
        if not encuesta_form.is_valid(): # Si el formulario no es valido enviamos un mensaje de errores a la pagina
            context['error'] = encuesta_form.errors

            print('Errores encuesta: ', encuesta_form.errors)
            return render(request, 'webAdminRadio/agregar_encuesta_preguntas.html', context)

        nueva_encuesta = encuesta_form.save()
        nueva_encuesta.imagen = agregarImagen(request, request, 'imagenes-encuesta/')
        nueva_encuesta.save()

        resultado = _agregar_preguntas_encuesta(nueva_encuesta, preguntas)

        print(isinstance(resultado, ErrorDict))

        if isinstance(resultado, ErrorDict):
            context['error'] = resultado
            return render(request, 'webAdminRadio/agregar_encuesta_preguntas.html', context)

        context['success'] = 'Se agrego la encuesta con exito'
                
    return render(request, 'webAdminRadio/agregar_encuesta_preguntas.html', context)

# def editar_encuesta(request: HttpRequest, id_encuesta):
#     encuesta_editar = Encuesta.objects.get(id=id_encuesta)

#     context = {
#         'title': 'Agregar Encuesta',
#         'emisoras': Emisora.objects.filter(estado=True),
#         'encuesta': encuesta_editar
#     }

#     if request.method == 'POST':
#         preguntas = json.loads(request.POST.pop('preguntas'))
#         encuesta_form = EncuestaForm(request.POST, instance=encuesta_editar)
        
#         if not encuesta_form.is_valid(): # Si el formulario no es valido enviamos un mensaje de errores a la pagina
#             context['error'] = encuesta_form.errors
#             return render(request, 'webAdminRadio/agregar_encuesta.html', context)

#         nueva_encuesta = encuesta_form.save()

#         if(request.FILES.get('archivo', 'no') != 'no'):
#             nueva_encuesta.imagen = agregarImagen(request, request, 'imagenes-encuesta/')

#         for pregunta_encuesta in preguntas:
#             opciones = pregunta_encuesta.pop('opciones')
            
#             pregunta_encuesta['id_encuesta'] = nueva_encuesta.id
#             pregunta_form = PreguntaEncuestaForm(pregunta_encuesta, instance=encuesta_editar.preguntas_set.get(id=pregunta_encuesta.get('id')))
            
#             if pregunta_form.is_valid():
#                 pregunta_editar = pregunta_form.save()
                
#                 for opcion_pregunta in opciones:
#                     opcion_pregunta['pregunta'] = pregunta_editar.id
#                     opcion_form = OpcionPreguntaEncuestaForm(opcion_pregunta, instance=pregunta_editar.opciones_set.get(id=pregunta_encuesta.get('id')))
                    
#                     if opcion_form.is_valid():
#                         opcion_form.save()
#                     else:
#                         context['error'] = opcion_form.errors
#                         return render(request, 'webAdminRadio/agregar_encuesta.html', context)

#             else:
#                 context['error'] = pregunta_form.errors
#                 return render(request, 'webAdminRadio/agregar_encuesta.html', context)

#         nueva_encuesta.save()
                
#     return render(request, 'webAdminRadio/agregar_encuesta.html', context)


def editar_encuesta(request: HttpRequest, id_encuesta):
    encuesta_editar = Encuesta.objects.get(id=id_encuesta)
    context = {
        'title': 'Agregar Encuesta',
        'emisoras': Emisora.objects.filter(estado=True),
        'encuesta': encuesta_editar
    }

    if request.method == 'POST':
        preguntas = json.loads(request.POST.pop('preguntas'))
        encuesta_form = EncuestaForm(request.POST, instance=encuesta_editar)
        
        if not encuesta_form.is_valid(): # Si el formulario no es valido enviamos un mensaje de errores a la pagina
            context['error'] = encuesta_form.errors
            return render(request, 'webAdminRadio/editar_encuesta.html', context)

        encuesta_editada = encuesta_form.save()

        if(request.FILES.get('archivo', 'no') != 'no'):
            encuesta_editada.imagen = agregarImagen(request, request, 'imagenes-encuesta/')
            encuesta_editada.save()

        resultado = _editar_preguntas_encuesta(encuesta_editada, preguntas)

        if isinstance(resultado, ErrorDict):
            context['error'] = resultado
            return render(request, 'webAdminRadio/editar_encuesta.html', context)
                
    return render(request, 'webAdminRadio/editar_encuesta.html', context)
