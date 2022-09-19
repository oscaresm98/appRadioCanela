from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from WebAdminRadio.models import *
from WebAdminRadio.forms import *
from django.contrib import messages

# Create your views here.


@login_required
def administrador(request):
    return render(request, 'webAdminRadio/administrador.html', {'title': 'Administrador'})

@login_required
def agregar_usuario(request):
    # Termianar este request
    return render(request,"webAdminRadio/agregar_usuario.html")

@login_required
def editar_usuario(request,id_usuario):
    # Termianar este request
    edit_usuario = Usuario.objects.get(id=id_usuario)
    context = {
        'title': 'Editar Usuario',
        'usuario': edit_usuario,
    }
    print("USUARIOOOO")
    print(context['usuario'])
    if request.POST:
        username = request.POST['username']
        first = request.POST['nombre']
        last = request.POST['apellido']
        sexo = request.POST['sexo']
        email = request.POST['email']
        cedula = request.POST['cedula']
        nacimiento = request.POST['fechaNac']
        telefono = request.POST['telefono']
        rol = request.POST['rol']
        #foto = request.POST['foto']
        descripcion=request.POST['descripcion']
        activo=True
        try:
            activo=request.POST['activo']=='on'
        except:
            activo=False
        
        print("SEXO: ",sexo)
        print("ACTIVO: ",activo)
        user_form = UsuarioForm({
            'username':username,
            'first_name':first,
            'last_name':last,
            'sexo':sexo,
            'email':email,
            'cedula':cedula,
            'fechaNacimiento':nacimiento,
            'telefono':telefono,
            'rol':rol,
            'descripcion':descripcion,
            'activo':activo,
            #'foto':foto,
        }, request.FILES, instance=edit_usuario)
        if user_form.is_valid():
            user_form.save()
            context['success'] = '¡El usuario ha sido modificado exitosamente!'
        else:
            context['error'] = user_form.errors
    return render(request,"webAdminRadio/editar_usuario.html",context)



@login_required
#@has_permission_decorator('emisoras')
def emisoras(request):
    listaEmisoras = Emisora.objects.filter(estado=True)
    context = {'title': 'Emisoras', 'emisoras': listaEmisoras}
    return render(request, 'webAdminRadio/emisoras.html', context)


@login_required
# @has_permission_decorator('add_emisora')
def agregar_emisora(request):
    context = {'title': 'Agregar Emisora'}
    if request.POST:
        emisora_form = EmisoraForm(request.POST, request.FILES)
        if not emisora_form.is_valid():
            context['error'] = emisora_form.errors
            return render(request, 'webAdminRadio/agregar_emisora.html', context)

        # for i in range(len(request.POST.getlist('telefono'))):
        #     telefono_form = TelefonoForm({
        #         'telefono':request.POST.getlist('telefono')[i]
        #     })
        #     if not telefono_form.is_valid():
        #         context['error'] = telefono_form.errors
        #         return render(request, 'webAdminRadio/agregar_emisora.html', context)

        # for i in range(len(request.POST.getlist('red_social_nombre'))):
        #     red_form = RedSocialForm({
        #         'nombre': request.POST.getlist('red_social_nombre')[i],
        #         'link': request.POST.getlist('red_social_url')[i]
        #     })
        #     if not red_form.is_valid():
        #         context['error'] = red_form.errors
        #         return render(request, 'webAdminRadio/agregar_emisora.html', context)

        #emisora_form.save()
        # for i in range(len(request.POST.getlist('telefono'))):
        #     Telefono_emisora.objects.create(
        #         idEmisora=Emisora.objects.order_by('-id')[0],
        #         nro_telefono=request.POST.getlist('telefono')[i]
        #     )
        # for i in range(len(request.POST.getlist('red_social_nombre'))):
        #     RedSocial_emisora.objects.create(
        #         idEmisora=Emisora.objects.order_by('-id')[0],
        #         nombre=request.POST.getlist('red_social_nombre')[i],
        #         link=request.POST.getlist('red_social_url')[i]
        #     )
            context['success'] = '¡La emisora ha sido registrada con éxito!'
            return render(request, 'webAdminRadio/agregar_emisora.html', context)
    return render(request, 'webAdminRadio/agregar_emisora.html', context)


