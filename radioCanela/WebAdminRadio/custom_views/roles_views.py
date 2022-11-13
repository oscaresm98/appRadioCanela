from django.shortcuts import render, redirect
from django.http import HttpRequest

from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, permission_required

from accounts.models import *
from WebAdminRadio.forms import RolGroupForm

import accounts.roles as funciones_rol

@login_required()
@permission_required('accounts.view_group', login_url='/permiso-no-autorizado')
def roles(request):
    """
    Devuelve la pagina con la lista de roles
    """

    context = {'title': 'Lista Roles'}
    return render(request, 'webAdminRadio/roles.html', context)

@login_required()
@permission_required('accounts.add_group')
def agregar_roles(request: HttpRequest):
    """
    Maneja el formulario para poder crear un nuevo rol
    """

    context = {
        'title': 'Agregar Rol',
        'grupos': funciones_rol.obtener_permisos(),
    }
    if request.POST:
        formulario = RolGroupForm(data=request.POST)

        if not formulario.is_valid():
            context['error'] = formulario.errors
            return render(request, 'webAdminRadio/agregar_rol.html', context)
        
        if formulario.is_valid():
            rol = formulario.save()
            context['success'] = '¡El Rol ha sido registrado!'
            return render(request, 'webAdminRadio/agregar_rol.html', context)

    return render(request, 'webAdminRadio/agregar_rol.html', context)

@login_required()
@permission_required('accounts.change_group', login_url='/permiso-no-autorizado')
def editar_rol(request: HttpRequest, id_rol):
    """
    
    """
    grupo_permisos = RolGroup.objects.get(id=id_rol)
    lista_ids_permisos = grupo_permisos.permissions.all().values_list('id', flat=True)
    context = {
        'title': 'Editar Rol',
        'grupos': funciones_rol.obtener_permisos(),
        'grupo_editar': grupo_permisos,
        'permisos_asignados': lista_ids_permisos,
    }

    if request.POST:
        print(request.POST['activo'])

        formulario = RolGroupForm(request.POST, instance=grupo_permisos)

        if not formulario.is_valid():
            context['error'] = formulario.errors
            return render(request, 'webAdminRadio/editar_rol.html', context)
        
        if formulario.is_valid():
            grupo_edicion = formulario.save()
            context['success'] = '¡El Rol ha sido modificado exitosamente!'
            return render(request, 'webAdminRadio/editar_rol.html', context)

    return render(request, 'webAdminRadio/editar_rol.html', context)

@login_required()
@permission_required('accounts.delete_group')
def borrar_rol(request, id_rol):
    """
    
    """
    grupo_permisos = RolGroup.objects.get(id=id_rol)
    grupo_permisos.delete()
    messages.success(request, 'El Rol ha sido eliminado')
    return redirect('lista_roles')
    