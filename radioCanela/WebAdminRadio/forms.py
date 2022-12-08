from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import Group


from .models import *
from accounts.models import *


# field_name_mapping es el diccionario con los names que estarán en los forms,
# que no deben ser iguales a los campos de los modelos
class EmisoraForm(forms.ModelForm):
    class Meta:
        model= Emisora
        fields = [
            'id_radio',
            'frecuencia_dial',
            'tipo_frecuencia',
            'url_streaming',
            'direccion',
            'ciudad',
            'provincia'
        ]
        
class RadioForm(forms.ModelForm):
    class Meta:
        model = Radio
        fields = [
            'nombre', 
            'logotipo',
            'sitio_web',
            'descripcion'
        ]
class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = [
            'nombre', 
            'descripcion',
            'activo',
        ]
class PermisosForm(forms.ModelForm):
    class Meta:
        model = Permisos
        fields = [
            'id_rol', 
            'nombre',
            'ver',
            'agregar',
            'actualizar',
            'borrar',
            'activo',
        ]        
class UsuarioForm(forms.ModelForm):
    class Meta:
        model=Usuario
        fields=[
                'first_name',
                'last_name',
                'username',
                'sexo',
                'email',
                'cedula',
                'fechaNacimiento',
                'telefono',
                # 'rol',
                'descripcion',
                'foto',
                #'activo'
        ]
        def add_prefix(self, field_name):
            field_name_mapping = {
                'fechaNacimiento': 'nacimiento',
            }
            field_name = field_name_mapping.get(field_name, field_name)
            return super(UsuarioForm, self).add_prefix(field_name)


    # def add_prefix(self, field_name):
    #     field_name_mapping = {
    #         'url_streaming': 'streaming',
    #         'frecuencia_dial': 'frecuencia',
    #         'sitio_web': 'sitioweb'
    #     }
    #     field_name = field_name_mapping.get(field_name, field_name)
    #     return super(EmisoraForm, self).add_prefix(field_name)

class TelefonoForm(forms.Form):
    telefono = forms.RegexField(regex=r"(\+)?[0-9]+", max_length=10)


class ProgramaForm(forms.ModelForm):
    class Meta:
        model = Programa
        fields = [
            'nombre',
            'descripcion',
            'imagen'
        ]

class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = [
            'id_programa',
            'dia',
            'hora_inicio',
            'hora_fin'
        ]
        
    # Esta función define el atributo 'name' con el valor del diccionario
    def add_prefix(self, field_name):
        field_name_mapping = {
            'id_programa': 'programa'
        }
        field_name = field_name_mapping.get(field_name, field_name)
        return super(HorarioForm, self).add_prefix(field_name)


class RedSocialForm(forms.Form):
    nombre = forms.CharField(max_length=25, required=False)
    logo_red_social = forms.URLField(max_length=2080, required=False)

# Publicidad
class PublicidadForm(forms.ModelForm):
    class Meta:
        model = Publicidad
        fields = [
            'id_radio',
            'titulo',
            'cliente',
            'descripcion',
            'url',
            'imagen',
            'fecha_inicio',
            'fecha_fin',
        ]
    # Esta función define el atributo 'name' con el valor del diccionario
    def add_prefix(self, field_name):
        field_name_mapping = {
            'id_radio': 'radio',
            'fecha_inicio': 'fechainicio',
            'fecha_fin': 'fechafin',
        }
        field_name = field_name_mapping.get(field_name, field_name)
        return super(PublicidadForm, self).add_prefix(field_name)

# Noticia
class NoticiaForm(forms.ModelForm):
    class Meta:
        model = NoticiasTips
        fields = [
            'id_emisora',
            'titulo',
            'fecha_subida',
            'imagen',
            'tipo',
            'descripcion',
            'activo',
        ]

    # Esta función define el atributo 'name' con el valor del diccionario
    def add_prefix(self, field_name):
        field_name_mapping = {
            'id_emisora': 'emisora',
            'fecha_subida': 'fechasubida',
        }
        field_name = field_name_mapping.get(field_name, field_name)
        return super(NoticiaForm, self).add_prefix(field_name)

# Trabsmisiones
class TransmisionForm(forms.ModelForm):
    class Meta:
        model = Transmision
        fields = [
            'id_emisora',
            'titulo',
            'subtitulo',
            'descripcion',
            'estado',
        ]

class RolGroupForm(forms.ModelForm):
    class Meta:
        model = RolGroup
        fields = '__all__'

    def add_prefix(self, field_name):
        field_name_mapping = {
            'permissions': 'permisos'
        }
        field_name = field_name_mapping.get(field_name, field_name)
        return super(RolGroupForm, self).add_prefix(field_name)


class UsuarioAdminForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        exclude = ('password', 'date_joined', 'slug', 'metodo_ingreso', 'foto')

    # Sobreescritura del metodo para aceptar los campos que envia el formulario
    def add_prefix(self, field_name):
        field_name_mapping = {
            'first_name': 'nombre',
            'last_name': 'apellido',
            'fechaNacimiento': 'fechaNac',
            'groups': 'roles',
            'is_active': 'activo'
        }
        field_name = field_name_mapping.get(field_name, field_name)
        return super(UsuarioAdminForm, self).add_prefix(field_name)


class PoliticasPrivacidadForm(forms.ModelForm):

    class Meta:
        model = PoliticasPriv
        fields = ['nombre', 'url', 'contenido']

# class FrecuenciaForm(forms.ModelForm):
#     class Meta:
#         model = Frecuencia
#         fields = [
#             'tipo',
#             'dia_semana',
#             'hora_inicio',
#             'hora_fin'
#             ]

#     def add_prefix(self, field_name):
#         field_name_mapping = {
#             'hora_inicio': 'inicio',
#             'hora_fin': 'fin',
#             'dia_semana': 'dia',
#         }
#         field_name = field_name_mapping.get(field_name, field_name)
#         return super(FrecuenciaForm, self).add_prefix(field_name)


# class UsuarioForm(UserCreationForm):
#     class Meta:
#         model = Usuario
#         fields = [
#             'first_name',
#             'last_name',
#             'username',
#             'password1',
#             'password2',
#             'email',
#             'telefono',
#             'fecha_nac',
#             'imagen',
#             'rol',
#             'apodo',
#             'biografia',
#             'hobbies',
#         ]

#     def add_prefix(self, field_name):
#         field_name_mapping = {
#             'first_name': 'nombre',
#             'last_name': 'apellido',
#             'fecha_nac': 'fechaNac',
#         }
#         field_name = field_name_mapping.get(field_name, field_name)
#         return super(UsuarioForm, self).add_prefix(field_name)

# class EditarUsuarioForm(forms.ModelForm):
#     class Meta:
#         model = Usuario
#         fields = [
#             'first_name',
#             'last_name',
#             'username',
#             'email',
#             'telefono',
#             'fecha_nac',
#             'imagen',
#             'rol',
#             'apodo',
#             'biografia',
#             'hobbies',
#         ]

#     def add_prefix(self, field_name):
#         field_name_mapping = {
#             'first_name': 'nombre',
#             'last_name': 'apellido',
#             'fecha_nac': 'fechaNac',
#         }
#         field_name = field_name_mapping.get(field_name, field_name)
#         return super(EditarUsuarioForm, self).add_prefix(field_name)

class TorneoForm(forms.ModelForm):
    class Meta:
        model = Torneo
        fields = [
            'nombre',
            'lugar',
            'estado'
        ]

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = [
            'equipo',
            'ciudad',
            'descripcion',
            'imagen'
        ]

class PartidoTransmisionForm(forms.ModelForm):
    id_equipo_local = forms.ModelChoiceField(queryset=Equipo.objects.all())
    id_equipo_visitante = forms.ModelChoiceField(queryset=Equipo.objects.all())
    id_torneo = forms.ModelChoiceField(queryset=Torneo.objects.all())

    class Meta:
        model = PartidoTransmision
        fields = [
            'hora_inicio',
            'fecha_evento',
            'lugar',
            'id_torneo',
            'descripcion',
            'id_equipo_local',
            'id_equipo_visitante',
            'ptos_equipo_local',
            'ptos_equipo_visitante',
            'estadio'
        ]

    # Se usa este metodo para sobrescribir los campos del formulario
    def add_prefix(self, field_name):
        field_name_mapping = {
            # Para la fecha y hora
            'hora_inicio': 'hora',
            'fecha_evento': 'fecha',
            # Para los equipos
            'id_equipo_local': 'equipo1',
            'id_equipo_visitante': 'equipo2',
            # Para los goles
            'ptos_equipo_local': 'goles_equipo_local',
            'ptos_equipo_visitante': 'goles_equipo_visitante',
            # Para el torneo
            'id_torneo':'torneo',
            'descripcion': 'descripcion',
            'lugar': 'lugar',
        }
        field_name = field_name_mapping.get(field_name, field_name)
        return super(PartidoTransmisionForm, self).add_prefix(field_name)  

