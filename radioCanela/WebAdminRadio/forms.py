from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm

# field_name_mapping es el diccionario con los names que estarán en los forms,
# que no deben ser iguales a los campos de los modelos
class EmisoraForm(forms.ModelForm):
    class Meta:
        model= Emisora
        fields = [
            
            'frecuencia_dial',
            'tipo_frecuencia',
            
            'url_streaming',
            'direccion',
            'ciudad',
            'provincia'
            
        ]

    # def add_prefix(self, field_name):
    #     field_name_mapping = {
    #         'url_streaming': 'streaming',
    #         'frecuencia_dial': 'frecuencia',
    #         'sitio_web': 'sitioweb'
    #     }
    #     field_name = field_name_mapping.get(field_name, field_name)
    #     return super(EmisoraForm, self).add_prefix(field_name)

# class TelefonoForm(forms.Form):
#     telefono = forms.RegexField(regex=r"(\+)?[0-9]+", max_length=10)

# class RedSocialForm(forms.Form):
#     nombre = forms.CharField(max_length=25, required=False)
#     link = forms.URLField(max_length=250, required=False)

# class PublicidadForm(forms.ModelForm):
#     class Meta:
#         model = Publicidad
#         fields = [
#             'titulo',
#             'cliente',
#             'descripcion',
#             'url',
#             'imagen'
#             ]

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

# class SegmentoForm(forms.ModelForm):
#     class Meta:
#         model = Segmento
#         fields = [
#             'nombre',
#             'slogan',
#             'descripcion',
#             'idEmisora',
#             'imagen'
#         ]
#     # Esta función define el atributo 'name' con el valor del diccionario
#     def add_prefix(self, field_name):
#         field_name_mapping = {
#             'idEmisora': 'emisora'
#         }
#         field_name = field_name_mapping.get(field_name, field_name)
#         return super(SegmentoForm, self).add_prefix(field_name)

# class HorarioForm(forms.ModelForm):
#     class Meta:
#         model = Horario
#         fields = [
#             'dia',
#             'fecha_inicio',
#             'fecha_fin'
#         ]

#     def add_prefix(self, field_name):
#         field_name_mapping = {
#             'fecha_inicio': 'inicio',
#             'fecha_fin': 'fin'
#         }
#         field_name = field_name_mapping.get(field_name, field_name)
#         return super(HorarioForm, self).add_prefix(field_name)

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

# class TorneoForm(forms.ModelForm):
#     class Meta:
#         model = Torneo
#         fields = [
#             'nombre',
#             'lugar'
#         ]

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = [
            'equipo',
            'ciudad',
            'descripcion',
            'imagen'
        ]

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

# class PodcastForm(forms.ModelForm):
#     emisora = forms.ModelChoiceField(queryset=Emisora.objects.all())

#     class Meta:
#         model = Podcast
#         fields = [
#             'nombre',
#             'descripcion',
#             'audio',
#             'fecha',
#             'emisora'
#         ]

# class PodcastEmisoraForm(forms.ModelForm):

#     class Meta:
#         model = PodcastEmisora
#         fields = [
#             'emisora'
#         ]

# class TransmisionEmisoraForm(forms.ModelForm):
    
#     class Meta:
#         model = TransmisionEmisora
#         fields = [
#             'emisora'
#         ]

# class TransmisionForm(forms.ModelForm):
#     equipo1 = forms.ModelChoiceField(queryset=Equipo.objects.all())
#     equipo2 = forms.ModelChoiceField(queryset=Equipo.objects.all())
#     evento = forms.ModelChoiceField(queryset=Torneo.objects.all())

#     class Meta:
#         model = Transmision
#         fields = [
#             'hora_inicio',
#             'fecha_evento',
#             'lugar',
#             'evento',
#             'descripcion',
#             'equipo1',
#             'equipo2'
#         ]

#     def add_prefix(self, field_name):
#         field_name_mapping = {
#             'hora_inicio': 'hora',
#             'fecha_evento': 'fecha',
#         }
#         field_name = field_name_mapping.get(field_name, field_name)
#         return super(TransmisionForm, self).add_prefix(field_name)  

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