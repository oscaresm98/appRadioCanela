from django.contrib import admin
from django.contrib.auth.models import Permission
from .models import *

# Clases para modificar el admin
class UsuarioAdmin(admin.ModelAdmin):
    filter_horizontal = ("groups", "user_permissions")

class RolGroupAdmin(admin.ModelAdmin):
    filter_horizontal = ("permissions",)

# Register your models here.

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(RolGroup, RolGroupAdmin)
admin.site.register(Permission)