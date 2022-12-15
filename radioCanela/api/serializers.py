# api/serializers.py
from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from WebAdminRadio import models
from accounts.models import Usuario, Rol, RolGroup
from django.contrib.auth.models import Group
from rest_framework.validators import UniqueValidator

from django.db.models import Q

from rolepermissions.roles import assign_role

class TimeSerializer(serializers.Serializer):
    fecha = serializers.DateField()
    hora = serializers.TimeField(format='%H:%M:%S')

# Programas
class ProgramaSerializer(serializers.ModelSerializer):
    # horarios = serializers.ReadOnlyField(source="get_horarios")
    class Meta:
        fields = '__all__'
        model = models.Programa
# Roles
class RolSerializer(serializers.ModelSerializer):
    # horarios = serializers.ReadOnlyField(source="get_horarios")
    class Meta:
        fields = '__all__'
        model = models.Rol
# Permisos
class PermisosSerializer(serializers.ModelSerializer):
    # horarios = serializers.ReadOnlyField(source="get_horarios")
    class Meta:
        fields = '__all__'
        model = models.Permisos

# Auditoria
class AuditoriaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Auditoria

# Concursos
class ConcursosSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Concursos

#Radio
class RadioSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Radio

#Emisora
class EmisoraSerializer(serializers.ModelSerializer):
    id_radio = RadioSerializer()
    class Meta:
        fields = '__all__'
        model = models.Emisora

class EmisoraRadioSerializer(serializers.ModelSerializer):
    radio = serializers.CharField(source='id_radio.nombre')

    class Meta:
        fields = [ 'id', 'frecuencia_dial', 'tipo_frecuencia', 'url_streaming', 'direccion', 'ciudad', 'provincia', 'radio' ]
        model = models.Emisora

# Usuario  
class UsuarioSerializer(serializers.ModelSerializer):
    roles = serializers.StringRelatedField(source='groups', many=True)
    activo = serializers.BooleanField(source='is_active')
    
    class Meta:
        fields = [
            'id', 
            'foto', 
            'username', 
            'fechaNacimiento', 
            'email', 
            'groups', 
            'roles', 
            'date_joined', 
            'first_name', 
            'last_name', 
            'activo' # Se creo un alias para referenciar el campo is_active
        ]
        model = models.Usuario

class UsuarioMovilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            'id', 
            'first_name', 
            'last_name', 
            'password', 
            'username',
            'email'
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'email': { 'validators': [UniqueValidator(queryset=Usuario.objects.all())] }
        }
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = self.Meta.model(**validated_data)
        if password is not None:
            user.set_password(password)
        user.save()
        return user

class UsuarioMovilDatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            'id', 
            'first_name', 
            'last_name', 
            'password', 
            'username', 
            'email', 
            'telefono', 
            'fechaNacimiento', 
            'cedula', 
            'sexo'
        ]

class UsuarioMovilUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            'id', 
            'first_name', 
            'last_name', 
            'username', 
            'email', 
            'telefono', 
            'fechaNacimiento', 
            'cedula', 
            'sexo'
        ]
    def validate_email(self, value):
        user = self.context['id']
        if Usuario.objects.exclude(pk=user).filter(email=value).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})
        return value

    def validate_username(self, value):
        user = self.context['id']
        if Usuario.objects.exclude(pk=user).filter(username=value).exists():
            raise serializers.ValidationError({"username": "This username is already in use."})
        return value
    
    def update(self, instance, validated_data):
        user = self.context['id']
        if user != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})
        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.email = validated_data['email']
        instance.username = validated_data['username']
        instance.telefono = validated_data['telefono']
        instance.fechaNacimiento = validated_data['fechaNacimiento']
        instance.cedula = validated_data['cedula']
        instance.sexo = validated_data['sexo']
        instance.save()
        return instance


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = Usuario
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs
    def validate_old_password(self, value):
        user = Usuario.objects.get(pk=self.context['id'])
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance

# Grupos de permisos
class RolGroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = RolGroup


# Torneo
class TorneosSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Torneo

# RedSocial
class RedSocialSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.RedSocial

#
# Serializadores para la api de detalle de equipos
# 

