from django import template
from ..models import Programa, Horario, SegmentoEmisora, SegmentoLocutor, TelefonoEmisora

register = template.Library()

# Devuelve los horarios de un segmento
@register.simple_tag
def get_horarios(programa):
    return Horario.objects.filter(id_programa=programa.id)

# Devuelve el teléfono de una emisora
@register.simple_tag
def get_telf_emisora(emisora):
    return TelefonoEmisora.objects.filter(id_emisora=emisora.id)

# Devuelve la cantidad de segmentos de una emisora
@register.simple_tag
def get_cant_segmentos(emisora):
    return Programa.objects.filter(pk__in=SegmentoEmisora.objects.filter(emisora=emisora).values('segmento'), estado=True).count()

# Devuelve la cantidad de locutores de una emisora
@register.simple_tag
def get_cant_locutores(emisora):
    count = 0
    list_segmentos = Programa.objects.filter(pk__in=SegmentoEmisora.objects.filter(emisora=emisora).values('segmento'), estado=True)
    for segmento in list_segmentos:
        count += SegmentoLocutor.objects.filter(id_segmento=segmento.id).count()
    return count