@login_required
def editar_emisora(request,pk):
    edit_emisora = Emisora.objects.get(id=pk, estado=True)
    # red_social = RedSocial_emisora.objects.filter(idEmisora=id_emisora)
    # telefono_emisora = Telefono_emisora.objects.filter(idEmisora=id_emisora)
    context = {
        'title': 'Editar Emisora',
        'emisora': edit_emisora,
        # 'telefono': json.dumps(list(telefono_emisora.values('nro_telefono')), cls=DjangoJSONEncoder),
        # 'redsocial': json.dumps(list(red_social.values('nombre', 'link')), cls=DjangoJSONEncoder)
    }
    if request.POST:
        emisora_form = EmisoraForm(request.POST, request.FILES, instance=edit_emisora)
        if not emisora_form.is_valid():
            context['error'] = emisora_form.errors
            return render(request, 'webAdminRadio/editar_emisora.html', context)

    #     for i in range(len(request.POST.getlist('telefono'))):
    #         telefono_form = TelefonoForm({
    #             'telefono': request.POST.getlist('telefono')[i]
    #         })
    #         if not telefono_form.is_valid():
    #             context['error'] = telefono_form.errors
    #             return render(request, 'webAdminRadio/modificar_emisora.html', context)

    #     for i in range(len(request.POST.getlist('red_social_nombre'))):
    #         red_form = RedSocialForm({
    #             'nombre': request.POST.getlist('red_social_nombre')[i],
    #             'link': request.POST.getlist('red_social_url')[i]
    #         })
    #         if not red_form.is_valid():
    #             context['error'] = red_form.errors
    #             return render(request, 'webAdminRadio/modificar_emisora.html', context)

    #     emisora_form.save()
    #     telefono_emisora.delete()
    #     red_social.delete()
    #     for i in range(len(request.POST.getlist('telefono'))):
    #         Telefono_emisora.objects.create(
    #             idEmisora=edit_emisora,
    #             nro_telefono=request.POST.getlist('telefono')[i]
    #         )
    #     for i in range(len(request.POST.getlist('red_social_nombre'))):
    #         RedSocial_emisora.objects.create(
    #             idEmisora=edit_emisora,
    #             nombre=request.POST.getlist('red_social_nombre')[i],
    #             link=request.POST.getlist('red_social_url')[i]
    #         )

            context['success'] = "¡La emisora ha sido modificada con éxito!"
            return render(request, 'webAdminRadio/editar_emisora.html', context)
        return render(request, 'webAdminRadio/editar_emisora.html', context)

@login_required
def equipos(request):
    context = {'title': 'Equipos'}
    return render(request, 'webAdminRadio/equipos.html', context)


@login_required
def agregar_equipo(request):
    context = {'title': 'Agregar Equipo'}
    if request.POST:
        equipo = request.POST['equipo']
        ciudad = request.POST['ciudad']
        descripcion = request.POST['descripcion']
        imagen =  request.POST['imagen']
        user_form = EquipoForm({
            'equipo': equipo,
            'ciudad': ciudad,
            'descripcion': descripcion,
            'imagen': imagen,
        })
        if user_form.is_valid():
            user_form.save()
            context['success'] = '¡El equipo ha sido registrado!'
        else:
            context['error'] = user_form.errors
    return render(request, 'webAdminRadio/agregar_equipo.html', context)


@login_required
def ver_equipo(request, id_equipo):
    equipo = Equipo.objects.get(id=id_equipo)
    context = {
        'title': 'Información del Equipo',
        'equipo': equipo,
    }
    return render(request, 'webAdminRadio/ver_equipo.html', context)

@login_required
def borrar_equipo(request, id_equipo):
    delete_equipo = Equipo.objects.get(id=id_equipo)
    delete_equipo.estado = False
    delete_equipo.delete()
    messages.success(request, 'El equipo ha sido eliminado')
    return redirect('equipos')

@login_required
def modificar_equipo(request, id_equipo):
    edit_equipo = Equipo.objects.get(id=id_equipo)
    context = {
        'title': 'Editar Equipo',
        'equipo': edit_equipo,
    }
    if request.POST:
        equipo = request.POST['equipo']
        ciudad = request.POST['ciudad']
        descripcion = request.POST['descripcion']
        imagen =  request.POST['imagen']
        user_form = EquipoForm({
            'equipo': equipo,
            'ciudad': ciudad,
            'descripcion': descripcion,
            'imagen': imagen,
        }, instance=edit_equipo)
        if user_form.is_valid():
            error=user_form.save()
            print(error)
            context['success'] = '¡El equipo ha sido modificado exitosamente!'
        else:
            context['error'] = user_form.errors
    return render(request, 'webAdminRadio/editar_equipo.html', context)