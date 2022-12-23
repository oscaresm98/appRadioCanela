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

from accounts.models import Usuario, RolGroup

from . import serializers
from rest_framework import mixins, viewsets
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
from django.shortcuts import render
from WebAdminRadio.models import *

from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


from django.contrib.auth.models import Group

from django.urls import path
from . import views
import datetime, jwt
from datetime import timedelta

from rolepermissions.roles import assign_role
from rolepermissions.mixins import HasRoleMixin

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

import datetime
from django.utils import timezone

from django.db.models import Q
from .pagination import PartidosPagination, NoticiasPagination, EncuestaPagination

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


#Redes Sociales
# GET: Vista que obtiene red social
class redsocial(generics.ListCreateAPIView):
    queryset = RedSocial.objects.filter(estado=True)
    serializer_class = serializers.RedSocialSerializer


# GET: Vista que obtiene red social del equipo
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

# Concursos
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
@api_view(['GET'])
def programa_detalle(request,pk):
    try:
        programa = Programa.objects.get(id=pk)
    except Programa.DoesNotExist: 
        return Response({'Error': 'El programa no existe'}, status=status.HTTP_404_NOT_FOUND)
        
    #GET: Vista en la que se obtiene una emisora por id 
    if request.method == 'GET':
        serializers = ProgramaSerializerFull(programa) 
        return Response(serializers.data) 


