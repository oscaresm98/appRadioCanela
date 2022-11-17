from django.shortcuts import render, redirect
from django.http import HttpRequest

from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, permission_required

from django.template.loader import render_to_string

from accounts.models import *

from WebAdminRadio.views import agregarImagen
from WebAdminRadio.forms import RolGroupForm, UsuarioAdminForm

from WebAdminRadio.emails import enviar_email


def _enviar_email_usuario(usuario, password, destinatarios):
    """

    """
    titulo = 'BIENVENIDO AL ADMINSITRADOR DE LA RADIO'
    context = { 'usuario':usuario, 'password':password }
    template = render_to_string('extras/correo.html', context)
    enviar_email(titulo,template, destinatarios, 'html')

@login_required()
@permission_required('accounts.view_usuario', login_url='/permiso-no-autorizado')
def usuarios(request: HttpRequest):
    """
    
    """

    context = {'title': 'Usuarios'}
    return render(request, 'webAdminRadio/usuarios.html', context)


def agregar_usuario(request: HttpRequest):
    """
    
    """

    roles = RolGroup.objects.filter(activo=True)
    context = {
        'title': 'Agregar Usuario', 
        'roles': roles
    }
    
    if request.POST:
        user_form = UsuarioAdminForm(request.POST)

        if not user_form.is_valid():
            context['error'] = user_form.errors
            return render(request,"webAdminRadio/agregar_usuario.html", context)

        if user_form.is_valid():
            usuario = user_form.save()
            url = agregarImagen(request, str(usuario.id), 'imagenes/')
            usuario.foto=url
            password = Usuario.objects.make_random_password()
            usuario.set_password(password)

            # _enviar_email_usuario(usuario.username, password, [usuario.email, ])            
            usuario.save()            
            
            context['success'] = '¡El usuario se ha registrado!'
            return render(request,"webAdminRadio/agregar_usuario.html", context)
            
    return render(request,"webAdminRadio/agregar_usuario.html", context)

def editar_usuario(request: HttpRequest, id_usuario):
    """
    Metodo para editar la informacion de un usuario
    """

    roles = RolGroup.objects.filter(activo=True)
    usuario_editar = Usuario.objects.get(id=id_usuario)

    context = {
        'title': 'Editar Usuario', 
        'roles': roles,
        'usuario': usuario_editar,
        'permisos_id': usuario_editar.groups.all().values_list('id', flat=True)
    }
    
    if request.POST:
        user_form = UsuarioAdminForm(request.POST, instance=usuario_editar)

        if not user_form.is_valid():
            context['error'] = user_form.errors
            return render(request,"webAdminRadio/editar_usuario.html", context)

        if user_form.is_valid():
            usuario = user_form.save()
            if(request.FILES.get('archivo', 'no') != 'no'): # Comprobando si hay un archivo nuevo para subir
                url = agregarImagen(request, str(usuario.id), 'imagenes/')
                usuario.foto=url
                usuario.save()
            context['success'] = '¡El usuario se ha registrado!'
            return render(request,"webAdminRadio/editar_usuario.html", context)

    return render(request,"webAdminRadio/editar_usuario.html", context)

def borrar_usuario(request: HttpRequest, id_usuario):
    """
    Metodo para borrar al usuario en la base de datos
    """

    delete_usuario = Usuario.objects.get(id=id_usuario)
    delete_usuario.estado = False
    delete_usuario.delete()
    messages.success(request, 'El usuario ha sido eliminado')
    return redirect('lista_usuarios')