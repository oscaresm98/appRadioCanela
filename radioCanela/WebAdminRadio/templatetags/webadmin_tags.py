from django import template
from ..models import Programa, Horario

register = template.Library()

# Devuelve los horarios de un segmento
@register.simple_tag
def get_horarios(programa):
    return Horario.objects.filter(id_programa=programa.id)