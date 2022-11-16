from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission, Group

from .models import Usuario
from WebAdminRadio.models import *

def obtener_permisos_modelo(modelo):
    """
    Devuelve los permisos asociados a un modelo
    """
    id_contenido = ContentType.objects.get_for_model(modelo)
    return Permission.objects.filter(content_type=id_contenido).order_by('-codename')

def obtener_permisos():
    """
    Devuelve un diccionario con el nombre del grupo de permisos y los permisos de estos
    """
    
    # Se tiene que aumentar a medida que crecen las secciones y las tablas
    diccionario_permisos = {
        'Usuario': obtener_permisos_modelo(Usuario),
        'Roles': obtener_permisos_modelo(Group),
        'Emisoras': obtener_permisos_modelo(Emisora),
        'Programas': obtener_permisos_modelo(Programa),
        'Locutores': obtener_permisos_modelo(Locutor),
        'Torneos': obtener_permisos_modelo(Torneo),
        'Partidos': obtener_permisos_modelo(PartidoTransmision),
        'Equipos': obtener_permisos_modelo(Equipo),
        'Transmisiones': obtener_permisos_modelo(Transmision),
        'Podcast': obtener_permisos_modelo(Podcast),
        'Noticias': obtener_permisos_modelo(NoticiasTips),
        'Publicidad': obtener_permisos_modelo(Publicidad),
    }

    return diccionario_permisos