class PartidoTransmisionEmisoraForm(forms.ModelForm):
    
    class Meta:
        model = PartidoTransmisionEmisora
        fields = [ 'id_emisora' ]

class LocutorForm(forms.ModelForm):
    class Meta:
        model = Locutor
        fields = [
            'nombre',
            'imagen',
            'descripcion',
            'fecha_nacimiento'
        ]

class PodcastForm(forms.ModelForm):
    emisora = forms.ModelChoiceField(queryset=Emisora.objects.all())
    class Meta:
        model = Podcast
        fields = [
            'nombre',
            'descripcion',
            'audio',
            'fecha',
            'id_emisora',
            'imagen',
        ]
    def add_prefix(self, field_name):
        field_name_mapping = {
            'id_emisora': 'emisora',
        }
        field_name = field_name_mapping.get(field_name, field_name)
        return super(PodcastForm, self).add_prefix(field_name)

class GaleriaForm(forms.ModelForm):
    class Meta:
        model = Galeria
        fields = [
            'id_emisora',
            'nombre',
            'descripcion',
            'imagen'
        ]



class ImagenVideoForm(forms.ModelForm):
    class Meta:
        model = VideoImagen
        fields = [
            'fecha_creacion',
            'titulo',
            'descripcion',
            'likes',
            'tipo',
            'id_galeria',
            'estado'
        ]

class EncuestaForm(forms.ModelForm):
    class Meta:
        model = Encuesta
        fields = [
            'titulo',
            'descripcion',
            'dia_inicio',
            'dia_fin',
            'id_emisora'
        ]
    
    def add_prefix(self, field_name):
        field_name_mapping = {
            'id_emisora': 'emisora',
        }
        field_name = field_name_mapping.get(field_name, field_name)
        return super(EncuestaForm, self).add_prefix(field_name)

class PreguntaEncuestaForm(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields = [
            'titulo',
            'id_encuesta'
        ]

class OpcionPreguntaEncuestaForm(forms.ModelForm):
    class Meta:
        model = OpcionPregunta
        fields = [
            'enunciado',
            'pregunta'
        ]

# class EncuestaForm(forms.ModelForm):
#     class Meta:
#         models = Encuesta
#         fields = [
#             'titulo',
#             'descripcion',
#             'imagen',
#             'hora_inicio',
#             'dia_inicio',
#             'hora_fin',
#             'dia_fin',
#             'estado',
#             'id_emisora',
#         ]


# class GaleriaForm(forms.ModelForm):

#     class Meta:
#         model = Galeria
#         fields = [
#             'nombre',
#             'descripcion',
#             'imagen'
#         ]

# class GaleriaEmisoraForm(forms.ModelForm):

#     class Meta:
#         model = GaleriaEmisora
#         fields = [
#             'emisora'
#         ]



# class PodcastEmisoraForm(forms.ModelForm):

#     class Meta:
#         model = PodcastEmisora
#         fields = [
#             'emisora'
#         ]


# class ConcursoForm(forms.ModelForm):
#     class Meta:
#         model = Concurso
#         fields = [
#             'idEncuesta',
#             'idUsuario',
#             'premios'
#         ]

# class PreguntaForm(forms.ModelForm):
#     class Meta:
#         model = Pregunta
#         fields = [
#             'contenido',
#             'respuesta_c',
#             'tipo',
#             'idEncuesta'
#         ]

# class RespuestaForm(forms.ModelForm):
#     class Meta:
#         model = Respuesta
#         fields = [
#             'contenido',
#             'correcta'
#         ]

# class AlternativaForm(forms.ModelForm):
#     class Meta:
#         model = Alternativa
#         fields = [
#             'contenido',
#             'idPregunta',
#         ]

# class Respuesta_EncuestaForm(forms.ModelForm):
#     class Meta:
#         model = Respuesta_Encuesta
#         fields = [
#             'respuesta',
#         ]

# class EncuestaForm(forms.ModelForm):
#     class Meta:
#         model = Encuesta
#         fields = [
#             'titulo',
#             'pregunta',
#             'hora_inicio',
#             'dia_inicio',
#             'hora_fin',
#             'dia_fin',
#         ]

#     def add_prefix(self, field_name):
#         field_name_mapping = {
#             'hora_fin': 'horaFin',
#             'dia_fin': 'diaFin',
#             'hora_inicio': 'horaInicio',
#             'dia_inicio':'diaInicio'
#         }
#         field_name = field_name_mapping.get(field_name, field_name)
#         return super(EncuestaForm, self).add_prefix(field_name)