# Equipos
class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Equipo

# RedSocial de equipo
class RedSocialEquipoSerializer(serializers.ModelSerializer):
    id_red_social = RedSocialSerializer()
    class Meta:
        # fields = '__all__'
        exclude = [ 'id_equipo' ]
        model = models.RedSocialEquipo


class EquipoDetallerSerializer(serializers.ModelSerializer):
    redes_sociales = RedSocialEquipoSerializer(source='get_redes_sociales_equipo', many=True)

    class Meta:
        fields = '__all__'
        extra_fields = [ 'redes_sociales' ]
        model = models.Equipo

#
# Serializadores para la api de partidos 
#  

# Emisora (Serializador que devuelve solo datos los datos importantes de la emisora)
class EmisoraPartidoSerializer(serializers.ModelSerializer):
    radio = serializers.CharField(source='id_radio.nombre')

    class Meta:
        fields = [ 'id', 'frecuencia_dial', 'tipo_frecuencia', 'radio' ]
        model = models.Emisora

# Equipos (Serializador que devuelve solo los datos importantes de un equipo)
class EquipoPartidoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [ 'id', 'equipo', 'imagen' ]
        model = models.Equipo

# Partidos
class PartidoTransmisionSerializer(serializers.ModelSerializer):
    emisoras = EmisoraPartidoSerializer(source="get_emisoras", many=True)
    id_torneo = TorneosSerializer()
    id_equipo_local = EquipoPartidoSerializer()
    id_equipo_visitante = EquipoPartidoSerializer()

    class Meta:
        fields = '__all__'
        extra_fields =['emisoras']
        model = models.PartidoTransmision

# Segmento emisora
class SegementoEmisoraSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.SegmentoEmisora

# Horario
class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Horario

class HorarioProgramaSerializer(serializers.ModelSerializer):
    programa = serializers.ReadOnlyField(source="get_programa")
    class Meta:
        fields = ['dia', 'hora_inicio', 'hora_fin', 'programa']
        model = models.Horario

# Programas CON HORARIOS y emisora
class ProgramaSerializerFull(serializers.ModelSerializer):
    horarios = serializers.ReadOnlyField(source="get_horarios")
    idEmisora = serializers.ReadOnlyField(source="get_emisora")

    class Meta:
        model = models.Programa
        fields = ('id', 'nombre', 'imagen','idEmisora', 'descripcion', 'horarios')

class SegementoLocutorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id','nombre','descripcion','imagen']
        model = models.Locutor

class RedSocialLocutorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.RedSocialLocutor

class LocutoresSerializer(serializers.ModelSerializer):

    class Meta:
        fields= '__all__'
        model = models.Locutor

class LocutoresDetalleSerializer(serializers.ModelSerializer):
    redes_sociales = RedSocialLocutorSerializer(source='get_redes_sociales_locutor', many=True)

    class Meta:
        fields= '__all__'
        extra_fields = [ 'redes_sociales' ]
        model = models.Locutor

# Trabsmisiones con plataformas
class TransmisionesSerializerFull(serializers.ModelSerializer):
    plataforma = serializers.ReadOnlyField(source="get_plataforma")

    class Meta:
        model = models.Transmision
        fields = ('id', 'titulo', 'subtitulo', 'descripcion', 'plataforma')


# Publicidad
class PublicidadSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Publicidad


# Noticias
class NoticiaSerializer(serializers.ModelSerializer):
    radioEmisora = serializers.ReadOnlyField(source="get_radio")
    class Meta:
        fields = '__all__'
        extra_fields =['radioEmisora']
        model = models.NoticiasTips


class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Podcast


class PodcastEmisoraSerializer(serializers.ModelSerializer):
    idEmisora = serializers.ReadOnlyField(source="get_emisora")
    class Meta:
        fields = (
            'id',
            'podcast',
            'id_emisora',
        )
        model = models.Podcast

class GaleriaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Galeria

class VideoImagenSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'titulo', 'fecha_creacion', 'descripcion', 'url', 'likes', 'tipo')
        model = models.VideoImagen  

