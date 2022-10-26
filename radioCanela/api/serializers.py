# api/serializers.py
from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from WebAdminRadio import models
from accounts.models import Usuario,Rol

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

# Usuario  
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Usuario

class UsuarioMovilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'first_name', 'last_name', 'password', 'username','email']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = self.Meta.model(**validated_data)
        if password is not None:
            user.set_password(password)
        user.save()
        return user

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

class LocutoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Locutor
        fields= ('id', "nombre", 'imagen', "descripcion", "fecha_nacimiento", "estado")

class RedSocialLocutorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.RedSocialLocutor

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

# class EncuestaSerializer(serializers.ModelSerializer):
#     respuestas = serializers.ReadOnlyField(source="get_respuestas")
    
#     class Meta:
#         model = models.Encuesta
#         fields = (
#             'id',
#             'titulo',
#             'pregunta',
#             'dia_inicio',
#             'hora_inicio',
#             'dia_fin',
#             'hora_fin',
#             'respuestas',
#             'activo'
#         )

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
