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
