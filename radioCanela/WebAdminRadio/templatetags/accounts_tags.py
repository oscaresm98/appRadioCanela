from django import template
from accounts.models import *
from django.contrib.auth.models import Permission, Group

register = template.Library()

@register.filter
def obtener_tipo_permiso(value: Permission):
    """
    Devuelve el nombre de la accion de acuerdo al nombre codigo del permiso
    """

    accion = value.codename.split('_')[0]
    if accion == 'add':
        return 'Agregar'
    elif accion == 'view':
        return 'Visualizar'
    elif accion == 'change':
        return 'Actualizar'
    elif accion == 'delete':
        return 'Borrar'

    return accion

@register.filter
def verificar_permiso(usuario: Usuario, nombre_permiso: str):
    """
    Devuelve True si en el rol del usuario existe el permiso pasado como argumento
    """
    return usuario.has_perm(nombre_permiso)

@register.filter
def cambiar_espacios_nombre_seccion(nombre_seccion: str):
    '''
    Esta funcion cambia los espacios que hay en el nombre de una seccion por '_'
    Sirve para evitar malas asignaciones de nombres a inputs
    '''
    if ' ' in nombre_seccion:
        return nombre_seccion.replace(' ', '_')
    return nombre_seccion