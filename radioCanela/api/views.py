from msilib.schema import RadioButton
from rest_framework import generics
# Social media imports
# FACEBOOK
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
# TWITTER
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from rest_auth.social_serializers import TwitterLoginSerializer

from api.serializers import *
from django.http import HttpResponse, JsonResponse
from WebAdminRadio import models
from accounts.models import Usuario
from . import serializers
from rest_framework import mixins
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import render
from WebAdminRadio.models import *

from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from django.urls import path
from . import views
import datetime
from datetime import timedelta

from rolepermissions.roles import assign_role
from rolepermissions.mixins import HasRoleMixin

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required

#from WebAdminRadio.models import *
# Create your views here.

DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]


def vista(request):
    return HttpResponse('')


# Obtiene el tiempo actual
class ListTime(APIView):
    def get(self, request, format=None):
        dicTime = {'fecha': datetime.datetime.now().date(), 'hora': datetime.datetime.now().time()}
        serializer = serializers.TimeSerializer(dicTime)
        return Response(serializer.data)


# GET: Vista que obtiene Auditorias
class ListAuditoria(generics.ListCreateAPIView):
    queryset = Auditoria.objects.filter(estado=True)
    serializer_class = serializers.AuditoriaSerializer


# GET: Vista que obtiene red social
class redsocial(generics.ListCreateAPIView):
    queryset = RedSocial.objects.filter(estado=True)
    serializer_class = serializers.RedSocialSerializer


# GET: Vista que obtiene red social
class redsocialequipo(generics.ListCreateAPIView):
    queryset = RedSocialEquipo.objects.filter(estado=True)
    serializer_class = serializers.RedSocialEquipoSerializer

# GET: Vista que obtiene red social por id
@api_view()
def redsocial_detalle(request,pk):
    try:
        redSocial = RedSocial.objects.get(id=pk)
    except RedSocial.DoesNotExist: 
        return Response({'Error': 'La red social no existe'}, status=status.HTTP_404_NOT_FOUND)
        
    #GET: Vista en la que se obtiene una red social por id 
    if request.method == 'GET':
        serializers = RedSocialSerializer(redSocial) 
        return Response(serializers.data)

# GET: Vista que obtiene los Concursos
@api_view(['GET'])
def ListConcursos(request):
    concursos = models.Concursos.objects.filter(estado=True)
    serializer = serializers.ConcursosSerializer(concursos, many=True)
    return Response(serializer.data)

#Programa
# Se maneja todos los programas
@api_view(['GET', 'POST','DELETE'])
def programaList(request):
    try:
        programa = Programa.objects.all()
    except Programa.DoesNotExist:
        return Response({'Error': 'El programa no existe'}, status=status.HTTP_400_NOT_FOUND)
    
    #GET: Vista que obtiene todos los programas 
    if request.method == 'GET':
        serializer = ProgramaSerializer(programa, many=True)
        return Response(serializer.data)
        
    #POST: Inserta un programa en la tabla     
    elif request.method == 'POST':
        serializer = ProgramaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    #DELETE: Borra todos los programas de la tabla
    elif request.method == 'DELETE':
        programa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 
#Se maneja los programas por id  
@api_view(['GET', 'PUT','DELETE'])
def programa_detalle(request,pk):
    try:
        programa = Programa.objects.get(id=pk)
    except Programa.DoesNotExist: 
        return Response({'Error': 'La emisora no existe'}, status=status.HTTP_404_NOT_FOUND)
        
    #GET: Vista en la que se obtiene una emisora por id 
    if request.method == 'GET':
        serializers = ProgramaSerializer(programa) 
        return Response(serializers.data) 
        
    
    #PUT: Edita la informacion de una emisora por id     
    elif request.method == 'PUT':
        serializer = ProgramaSerializer(programa, data=request.data)
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        
    #DELETE: Eliminar la emisora por id
    elif request.method == 'DELETE':
        programa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 


#Emisora 
# Se maneja todas las emisoras 
@api_view(['GET', 'POST','DELETE'])
def emisoraList(request):
    
    try:
        emisora = Emisora.objects.all()
    except Emisora.DoesNotExist:
        return Response({'Error': 'La emisora no existe'}, status=status.HTTP_400_NOT_FOUND)
    
    #GET: Vista que obtiene todas las emisoras 
    if request.method == 'GET':
        serializer = EmisoraSerializer(emisora, many=True)
        return Response(serializer.data)
        
    #POST: Inserta una emisora en la tabla     
    elif request.method == 'POST':
        serializer = EmisoraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    #DELETE: Borra todas las emisoras de la tabla
    elif request.method == 'DELETE':
        emisora.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 