class GaleriaDetalleSerializer(serializers.ModelSerializer):
    imagenes_videos = VideoImagenSerializer(source='get_imagenes_videos_galeria', many=True)

    class Meta:
        fields= '__all__'
        extra_fields = [ 'imagenes_videos' ]
        model = models.Galeria

class PoliticasPrivacidadSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = models.PoliticasPriv

# class EmisoraSerializer(serializers.ModelSerializer):
#     red_sociales = serializers.ReadOnlyField(source="get_redes_sociales")

#     class Meta:
#         fields = '__all__'
#         model = models.Emisora



# #SEGMENTOS DEL DIA ACTUAL
# class SegmentoSerializerToday(serializers.ModelSerializer):
#     horarios = serializers.ReadOnlyField(source="get_horario_dia_actual")
#     emisora= serializers.SerializerMethodField()

#     def get_emisora(self,ob):
#         return EmisoraSerializer(ob.get_emisora()).data


#     class Meta:
#         model = models.SegmentoEmisora
#         fields = ('id', 'nombre', 'imagen','idEmisora', 'horarios','descripcion','emisora')

# class ContactoSerializer(serializers.ModelSerializer):

#     def create(self, validated_data):
#         usuario = models.Contactenos.objects.create(
#             nombre = validated_data['nombre'],
#             correo = validated_data['correo'],
#             telefono = validated_data['telefono'],
#             mensaje = validated_data['mensaje'],
#         )
#         usuario.save()

#         return usuario
    
#     class Meta:
#         fields = (
#             'id',
#             'nombre',
#             'correo',
#             'telefono',
#             'mensaje',
#         )
#         model = models.Contactenos


# class UsuarioRedesSerializer(serializers.ModelSerializer):

#     def create(self, validated_data):
#         usuario = Usuario.objects.create(
#             username=validated_data['username'],
#             email = validated_data['email'],
#         )
#         usuario.save()
#         return usuario  

#     class Meta:
#         fields = (
#             'id',
#             'username',
#             'email',
#         )
#         model = Usuario

# class UsuarioSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)
#     # telefono = serializers.ReadOnlyField(source='get_telefono')

#     def create(self, validated_data):
#         # password = validated_data['password']
#         rol = validated_data['rol']
#         usuario = Usuario.objects.create(
#             cedula = validated_data['cedula'],
#             username=validated_data['username'],
#             email = validated_data['email'],
#             telefono = validated_data['telefono'],
#             first_name = validated_data['first_name'],
#             last_name = validated_data['last_name'],
#             fecha_nac = validated_data['fecha_nac'],
#             # password = password,
#             rol = rol,
#         )
#         usuario.set_password(validated_data['password'])
#         usuario.save()
#         # print(password)
#         idUsuario = Usuario.objects.order_by('-id')[0]
#         assign_role(idUsuario, 'cliente')
#         return usuario  

#     class Meta:
#         fields = (
#             'id',
#             'cedula',
#             'username',
#             'imagen',
#             'email',
#             'first_name',
#             'last_name',
#             'password',
#             'telefono',
#             'fecha_nac',
#             'is_active',
#             'rol',
#         )
#         model = Usuario

# class Usuario2Serializer(serializers.ModelSerializer):

#     def create(self, validated_data):
#         rol = validated_data['rol']
#         usuario = Usuario.objects.create(
#             cedula = validated_data['cedula'],
#             username=validated_data['username'],
#             email = validated_data['email'],
#             telefono = validated_data['telefono'],
#             first_name = validated_data['first_name'],
#             last_name = validated_data['last_name'],
#             fecha_nac = validated_data['fecha_nac'],
#             rol = rol,
#         )
#         usuario.save()

#         assign_role(usuario, 'cliente')
#         return usuario  

#     class Meta:
#         fields = (
#             'id',
#             'cedula',
#             'username',
#             'imagen',
#             'email',
#             'first_name',
#             'last_name',
#             'telefono',
#             'fecha_nac',
#             'is_active',
#             'rol',
#         )
#         model = Usuario





# class TorneoSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         fields = (
#             'id',
#             'nombre',
#             'lugar',
#             'activo',
#         )
#         model = models.Torneo