@api_view(['GET', 'POST','DELETE'])
def programaLocutorList(request,pk):
    
    try:
        emisora = SegmentoLocutor.get_locutores(pk)
    except Emisora.DoesNotExist:
        return Response({'Error': 'El programa no tiene locutores asignados'}, status=status.HTTP_400_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = SegementoLocutorSerializer(emisora, many=True)
        return Response(serializer.data)

# lista de los programas de una emisora por dia
class ListProgramasDia(generics.ListAPIView):
    serializer_class = serializers.HorarioProgramaSerializer
    
    def get_queryset(self):
        em = self.kwargs['id_emisora']
        d = self.kwargs['dia']
        programas = Programa.objects.filter(pk__in=SegmentoEmisora.objects.filter(emisora=em).values('segmento'), estado=True)
        print(programas)
        return Horario.objects.filter(id_programa__in=programas, estado=True, dia=d.capitalize()).order_by('hora_inicio')
    


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

#Obtiene las programas segun la emisora
class ListEmisoraProgramas(generics.ListAPIView):
    serializer_class = serializers.ProgramaSerializerFull

    def get_queryset(self):
        em = self.kwargs['id_emisora']
        return Programa.objects.filter(pk__in=SegmentoEmisora.objects.filter(emisora=em).values('segmento'), estado=True)


# GET: Vista que obtiene Segmentos emisoras
class SegmentoEmisoraList(generics.ListCreateAPIView):
    queryset = SegmentoEmisora.objects.all()
    serializer_class = serializers.SegementoEmisoraSerializer
    
# GET: Vista que obtiene Horarios
class HorariosList(generics.ListCreateAPIView):
    queryset = Horario.objects.filter(estado=True)
    serializer_class = serializers.HorarioSerializer


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

# api que obtiene las emisoras de una radio
class ListRadioEmisoras(generics.ListAPIView):
    serializer_class = serializers.EmisoraRadioSerializer
    
    def get_queryset(self):
        radio = self.kwargs['id_radio']
        return Emisora.objects.filter(id_radio=radio, estado=True)
       
#
## Usuarios
#
@api_view(['GET'])
def usuarioList(request):
    if request.method == 'GET':
        try:
            usuarios = Usuario.objects.all()
            serializer = UsuarioSerializer(usuarios, many=True)
            return Response(serializer.data)
        except Usuario.DoesNotExist:
            return Response({'Error': 'El usuario no existe'}, status=status.HTTP_400_NOT_FOUND)

# Servicio para obtener informacion de los roles
class ListRoles(generics.ListAPIView):
    serializer_class = serializers.RolGroupSerializer
    queryset = RolGroup.objects.all()

# Servicio para registro de un nuevo usuario
class RegisterView(APIView):
    def post(self, request):
        serializer = UsuarioMovilSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

# Servicio para vericicar el login de usuario
class LoginView(APIView):
    def post(self, request):
        username_email = request.data['username_email']
        password = request.data['password']
        user = Usuario.objects.filter(Q(username=username_email) | Q(email=username_email)).first()

        if user is None:
            raise AuthenticationFailed('Usuario no encontrado!')

        if not user.check_password(password):
            raise AuthenticationFailed('Password Incorecta!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        # response.set_cookie(key='jwt', value=token, samesite='None', secure=True, httponly=True) # Activar esta linea cuando se prueba en el servidor
        
        response.set_cookie(key='jwt', value=token) # Activar esta linea cuando se depura en local y se prueba con Postman

        response.data = { 'jwt': token }
        return response

# Servicio para obtener los datos del usuario autentificado
class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        
        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = Usuario.objects.filter(id=payload['id']).first()
        serializer = UsuarioMovilDatosSerializer(user)
        return Response(serializer.data)

# Servicio para cerrar session
class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response

# Servicio para actualizar usuario
class UpdateProfileView(generics.UpdateAPIView):
    def put(self, request, *args, **kwargs):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        user = Usuario.objects.get(id=payload['id'])
        serializer = UsuarioMovilUpdateSerializer(user, data=request.data, context={'id': user.id})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Servicio para cambiar password a usuario
class ChangePasswordView(generics.UpdateAPIView):
    def put(self, request, *args, **kwargs):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        user = Usuario.objects.get(id=payload['id'])
        serializer = ChangePasswordSerializer(user, data=request.data, context={'id': user.id})
        if serializer.is_valid():
            serializer.save()
            response = Response()
            response.data = {
            'message': 'success'}
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Roles
@api_view(['GET', 'POST','DELETE','PUT'])
def rolesList(request):
    if request.method == 'GET':
        try:
            roles = Rol.objects.all()
            serializer = RolSerializer(roles, many=True)
            return Response(serializer.data)
        except Rol.DoesNotExist:
            return Response({'Error': 'El rol no existe'}, status=status.HTTP_400_NOT_FOUND)
        
    elif request.method == 'POST':
        serializer = RolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        serializer = RolSerializer(roles, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        roles = Rol.objects.all()
        roles.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Roles
@api_view(['GET', 'POST','DELETE','PUT'])
def permisosList(request):
    
    if request.method == 'GET':
        try:
            permisos = Permisos.objects.all()
            serializer = PermisosSerializer(permisos, many=True)
            return Response(serializer.data)
        except Permisos.DoesNotExist:
            return Response({'Error': 'El permiso no existe'}, status=status.HTTP_400_NOT_FOUND)
        
    elif request.method == 'POST':
        serializer = PermisosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        serializer = PermisosSerializer(permisos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        permisos = Permisos.objects.all()
        permisos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# 
# Vistas de la API para torneos
# 

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

# 
# Vistas de la API para equipos
# 

# Equipos
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

# class ListEquiposPorId(generics.ListAPIView):
#     serializer_class = serializers.EquipoSerializer

#     def get_queryset(self):
#         idteam = self.kwargs['id_equipo']
#         queryset = Equipo.objects.filter(id=idteam, estado=True)
#         return queryset

# Detalle Equipo
class EquipoPorId(generics.RetrieveAPIView):
    serializer_class = serializers.EquipoDetallerSerializer
    queryset = Equipo.objects.all()

# 
# Vistas de la API para partidos
# 

# Partidos
class ListPartidoTransmisiones(generics.ListAPIView):
    serializer_class = serializers.PartidoTransmisionSerializer
    queryset = PartidoTransmision.objects.filter(estado=True).order_by('-fecha_evento')

# Partidos ya jugados
class ListPartidosJugados(generics.ListAPIView):
    serializer_class = serializers.PartidoTransmisionSerializer
    pagination_class = PartidosPagination

    def get_queryset(self):
        fecha_actual = datetime.datetime.now(tz=timezone.utc)
        return PartidoTransmision.objects.filter(Q(fecha_evento__lt=fecha_actual)).order_by('-fecha_evento')

# Partidos por jugar
class ListPartidosPorJugar(generics.ListAPIView):
    serializer_class = serializers.PartidoTransmisionSerializer
    pagination_class = PartidosPagination

    def get_queryset(self):
        fecha_actual = datetime.datetime.now(tz=timezone.utc)
        return PartidoTransmision.objects.filter(Q(fecha_evento__gte=fecha_actual)).order_by('-fecha_evento')

# 
# Vistas de API para locutores
# 

@api_view(['GET', 'POST', 'DELETE'])
def LocutorList(request):
    try:
        locutor = Locutor.objects.filter(estado=True)
    except Locutor.DoesNotExist:
        return Response({'Error': 'La emisora no existe'}, status=status.HTTP_400_NOT_FOUND)

    if request.method == 'GET':
        serializer = LocutoresSerializer(locutor, many=True)
        return Response(serializer.data)
        
    elif request.method == 'POST':
        serializer = LocutoresSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        locutor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Se maneja la radios por id     
@api_view(['GET', 'PUT','DELETE'])
def Locutor_detalle(request,pk): 
    try: 
        locutor = Locutor.objects.get(id=pk)
    except Locutor.DoesNotExist:
        return Response({'Error': 'Locutor no existe'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializers = LocutoresDetalleSerializer(locutor) 
        return Response(serializers.data) 
      
    elif request.method == 'PUT':       
        serializer = LocutoresSerializer(locutor, data=request.data)    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
    elif request.method == 'DELETE':
        locutor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

# Publicidad
# GET: que obtiene las publicidades por radio
class ListPublicidad(generics.ListAPIView):
    serializer_class = serializers.PublicidadSerializer
    
    def get_queryset(self):
        radio = self.kwargs['id_radio']
        return Publicidad.objects.filter(id_radio=radio, estado=True)

#
# Vistas de API para Noticias
#

# GET de todas las noticias
class NoticiasList(generics.ListAPIView):
    queryset = NoticiasTips.objects.filter(estado=True)
    pagination_class = NoticiasPagination
    serializer_class = serializers.NoticiaSerializer

# lista de las noticias de una emisora
class ListNoticia(generics.ListAPIView):
    pagination_class = NoticiasPagination
    serializer_class = serializers.NoticiaSerializer
    
    def get_queryset(self):
        emisora = self.kwargs['id_emisora']
        return NoticiasTips.objects.filter(id_emisora=emisora, estado=True)


# lista de las noticias por id
class Noticia_detalle(generics.ListAPIView):
    pagination_class = NoticiasPagination
    serializer_class = serializers.NoticiaSerializer
    
    def get_queryset(self):
        noticia = self.kwargs['pk']
        return NoticiasTips.objects.filter(id=noticia, estado=True)


# lista de las noticias por tipo
class NoticiaTipo(generics.ListAPIView):
    pagination_class = NoticiasPagination
    serializer_class = serializers.NoticiaSerializer
    
    def get_queryset(self):
        tipo = self.kwargs['tipo']
        return NoticiasTips.objects.filter(tipo=tipo.capitalize(), estado=True)

@api_view(['GET',"POST"])
def ListPodcasts(request):
    try:
        podcast = Podcast.objects.filter(estado=True)
    except Podcast.DoesNotExist:
        return Response({'Error': 'El podcast no existe'}, status=status.HTTP_400_NOT_FOUND)

    if request.method == 'GET':
        serializer = PodcastSerializer(podcast, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PodcastSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def Emisora_Podcast_list(request, id_emisora):
    try:
        podcast = Podcast.objects.filter(estado=True,id_emisora=id_emisora)
    except Podcast.DoesNotExist:
        return Response({'Error': 'El podcast no existe'}, status=status.HTTP_400_NOT_FOUND)

    if request.method == 'GET':
        serializer = PodcastSerializer(podcast, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PodcastSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
def podcast_Detalle(request,id_podcast):
    try:
        podcast = Podcast.objects.filter(estado=True,id=id_podcast)
    except Podcast.DoesNotExist:
        return Response({'Error': 'El podcast no existe'}, status=status.HTTP_400_NOT_FOUND)

    if request.method == 'GET':
        serializer = PodcastSerializer(podcast, many=True)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PodcastSerializer(podcast, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE'])
def GaleriaList(request):
    try:
        galeria = Galeria.objects.filter(estado=True)
    except Galeria.DoesNotExist:
        return Response({'Error': 'La emisora no existe'}, status=status.HTTP_400_NOT_FOUND)

    if request.method == 'GET':
        serializer = GaleriaSerializer(galeria, many=True)
        return Response(serializer.data)
        
    elif request.method == 'POST':
        serializer = GaleriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        galeria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT','DELETE'])
def Galeria_detalle(request,id_emisora): 
    try: 
        galeria = Galeria.objects.get(id_emisora=id_emisora)
        multimedia = VideoImagen.objects.filter(id_galeria=galeria.id)
    except Galeria.DoesNotExist:
        return Response({'Error': 'Galeria no existe'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializers = VideoImagenSerializer(multimedia, many=True)
        return Response(serializers.data) 
      
    elif request.method == 'PUT':       
        serializer = GaleriaSerializer(galeria, data=request.data)    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
    elif request.method == 'DELETE':
        galeria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def GaleriaImagenes_detalle(request,id_emisora): 
    try: 
        galeria = Galeria.objects.get(id_emisora=id_emisora)
        multimedia = VideoImagen.objects.filter(id_galeria=galeria.id, tipo='imagen')
    except Galeria.DoesNotExist:
        return Response({'Error': 'Galeria no existe'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializers = VideoImagenSerializer(multimedia, many=True)
        return Response(serializers.data) 

@api_view(['GET'])
def GaleriaVideos_detalle(request,id_emisora): 
    try: 
        galeria = Galeria.objects.get(id_emisora=id_emisora)
        multimedia = VideoImagen.objects.filter(id_galeria=galeria.id, tipo='video')
    except Galeria.DoesNotExist:
        return Response({'Error': 'Galeria no existe'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializers = VideoImagenSerializer(multimedia, many=True)
        return Response(serializers.data) 

@api_view(['GET', 'POST', 'DELETE'])
def ImagenesVideosList(request):
    try:
        multimedia = VideoImagen.objects.filter(estado=True)
    except VideoImagen.DoesNotExist:
        return Response({'Error': 'La emisora no existe'}, status=status.HTTP_400_NOT_FOUND)

    if request.method == 'GET':
        serializer = VideoImagenSerializer(multimedia, many=True)
        return Response(serializer.data)
        
    elif request.method == 'POST':
        serializer = VideoImagenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        multimedia.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class ListUsuarios(generics.ListAPIView, HasRoleMixin):
#     allowed_roles = 'Locutor'
#     serializer_class = serializers.UsuarioSerializer
#     queryset = Usuario.objects.filter(is_active=True)



#
# Transmisiones
#

#Obtiene las transmisiones segun la emisora
class ListEmisoraTrasmisiones(generics.ListAPIView):
    serializer_class = serializers.TransmisionesSerializerFull

    def get_queryset(self):
        em = self.kwargs['id_emisora']
        return Transmision.objects.filter(id_emisora=em)


# 
# Politicas de Privacidad
#

class ListPoliticas(generics.ListAPIView):
    serializer_class = serializers.PoliticasPrivacidadSerializer
    
    def get_queryset(self):
        return PoliticasPriv.objects.order_by('-fecha_creado')

@api_view(['GET'])
def politicas_privacidad_vigente(request):
    """
    Renderiza una API view para obtener los datos de la politica de privacidad vigente
    """

    politicas_actual = PoliticasPriv.objects.order_by('fecha_creado').first()
    serializer = serializers.PoliticasPrivacidadSerializer(politicas_actual)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST', 'DELETE'])
def EncuestaEmisora(request,id_emisora):  
    try:
        encuestas = Encuesta.objects.filter(id_emisora=id_emisora)
    except Encuesta.DoesNotExist:
        return Response({'Error': 'La encuesta no esta activa o existe'}, status=status.HTTP_400_NOT_FOUND)

    if request.method == 'GET':
        serializer = EncuestaSerializer(encuestas, many=True)
        return Response(serializer.data)
        
    elif request.method == 'POST':
        serializer = EncuestaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        encuestas.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Servicio para web, retorna encuestas activas
@api_view(['GET', 'POST', 'DELETE'])
def EncuestaListActivas(request):  
    try:
        encuestas = Encuesta.objects.filter(estado=True)
    except Encuesta.DoesNotExist:
        return Response({'Error': 'La encuesta no esta activa o existe'}, status=status.HTTP_400_NOT_FOUND)

    if request.method == 'GET':
        serializer = EncuestaSerializer(encuestas, many=True)
        return Response(serializer.data)
        
    elif request.method == 'POST':
        serializer = EncuestaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        encuestas.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Servicio retorna Preguntas segun encuesta
@api_view(['GET', 'POST', 'DELETE'])
def PreguntaEcuestas(request,id_encuesta):
    try: 
        pregunta = Pregunta.objects.filter(id_encuesta=id_encuesta)
    except Encuesta.DoesNotExist:
        return Response({'Error': 'La pregunta no existe'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializers = PreguntaSerializer(pregunta, many=True)
        return Response(serializers.data) 

    elif request.method == 'POST':
        serializer = PreguntaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        pregunta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'DELETE'])
def OpcionesPreguntas(request,id_encuesta,id_pregunta):
    try: 
        pregunta = Pregunta.objects.filter(id_encuesta=id_encuesta)
        opcionesPregunta = OpcionPregunta.objects.filter(pregunta_id=id_pregunta)
    except Pregunta.DoesNotExist:
        return Response({'Error': 'La pregunta no existe'}, status=status.HTTP_404_NOT_FOUND)
    except OpcionPregunta.DoesNotExist:
        return Response({'Error': 'La respuesta no existe'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = OpcionPreguntaSerializer(opcionesPregunta, many=True)
        return Response(serializers.data) 

    elif request.method == 'POST':
        serializer = OpcionPreguntaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        opcionesPregunta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListPreguntasEncuestaAdmin(generics.ListAPIView):
    serializer_class = serializers.PreguntaAdminSerializer

    def get_queryset(self):
        encuesta = self.kwargs['id_encuesta']
        return Pregunta.objects.filter(id_encuesta=encuesta)

@api_view(['GET'])
def encuesta_detalles(request, id_encuesta):
    encuesta = Encuesta.objects.get(id=id_encuesta)
    serializer = serializers.EncuestaDetalleAppSerializer(encuesta)
    return Response(serializer.data, status=status.HTTP_200_OK)


def obtener_id_usuario_token(request):
    '''
    Metodo que obtiene el id del usuario mediante el token que se pasa por las cookies de la peticion
    '''

    token = request.COOKIES.get('jwt')
    
    if not token: # En el caso que en las cookies de la peticion no esta el token del usuario
        print('NO HAY TOKEN')
        return None

    print(token)
    payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    return payload['id']


class ListEncuestasDisponibles(generics.ListAPIView):
    '''
    Vista de API para obtener las encuestas disponibles
    '''

    # serializer_class = serializers.EncuestaSerializer
    serializer_class = serializers.EncuestaAppSerializer
    pagination_class = EncuestaPagination

    def get_queryset(self):
        fecha_hora_actual = datetime.datetime.now(tz=timezone.utc)
        return Encuesta.objects.filter(Q(fecha_hora_fin__gt=fecha_hora_actual) & Q(estado=True)).order_by('-fecha_hora_inicio')

    def get_serializer_context(self):
        context = super().get_serializer_context()
        id_usuario = obtener_id_usuario_token(self.request)
        context.update({ 'id_usuario': id_usuario })
        return context

    

class ListEncuestasFinalizadas(generics.ListAPIView):
    '''
    Vista de API para obtener las encuestas finalizadas
    '''

    # serializer_class = serializers.EncuestaSerializer
    serializer_class = serializers.EncuestaAppSerializer
    pagination_class = EncuestaPagination

    def get_queryset(self):
        fecha_hora_actual = datetime.datetime.now(tz=timezone.utc)
        return Encuesta.objects.filter(Q(fecha_hora_fin__lt=fecha_hora_actual) & Q(estado=True)).order_by('-fecha_hora_inicio')

    def get_serializer_context(self):
        context = super().get_serializer_context()
        id_usuario = obtener_id_usuario_token(self.request)
        context.update({ 'id_usuario': id_usuario })
        return context


class EncuestaRespuesta(APIView):

    def post(self, request):
        id_usuario = obtener_id_usuario_token(request)
        request.data['usuario'] = id_usuario
        serializador = serializers.RespuestaEncuestaSerializer(data=request.data)

        if serializador.is_valid():
            usuario_encuesta = serializador.save()
            return Response({ 
                'mensaje': 'Registro de la respuesta exitosa',
                'respuesta' : serializers.EncuestaDetalleAppSerializer(Encuesta.objects.get(id=request.data['id_encuesta'])).data
            })

        return Response({ 'error': 'No se pasaron valores correctos' })


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