#Se maneja emisora por id  
@api_view(['GET', 'PUT','DELETE'])
def emisora_detalle(request,pk):
    try:
        emisora = Emisora.objects.get(id=pk)
    except Emisora.DoesNotExist: 
        return Response({'Error': 'La emisora no existe'}, status=status.HTTP_404_NOT_FOUND)
        
    #GET: Vista en la que se obtiene una emisora por id 
    if request.method == 'GET':
        serializers = EmisoraSerializer(emisora) 
        return Response(serializers.data) 
        
    
    #PUT: Edita la informacion de una emisora por id     
    elif request.method == 'PUT':
        serializer = EmisoraSerializer(emisora, data=request.data)
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        
    #DELETE: Eliminar la emisora por id
    elif request.method == 'DELETE':
        emisora.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
    
# Radio
# Se manejan todas las radios 
@api_view(['GET', 'POST','DELETE'])
def radio_List(request):
    try:
        radio = Radio.objects.all()
    except Radio.DoesNotExist:
        return Response({'Error': 'La radio no existe'}, status=status.HTTP_400_NOT_FOUND)
    
    #GET: Vista que obtiene todas las radios 
    if request.method == 'GET':
        serializer = RadioSerializer(radio, many=True)
        return Response(serializer.data)
        
    
    #POST: Inserta una radio en la tabla     
    elif request.method == 'POST':
        serializer = RadioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    #DELETE: Borra todas las radios de la tabla
    elif request.method == 'DELETE':
        radio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  
      
# Se maneja la radios por id     
@api_view(['GET', 'PUT','DELETE'])
def radio_detalle(request,pk): 
    try: 
        radio = Radio.objects.get(id=pk)
    except Radio.DoesNotExist:
        return Response({'Error': 'La radio no existe'}, status=status.HTTP_404_NOT_FOUND)
 
    #GET: Vista en la que se obtiene una radio por id 
    if request.method == 'GET':
        serializers = RadioSerializer(radio) 
        return Response(serializers.data) 
       
    
    #PUT: Edita la informacion de una radio por id     
    elif request.method == 'PUT':       
        serializer = RadioSerializer(radio, data=request.data)    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #PUT: Elimina una radio por id  
    elif request.method == 'DELETE':
        radio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
        