# class EquipoSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         fields = (
#             'id',
#             'equipo',
#             'lugar',
#             'imagen',
#             'activo',
#         )
#         model = models.Equipo

# class TransmisionEmisoraSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         fields = (
#             'id',
#             'transmision',
#             'emisora'
#         )
#         model = models.TransmisionEmisora

# class GaleriaSerializer(serializers.ModelSerializer):
#     emisoras = serializers.ReadOnlyField(source='get_emisoras')
    
#     class Meta:
#         fields = (
#             'id',
#             'nombre',
#             'imagen',
#             'descripcion',
#             'emisoras',
#             'activo',
#         )
#         model = models.Galeria

# class GaleriaEmisoraSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         fields = (
#             'id',
#             'galeria',
#             'emisora'
#         )
#         model = models.GaleriaEmisora



# class FrecuenciaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Frecuencia
#         fields = (
#             'tipo',
#             'dia_semana',
#             'hora_inicio',
#             'hora_fin',
#         )

# class TelefonoEmisoraSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Telefono_emisora
#         fields= '__all__'

# class RedSocialEmisoraSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.RedSocial_emisora
#         fields= '__all__'

# class TelefonoUsuarioSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Telefono_Usuario
#         fields= '__all__'

# class RedSocialUsuarioSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.RedSocial_usuario
#         fields= '__all__'

# class LocutoresSegmentoSerializer(serializers.ModelSerializer):
#     redes_sociales= serializers.ReadOnlyField(source="get_redes_sociales")

#     #def get_redes_sociales(self,ob):
#     #    return RedSocialUsuarioSerializer(ob.get_redes_sociales()).data

#     class Meta:
#         model = Usuario
#         fields=(
#             'id',
#             'imagen',
#             'first_name',
#             'last_name',
#             'biografia',
#             'fecha_nac',
#             'hobbies',
#             'apodo',
#             'redes_sociales',
#         )

# class LocutoresSerializer(serializers.ModelSerializer):
#     emisora = serializers.SerializerMethodField()

#     class Meta:
#         model = Usuario
#         fields = (
#             'id',
#             'imagen',
#             'first_name',
#             'last_name',
#             'emisora',
#         )

#     def get_emisora(self, obj):
#         segmento_id = self.context.get('segmento')
#         segmento_obj = models.segmento_usuario.objects.get(idSegmento=segmento_id, idUsuario=obj.id)
#         return segmento_obj.idSegmento.idEmisora.nombre


# class ImagenesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Imagenes
#         fields= '__all__'

# class VideosSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Videos
#         fields= '__all__'

# class FavoritoSerializer(serializers.ModelSerializer):
#     emisora= serializers.SerializerMethodField()

#     def get_emisora(self,ob):
#         return EmisoraSerializer(ob.get_emisora()).data

#     class Meta:
#         model = models.Segmento
#         fields = ('id', 'nombre', 'imagen','idEmisora','descripcion','emisora')

# Serializadores para las preguntas de las encuestas en el administrador

class OpcionPreguntaAdminSerializer(serializers.ModelSerializer):
    '''
    Serializador para las opciones de las preguntas, que van a ser utilizadas para representar en el sistema Administrador
    '''

    class Meta:
        fields = ['enunciado']
        model = models.OpcionPregunta

class PreguntaAdminSerializer(serializers.ModelSerializer):
    '''
    Serializador para las preguntas de las encuestas, sirve para pasar como json
    '''

    opciones = OpcionPreguntaAdminSerializer(source='opciones_set', many=True)
    tipo = serializers.CharField(source='tipo_pregunta')

    class Meta:
        fields = [
            'titulo', 
            'tipo', 
            'opciones'
        ]
        model = models.Pregunta


# Serializadores para los detalles de una encuesta que van a ser mostradas en las apps

class OpcionPreguntaAppSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.OpcionPregunta

class PreguntaAppSerializer(serializers.ModelSerializer):
    opciones = OpcionPreguntaAppSerializer(source='opciones_set', many=True)

    class Meta:
        fields = '__all__'
        extra_fields = ['opciones']
        model = models.Pregunta

