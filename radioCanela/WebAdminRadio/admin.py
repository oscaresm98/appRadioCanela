from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Emisora)
admin.site.register(Equipo)
admin.site.register(Radio)
admin.site.register(Torneo)

admin.site.register(Encuesta)
admin.site.register(Pregunta)
admin.site.register(OpcionPregunta)