# Usuarios
@api_view(['GET', 'POST','DELETE','PUT'])
def usuarioList(request):
    
    if request.method == 'GET':
        try:
            usuarios = Usuario.objects.all()
            serializer = UsuarioSerializer(usuarios, many=True)
            return render(request,"webAdminRadio/usuarios.html",{"users":usuarios})
            #return Response(serializer.data)
        except Usuario.DoesNotExist:
            return Response({'Error': 'El usuario no existe'}, status=status.HTTP_400_NOT_FOUND)
        
    elif request.method == 'POST':
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        serializer = UsuarioSerializer(usuarios, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        usuarios.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# Torneos
@api_view(['GET', 'POST','DELETE','PUT'])
def torneosList(request):
    
    if request.method == 'GET':
        try:
            torneo = Torneo.objects.all()
            serializer = TorneosSerializer(torneo, many=True)
            return Response(serializer.data)
        except Torneo.DoesNotExist:
            return Response({'Error': 'El usuario no existe'}, status=status.HTTP_400_NOT_FOUND)
        
    elif request.method == 'POST':
        serializer = TorneosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        serializer = UsuarioSerializer(torneo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        torneo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST','DELETE'])
def equipoList(request):
    
    if request.method == 'GET':
        try:
            equipo = Equipo.objects.filter(estado=True)
            serializer = EquipoSerializer(equipo, many=True)
            return Response(serializer.data)
        except Equipo.DoesNotExist:
            return Response({'Error': 'La emisora no existe'}, status=status.HTTP_400_NOT_FOUND)
        
    elif request.method == 'POST':
        serializer = EquipoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        equipo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ListEquiposPorId(generics.ListAPIView):
    serializer_class = serializers.EquipoSerializer

    def get_queryset(self):
        idteam = self.kwargs['id_equipo']
        queryset = Equipo.objects.filter(id=idteam, estado=True)
        return queryset


# class ListUsuarios(generics.ListAPIView, HasRoleMixin):
#     allowed_roles = 'Locutor'
#     serializer_class = serializers.UsuarioSerializer
#     queryset = Usuario.objects.filter(is_active=True)


# class ListEncuestasActivas(generics.ListAPIView):  # servicio para web, retorna encuestas activas
#     serializer_class = serializers.EncuestaSerializer
#     fecha = datetime.datetime.now().date()
#     hora = datetime.datetime.now().time()
#     encuestas = models.Encuesta.objects.all()
#     for encuesta in encuestas:
#         if encuesta.dia_fin < fecha:
#             encuesta.activo = 'F'
#             encuesta.save()
#         elif (encuesta.dia_fin == fecha) and (encuesta.hora_fin < hora):
#             encuesta.activo = 'F'
#             encuesta.save()
#     q = models.Encuesta.objects.filter(dia_fin__gt=fecha)
#     query = models.Encuesta.objects.filter(dia_fin=fecha).filter(hora_fin__gte=hora)
#     queryset = q.union(query)


# class ListEncuestas(generics.ListAPIView):  # servicio para apps y admin (actualiza estado en vista), retorna encuestas con estado
#     serializer_class = serializers.EncuestaSerializer
#     fecha = datetime.datetime.now().date()
#     hora = datetime.datetime.now().time()
#     encuestas = models.Encuesta.objects.all()
#     for encuesta in encuestas:
#         if encuesta.dia_fin < fecha:
#             encuesta.activo = 'F'
#             encuesta.save()
#         elif (encuesta.dia_fin == fecha) and (encuesta.hora_fin < hora):
#             encuesta.activo = 'F'
#             encuesta.save()
#     queryset = models.Encuesta.objects.all()


# class AutenticarUsuario(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         response = super(AutenticarUsuario, self).post(request, *args, **kwargs)
#         token = Token.objects.get(key=response.data['token'])
#         return Response({'token': token.key, 'id': token.user_id})


# class DeleteVoto(generics.DestroyAPIView):
#     serializer_class = serializers.VotoSerializer
#     queryset = models.Voto.objects.all()

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# class CreateVoto(generics.CreateAPIView):
#     serializer_class = serializers.VotoSerializer

#     def post(self, request, format=None):
#         serializer = serializers.VotoSerializer(data=request.data)
#         if serializer.is_valid():
#             # serializer.save()
#             # return Response(serializer.data, status=status.HTTP_201_CREATED)
#             votos = models.Voto.objects.filter(usuario=serializer.validated_data['usuario'], encuesta=serializer.validated_data['encuesta'])
#             encuesta = serializer.validated_data['encuesta']
#             bandera = 0
#             for respuesta in models.Encuesta.get_respuestas(encuesta):
#                 if serializer.validated_data['respuesta'].id == respuesta['id']:
#                     bandera = 1
#                     break

#             if votos.exists() or bandera == 0:
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#             else:
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)


# class ListVotaciones(generics.ListAPIView):
#     serializer_class = serializers.VotoSerializer
#     queryset = models.Voto.objects.all()


# class ListVotacionesUsuario(generics.ListAPIView):
#     serializer_class = serializers.VotoSerializer

#     def get_queryset(self):
#         idusuario = self.kwargs['id_usuario']
#         queryset = models.Voto.objects.filter(usuario=idusuario)
#         return queryset


# class ListVotacionesEncuesta(generics.ListAPIView):
#     serializer_class = serializers.VotoSerializer

#     def get_queryset(self):
#         idencuesta = self.kwargs['id_encuesta']
#         queryset = models.Voto.objects.filter(encuesta=idencuesta)
#         return queryset


# class ListResultadosEncuesta(generics.ListAPIView):

#     serializer_class = serializers.ResultadoEncuestaSerializer

#     def get_queryset(self):
#         idencuesta = self.kwargs['id_encuesta']
#         q = models.Voto.objects.filter(encuesta=idencuesta)
#         resp = {}
#         indice = {}
#         perc = {}

#         if(models.ResultadosEncuesta.objects.filter(encuesta=idencuesta).exists()):
#             models.ResultadosEncuesta.objects.filter(encuesta=idencuesta).delete()

#         result = models.ResultadosEncuesta.objects.create(encuesta=Encuesta(idencuesta))

#         for i in q:  # obtengo numero de votos por respuesta
#             if i.respuesta not in resp:
#                 resp[i.respuesta] = 1
#                 indice[i.respuesta] = i.respuesta
#             else:
#                 resp[i.respuesta] += 1

#         total = 0
#         for respuesta in resp:  # obtendo porcentaje de votos por respuesta
#             total += resp[respuesta]

#         for respuesta in resp:
#             porcentaje = int(resp[respuesta] / total * 100)
#             perc[respuesta] = str(porcentaje) + "%"
#             models.Resultados.objects.create(resultado=result, id_respuesta=indice[respuesta], respuesta=int(resp[respuesta]), porcentaje=perc[respuesta])

#         queryset = models.ResultadosEncuesta.objects.filter(encuesta=idencuesta)
#         return queryset


# class ListUsuariosLocutores(generics.ListAPIView):
#     serializer_class = serializers.UsuarioSerializer
#     queryset = Usuario.objects.filter(rol='Locutor')


# class ListAdminLocutores(generics.ListAPIView):
#     serializer_class = serializers.UsuarioSerializer
#     locutores = Usuario.objects.filter(rol='Locutor')
#     admin = Usuario.objects.filter(rol='Gerente')
#     cm = Usuario.objects.filter(rol='Community Manager')
#     director = Usuario.objects.filter(rol='Director')
#     queryset = locutores.union(admin, cm, director)


# class ListUsuariosClientes(generics.ListAPIView, HasRoleMixin):
#     serializer_class = serializers.UsuarioSerializer
#     queryset = Usuario.objects.filter(rol__isnull=True)
#     print(queryset.count())


# class ListTorneos(generics.ListAPIView):
#     serializer_class = serializers.TorneoSerializer
#     queryset = models.Torneo.objects.filter(activo=True)


# class ListEquipos(generics.ListAPIView):
#     serializer_class = serializers.EquipoSerializer
#     queryset = models.Equipo.objects.filter(activo=True)


# class ListTransmisiones(generics.ListAPIView):
#     serializer_class = serializers.TransmisionSerializer
#     queryset = models.Transmision.objects.filter(activo=True).order_by('-fecha_evento')


# class ListTransmisionEmisora(generics.ListAPIView):
#     serializer_class = serializers.TransmisionEmisoraSerializer
#     queryset = models.TransmisionEmisora.objects.all()


# class ListTransmisionesPorEmisora(generics.ListAPIView):
#     # serializer_class = serializers.TransmisionEmisoraSerializer
#     serializer_class = serializers.TransmisionSerializer

#     def get_queryset(self):
#         idemisora = self.kwargs['id_emisora']
#         # queryset = models.TransmisionEmisora.objects.filter(emisora=idemisora)
#         fecha = datetime.datetime.now().date()
#         queryset = models.Transmision.objects.filter(transmisionemisora__emisora=idemisora, fecha_evento__gte=fecha).order_by('fecha_evento', 'hora_inicio')
#         # queryset = models.Transmision.objects.filter(emisoras=queryset.values('emisora'), activo=True).order_by('fecha_evento')
#         return queryset


# class ListTransmisionesEnFecha(generics.ListAPIView):
#     serializer_class = serializers.TransmisionSerializer
#     fecha = datetime.datetime.now().date() - timedelta(days=30)
#     queryset = models.Transmision.objects.filter(activo=True, fecha_evento__gte=fecha).order_by('-fecha_evento')
#     # q2 = models.Transmision.objects.filter(activo=True, fecha_evento=datetime.datetime.now().date(), hora_inicio__gte=datetime.datetime.now().time())
#     # queryset = q.union(q2)


# class ListPodcasts(generics.ListAPIView):
#     serializer_class = serializers.PodcastSerializer
#     queryset = models.Podcast.objects.filter(activo=True).order_by('-fecha')


# class ListPodcastsEmisora(generics.ListAPIView):
#     serializer_class = serializers.PodcastEmisoraSerializer
#     queryset = models.PodcastEmisora.objects.all()


# class ListPodcastsPorEmisora(generics.ListAPIView):
#     serializer_class = serializers.PodcastSerializer

#     def get_queryset(self):
#         idemisora = self.kwargs['id_emisora']
#         queryset = models.Podcast.objects.filter(emisora=idemisora)
#         # queryset = models.Podcast.objects.filter(podcastemisora__emisora=idemisora)
#         return queryset


# class ListGaleria(generics.ListAPIView):
#     serializer_class = serializers.GaleriaSerializer
#     queryset = models.Galeria.objects.filter(activo=True)


# class ListGaleriaEmisora(generics.ListAPIView):
#     serializer_class = serializers.GaleriaEmisoraSerializer
#     queryset = models.GaleriaEmisora.objects.all()


# class ListGaleriaPorEmisora(generics.ListAPIView):
#     # serializer_class = serializers.TransmisionEmisoraSerializer
#     serializer_class = serializers.GaleriaSerializer

#     def get_queryset(self):
#         idemisora = self.kwargs['id_emisora']
#         # queryset = models.TransmisionEmisora.objects.filter(emisora=idemisora)

#         queryset = models.Galeria.objects.filter(galeriaemisora__emisora=idemisora)
#         # queryset = models.Transmision.objects.filter(emisoras=queryset.values('emisora'), activo=True).order_by('fecha_evento')
#         return queryset
# ##
# #GET: Vista que obtiene el equipo mediante el id
# #
# #PARAMS: id


# class ListEquiposPorId(generics.ListAPIView):
#     serializer_class = serializers.EquipoSerializer

#     def get_queryset(self):
#         idteam = self.kwargs['id_equipo']
#         queryset = models.Equipo.objects.filter(id=idteam, activo=True)
#         return queryset

# ##
# #GET: Vista que obtiene la transmision mediante la fecha del evento
# #
# #PARAMS: fecha_evento


# class ListTransmisionesPorFecha(generics.ListAPIView):
#     serializer_class = serializers.TransmisionSerializer

#     def get_queryset(self):
#         date = self.kwargs['fecha_evento']
#         queryset = models.Transmision.objects.filter(fecha_evento=date, activo=True)
#         return queryset


# ##
# #GET: Vista que obtiene los segmentos de todas las emisoras


# ##
# #GET: Vista que obtiene los segmentos del dia actual
# #
# #PARAMS: provincia (para escoger los segmentos por provincia)
# #
# class ListSegmentosDiaActual(generics.ListAPIView):
#     serializer_class = serializers.SegmentoSerializerToday

#     def get_queryset(self):
#         provincia = self.request.query_params.get('provincia')
#         day = datetime.datetime.today().weekday()
#         dia_actual = DIAS[day]
#         horariosDelDia = models.Horario.objects.filter(dia=dia_actual)
#         ids_segmentos = models.segmento_horario.objects.filter(idHorario__in=horariosDelDia).distinct()
#         queryset = models.Segmento.objects.filter(pk__in=ids_segmentos.values('idSegmento'), activo='A')
#         if provincia != None:
#             emisoras = models.Emisora.objects.filter(provincia=provincia.capitalize())
#             queryset = queryset.filter(idEmisora__in=emisoras.values('id'), activo='A')

#         return queryset

# ##
# #GET: Vista que obtiene los segmentos del dia actual de una emisora especifica
# #
# #PARAMS: provincia (para escoger los segmentos por provincia)
# #
# class ListSegmentosEmisoraDiaActual(generics.ListAPIView):
#     serializer_class= serializers.SegmentoSerializerToday

#     def get_queryset(self):
#         emisora = self.kwargs['id_emisora']
#         day = datetime.datetime.today().weekday()
#         dia_actual = DIAS[day]
#         horariosDelDia = models.Horario.objects.filter(dia=dia_actual)
#         ids_segmentos = models.segmento_horario.objects.filter(idHorario__in=horariosDelDia).distinct()
#         print(ids_segmentos)
#         queryset = models.Segmento.objects.filter(pk__in=ids_segmentos.values('idSegmento'), idEmisora=emisora, activo='A').distinct().order_by('segmento_horario__idHorario__fecha_inicio')
#         # print(q)
#         return queryset


# ##
# #GET: Vista que obtiene todas las emisoras
# #
# #PARAMS: provincia (para escoger las emisoras por una provincia especifica)
# #
# class ListEmisora(generics.ListCreateAPIView):
#     serializer_class = serializers.EmisoraSerializer

#     def get_queryset(self):
#         provincia = self.request.query_params.get('provincia')
#         if provincia != None:
#             queryset = models.Emisora.objects.filter(provincia=provincia.capitalize(), activo='A')
#         else:
#             queryset = models.Emisora.objects.filter(activo='A')
#         return queryset


# # class RecuperarContrasena(generics.ListAPIView):
# #     serializer_class = serializers.UsuarioSerializer

# #     def get_queryset(self):
# #         correo = self.kwargs['email']
# #         lista = []
# #         lista.append(correo)
# #         desde = settings.EMAIL_HOST_USER
# #         asunto = "Cambio de contraseña"
# #         link = 'http://innovasystem.pythonanywhere.com/usuarios/%s/editarcontrasena' % correo
# #         # link = 'http://127.0.0.1:8000/usuarios/%s/editarcontrasena' % correo
# #         contenido = "<p>Ingresa al sgte link para cambiar tu contraseña: \n</p><a href=%s>ailshdfsfecdsasdkdjfrnfrdhajwfessfakoqdnnndwdd</a>" % link
# #         mail = EmailMessage(asunto, contenido, desde, lista)
# #         mail.content_subtype = "html"  # Main content is now text/html
# #         mail.send()

# #         queryset = Usuario.objects.filter(email=correo, is_active=True)
# #         return queryset

# class CreateContacto(generics.CreateAPIView):
#     serializer_class = serializers.ContactoSerializer

#     def post(self, request, format=None):
#         serializer = serializers.ContactoSerializer(data=request.data)
#         if serializer.is_valid():
#             correo = serializer.validated_data['correo']
#             nombre = serializer.validated_data['nombre']
#             telefono = serializer.validated_data['telefono']
#             mensaje = serializer.validated_data['mensaje']
#             lista = []
#             lista.append(settings.EMAIL_HOST_USER)
#             desde = settings.EMAIL_HOST_USER
#             asunto = "Nueva solicitud de contacto"
#             contenido = "Nombre: %s \nCorreo: %s \nTelefono: %s \nMensaje: %s" % (nombre, correo, telefono, mensaje)
#             mail = EmailMultiAlternatives(subject=asunto, body=contenido, from_email=desde, to=lista)
#             # mail.content_subtype = "html"
#             mail.send()
#             serializer.save()

#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class CreateUser(generics.CreateAPIView):
#     # permission_classes = [AllowAny]
#     serializer_class = serializers.UsuarioSerializer

#     def post(self, request, format=None):
#         serializer = serializers.UsuarioSerializer(data=request.data)
#         if serializer.is_valid():
#             correo = serializer.validated_data['email']
#             username = serializer.validated_data['username']
#             password = serializer.validated_data['password']
#             # rol = serializer.validated_data['rol']
#             lista = []
#             lista.append(correo)
#             desde = settings.EMAIL_HOST_USER
#             asunto = "Bienvenido a App Radio"
#             contenido = "<img src='https://i.ibb.co/wdDWrJJ/bienvenida.png' alt='bienvenida' width='400' height='400' border='0'>" + "<p>\nEstos son tus datos para login: \nUsuario: %s \nContrasena: %s</p>" % (username, password)
#             mail = EmailMultiAlternatives(subject=asunto, body=contenido, from_email=desde, to=lista)
#             mail.content_subtype = "html"
#             mail.send()

#             serializer.save()

#             # idUsuario = Usuario.objects.order_by('-id')[0]
#             # # print(idUsuario)
#             # if rol=='L':
#             #     assign_role(idUsuario, 'locutor')
#             # # print("Se asigno rol Locutor")
#             # elif rol=='A':
#             #     assign_role(idUsuario, 'secretaria')
#             # print("Se asigno rol Secretaria")
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ##
# #GET: Vista que permite actualizar un usuario
# #


# class UpdateUsuario(RetrieveUpdateAPIView):
#     # permission_classes = [IsAuthenticated]
#     queryset = Usuario.objects.all()
#     serializer_class = serializers.Usuario2Serializer

#     # def put(self, request, format=None):
#     #     serializer = serializers.UsuarioSerializer(data=request.data)
#     #     if serializer.is_valid():

#     #         serializer.save()

#     #         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ResetPassword(RetrieveUpdateAPIView):

#     serializer_class = serializers.reseteoDPaswword

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             user = Usuario.objects.get(username=serializer.data.get("username"))
#             user.set_password(serializer.data.get("password"))
#             user.save()
#             response = {
#                 'valid': 'OK',
#                 'code': status.HTTP_200_OK,
#                 'message': 'Password updated successfully',
#                 'data': []
#             }

#             return Response(response)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ##
# #GET: Vista que obtiene el usuario mediante el id
# #
# #PARAMS: id

# class ListUsuariosPorId(generics.ListAPIView):
#     serializer_class = serializers.UsuarioSerializer

#     def get_queryset(self):
#         iduser = self.kwargs['id_usuario']
#         queryset = Usuario.objects.filter(id=iduser, is_active=True)
#         return queryset


# class CreateUserRedes(generics.CreateAPIView):

#     serializer_class = serializers.UsuarioRedesSerializer

#     def post(self, request, format=None):
#         serializer = serializers.UsuarioRedesSerializer(data=request.data)
#         if serializer.is_valid():

#             serializer.save()

#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # class CreateUserA(APIView, mixins.CreateModelMixin):
# #     permission_classes = (AllowAny,)

# #     def post(self, request, format=None):
# #         serializer = serializers.UsuarioSerializer(data=request.data)
# #         if serializer.is_valid():

# #             correo = serializer.validated_data['email']
# #             desde = settings.EMAIL_HOST_USER
# #             asunto = "Bienvenido a App Radio"
# #             contenido = "Este es un mensaje de prueba para representar el registro de usuario"
# #             mail = EmailMessage(asunto, contenido, desde, ['juanjofs96@gmail.com'])
# #             mail.send(fail_silently=False)
# #             send_mail(asunto, contenido, desde, ['juanjofs96@gmail.com'], fail_silently=False)

# #             #llamar la funcion
# #             enviarmail = EnviarEmail()
# #             enviarmail.enviar_correo(asunto, contenido,desde, correo)


# #             serializer.save()

# #             return Response(serializer.data, status=status.HTTP_201_CREATED)

# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class FacebookLogin(SocialLoginView):
#     adapter_class = FacebookOAuth2Adapter


# class TwitterLogin(SocialLoginView):
#     serializer_class = TwitterLoginSerializer
#     adapter_class = TwitterOAuthAdapter

# # Lista los segmentos de una emisora
# class ListEmisoraSegmentos(generics.ListAPIView):
#     serializer_class = serializers.SegmentoSerializerFull

#     def get_queryset(self):
#         emisora = self.kwargs['id_emisora']
#         return models.Segmento.objects.filter(idEmisora=emisora, activo='A')

# # Lista un segmento de una emisora
# class ListEmisoraSegmento(generics.RetrieveAPIView):
#     serializer_class = serializers.SegmentoSerializerFull

#     def get_object(self):
#         emisora = self.kwargs['id_emisora']
#         segmento = self.kwargs['id_segmento']
#         return models.Segmento.objects.get(id=segmento, idEmisora=emisora, activo='A')


# # class ListLocutoresEmisora(generics.ListAPIView):
# #     serializer_class= serializers.LocutoresSerializer

# #     def get_queryset(self):
# #         id_emisora= self.kwargs['id_emisora']
# #         results= models.segmento_usuario.objects.filter(idSegmento=id_segmento)
# #         return Usuario.objects.filter(pk__in=results.values('idUsuario'))

# class ListLocutores(generics.ListAPIView):
#     serializer_class = serializers.LocutoresSerializer

#     def get_serializer_context(self):
#         return {'segmento': self.kwargs['id_segmento']}

#     def get_queryset(self):
#         segmento = self.kwargs['id_segmento']
#         return Usuario.objects.filter(id__in=models.segmento_usuario.objects.filter(idSegmento=segmento).values('idUsuario'), is_active=True)


# class ListLocutoresSegmento(generics.ListAPIView):
#     serializer_class = serializers.LocutoresSegmentoSerializer

#     def get_queryset(self):
#         id_segmento = self.kwargs['id_segmento']
#         results = models.segmento_usuario.objects.filter(idSegmento=id_segmento)
#         return Usuario.objects.filter(pk__in=results.values('idUsuario'), is_active=True)


# class ListPublicidad(generics.ListAPIView):
#     serializer_class = serializers.PublicidadSerializer

#     def get_serializer_context(self):
#         return {'segmento': self.kwargs['id_segmento']}

#     def get_queryset(self):
#         segmento = self.kwargs['id_segmento']
#         return models.Publicidad.objects.filter(id__in=models.segmento_publicidad.objects.filter(idSegmento=segmento).values('idPublicidad'), estado='A')


# class ListFrecuencias(generics.ListAPIView):
#     serializer_class = serializers.FrecuenciaSerializer

#     def get_queryset(self):
#         publicidad = self.kwargs['id_publicidad']
#         return models.Frecuencia.objects.filter(id__in=models.frecuencia_publicidad.objects.filter(idPublicidad=publicidad))

# ##
# #GET: Vista que obtiene los telefonos de una emisora


# class ListTelefonosEmisora(generics.ListCreateAPIView):
#     serializer_class = serializers.TelefonoEmisoraSerializer

#     def get_queryset(self):
#         idemisora = self.kwargs['id_emisora']
#         return models.Telefono_emisora.objects.filter(idEmisora=idemisora)


# ##
# #GET: Vista que obtiene las redes sociales de una emisora
# #
# class ListRedSocialEmisora(generics.ListCreateAPIView):
#     serializer_class = serializers.RedSocialEmisoraSerializer

#     def get_queryset(self):
#         idemisora = self.kwargs['id_emisora']
#         return models.RedSocial_emisora.objects.filter(idEmisora=idemisora)


# class ListImagenes(generics.ListAPIView):
#     serializer_class = serializers.ImagenesSerializer
#     queryset = models.Imagenes.objects.all()


# class ListImagenesSegmento(generics.ListAPIView):
#     serializer_class = serializers.ImagenesSerializer

#     def get_queryset(self):
#         id_segmento = self.kwargs['id_segmento']
#         results = models.Imagenes.objects.filter(segmento=id_segmento)
#         return results


# class ListVideos(generics.ListAPIView):
#     serializer_class = serializers.VideosSerializer
#     queryset = models.Videos.objects.all()


# class ListVideosSegmento(generics.ListAPIView):
#     serializer_class = serializers.VideosSerializer

#     def get_queryset(self):
#         id_segmento = self.kwargs['id_segmento']
#         results = models.Videos.objects.filter(segmento=id_segmento)
#         return results


# class ListFavoritos(generics.ListAPIView):
#     serializer_class = serializers.FavoritoSerializer
#     queryset = models.Favorito.objects.all()


# class ListFavoritosUsuario(generics.ListAPIView):
#     serializer_class = serializers.FavoritoSerializer

#     def get_queryset(self):
#         usuario = self.kwargs['usuario']
#         id_usuario = Usuario.objects.filter(username=usuario).values('id').get()['id']
#         results = models.Favorito.objects.filter(usuario=id_usuario)
#         queryset = models.Segmento.objects.filter(pk__in=results.values('segmento'))
#         return queryset


# class ListEncuestasSegmentos(generics.ListAPIView):
#     serializer_class = serializers.EncuestaSerializer

#     def get_queryset(self):
#         id_segmento = self.kwargs['id_segmento']
#         results = models.Encuesta.objects.filter(idSegmento=id_segmento)
#         return results


# class CreateFavorito(generics.ListCreateAPIView):
#     queryset = models.Favorito.objects.all()
#     serializer_class = serializers.FavoritoCreateSerializer


# def CreateFavoritoView(request, id_segmento, username):

#     user = Usuario.objects.get(username=username)

#     fav = models.Favorito(usuario=user, segmento=models.Segmento.objects.filter(id=id_segmento)[0])
#     fav.save()

#     context = {'title': 'Usuarios'}
#     return render(request, 'webAdminRadio/usuarios.html', context)


# def DeleteFavoritoView(request, id_segmento, username):
# 	user = Usuario.objects.get(username=username)
# 	seg = models.Segmento.objects.filter(id=id_segmento)[0]
# 	fav = models.Favorito.objects.filter(usuario=user, segmento=seg)
# 	fav.delete()
# 	context = {'title': 'Usuarios'}
# 	return render(request, 'webAdminRadio/usuarios.html', context)