class EncuestaDetalleAppSerializer(serializers.ModelSerializer):
    preguntas = PreguntaAppSerializer(source='preguntas_set', many=True)
    usuarios_respondieron = serializers.ReadOnlyField(source='numero_total_usuarios_respondieron')

    class Meta:
        model = models.Encuesta
        extra_fields = ['preguntas']        
        exclude = ['usuarios_encuesta']

class EncuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Encuesta
        exclude = ['usuarios_encuesta']


# 

class EncuestaAppSerializer(serializers.ModelSerializer):
    contestado = serializers.SerializerMethodField('_verificar_usuario_respuesta')

    def _verificar_usuario_respuesta(self, obj):
        '''
        Verifica si en la tabla usuario encuesta hay un registro que tenga la id del usuario (id_usuario) y la id de la
        encuesta (obj.id) la cual indica que el usuario ha respondido esta encuesta
        '''

        id_usuario = self.context.get('id_usuario')
        if not id_usuario: # Si no hay una id de usuario se devuelve False por defecto
            return False

        resp = models.UsuarioEncuesta.objects.filter(Q(usuario=id_usuario) & Q(encuesta=obj.id)).exists()
        return resp

    class Meta:
        model = models.Encuesta
        exclude = ['usuarios_encuesta']



class RespuestaPreguntaSerializer(serializers.Serializer):
    id_pregunta= serializers.IntegerField()
    respuestas = serializers.ListField(child = serializers.IntegerField())

class RespuestaEncuestaSerializer(serializers.Serializer):
    id_encuesta = serializers.IntegerField()
    usuario = serializers.IntegerField()
    preguntas = RespuestaPreguntaSerializer(many=True)

    def create(self, validated_data):
        preguntas_datos = validated_data.pop('preguntas')

        usuario = Usuario.objects.get(id=validated_data['usuario'])
        encuesta = models.Encuesta.objects.get(id=validated_data['id_encuesta'])

        usuario_encuesta = models.UsuarioEncuesta.objects.create(usuario=usuario, encuesta=encuesta)

        for pregunta in preguntas_datos:
            respuestas_usuario = pregunta['respuestas']

            for respuesta in respuestas_usuario:
                opcion = models.OpcionPregunta.objects.get(id=respuesta)

                detalles = models.UsuarioDetalleEncuesta(
                    opcion_pregunta= opcion,
                    pregunta= encuesta.preguntas_set.get(id=pregunta['id_pregunta']),
                    usuario_encuesta=usuario_encuesta
                )

                usuario_encuesta.usuarios_detalle_encuesta_set.add(detalles, bulk=False)

        usuario_encuesta.save()
        
        return usuario_encuesta


# class ListEncuestaUsuarioAppSerializer(serializers.ModelSerializer):
#     contestada = serializers.SerializerMethodField('get_usuario')

#     def get_usuario(self, obj):
#         id_usuario = self.context.get('user_id')
#         return Usuario.objects.filter(id=id_usuario).exists()

#     class Meta:
#         model = models.Encuesta
#         fields= '__all__'

# class RespuestaEncuestaSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = models.Respuesta_Encuesta
#         fields= '__all__'

# class VotoSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = models.Voto
#         fields = '__all__'
        
# class ResultadoSerializer(serializers.ModelSerializer):
#     # respuestas = serializers.ReadOnlyField(source="get_respuestas")
    
#     # class Meta:
#     #     model = models.Encuesta
#     #     fields = (
#     #         'id',
#     #         'titulo',
#     #         'pregunta',
#     #         'respuestas',
#     #         'activo'
#     #     )
#     class Meta:
#         model = models.Resultados
#         fields = '__all__'



# class ResultadoEncuestaSerializer(serializers.ModelSerializer):
#     respuestas = serializers.ReadOnlyField(source="get_respuestas")
#     class Meta:
#         model = models.ResultadosEncuesta
#         fields = '__all__'


# # class ResultadosRespuestaSerializer(serializers.ModelSerializer):
    
# #     class Meta:
# #         model = models.Respuesta_Encuesta
# #         fields= '__all__'

# class FavoritoCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Favorito
#         fields = "__all__"


# class reseteoDPaswword(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField(required=True)
#     username = serializers.CharField(required=True)
