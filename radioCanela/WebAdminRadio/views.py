from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from WebAdminRadio.models import *
from WebAdminRadio.forms import *
from django.contrib import messages
from django.core.serializers.json import DjangoJSONEncoder
import json
# Create your views here.


@login_required
def administrador(request):
    return render(request, 'webAdminRadio/administrador.html', {'title': 'Administrador'})

@login_required
def agregar_usuario(request):
    context = {'title': 'Agregar Usuario'}
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
        })
        
        if user_form.is_valid():
            user_form.save()
            context['success'] = '¡El usuario se ha registrado!'
        else:
            context['error'] = user_form.errors
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
    listaRadios= Radio.objects.filter(estado=True)
    listaEmisoras = Emisora.objects.filter(estado=True)
    context = {'title': 'Emisoras', 'emisoras': listaEmisoras, 'radios': listaRadios}
    return render(request, 'webAdminRadio/emisoras.html', context)

@login_required
def agregar_radio(request):
    context = {'title': 'Agregar Radio'}
    if request.POST:
        nombre = request.POST['nombre']
        logotipo = request.POST['imagen']
        sitio_web = request.POST['sitio_web']
        descripcion = request.POST['descripcion']
        # imagen =  request.POST['imagen']
        user_form = RadioForm({
            'nombre': nombre,
            # 'imagen': imagen,
            'logotipo': logotipo,
            'sitio_web': sitio_web,
            'descripcion': descripcion
        })
        
        if user_form.is_valid():
            user_form.save()
            context['success'] = '¡La radio se ha registrado!'
        else:
            context['error'] = user_form.errors
    return render(request, 'webAdminRadio/agregar_radio.html', context)


@login_required
# @has_permission_decorator('add_emisora')
def agregar_emisora(request):
    listaRadios= Radio.objects.filter(estado=True)
    context = {'title': 'Agregar Emisora','radios': listaRadios}
    if request.POST:
        id_radio = request.POST['id_radio']
        frecuencia_dial = request.POST['frecuencia_dial']
        tipo_frecuencia = request.POST['tipo_frecuencia']
        url_streaming = request.POST['url_streaming']
        direccion = request.POST['direccion']
        ciudad = request.POST['ciudad']
        provincia = request.POST['provincia']
        url_streaming = request.POST['url_streaming']
        emisora_form = EmisoraForm({
            'id_radio': id_radio,
            'frecuencia_dial': frecuencia_dial,
            'tipo_frecuencia': tipo_frecuencia,
            'direccion': direccion,
            'url_streaming': url_streaming,
            'ciudad': ciudad,
            'provincia': provincia,
            'estado': True,
        })
        
        if not emisora_form.is_valid():
            context['error'] = emisora_form.errors
            return render(request, 'webAdminRadio/agregar_emisora.html', context)
        
        emisora_form.save()
        context['success'] = '¡La emisora ha sido registrada con éxito!'
    return render(request, 'webAdminRadio/agregar_emisora.html', context)

@login_required
def borrar_emisora(request, id_emisora):
    delete_emisora = Emisora.objects.get(id=id_emisora)
    delete_emisora.estado = False
    delete_emisora.delete()
    messages.success(request, 'La emisora ha sido eliminado')
    return redirect('emisora')

@login_required
def borrar_radio(request, id_radio):
    delete_radio = Radio.objects.get(id=id_radio)
    delete_radio.estado = False
    delete_radio.delete()
    messages.success(request, 'La radio ha sido eliminado')
    return redirect('emisora')


@login_required
def editar_emisora(request,id_emisora):
    edit_emisora = Emisora.objects.get(id=id_emisora, estado=True)
    edit_radio = Radio.objects.get(id=id_emisora,stado=True)
    # red_social = RedSocial_emisora.objects.filter(idEmisora=id_emisora)
    context = {
        'title': 'Editar Emisora',
        'emisora': edit_emisora,
        # 'redsocial': json.dumps(list(red_social.values('nombre', 'link')), cls=DjangoJSONEncoder)
    }
    if request.POST:
        emisora_form = EmisoraForm(request.POST, request.FILES, instance=edit_emisora)
        if not emisora_form.is_valid():
            context['error'] = emisora_form.errors
            return render(request, 'webAdminRadio/editar_emisora.html', context)
        elif emisora_form.is_valid():
            context['success'] = "¡La emisora ha sido modificada con éxito!"
            return render(request, 'webAdminRadio/editar_emisora.html', context)
        
        return render(request, 'webAdminRadio/editar_emisora.html', context)

# Equipos

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
        equipo_form = EquipoForm({
            'equipo': equipo,
            'ciudad': ciudad,
            'descripcion': descripcion,
            'imagen': imagen,
        })
        if not equipo_form.is_valid():
            context['error'] = equipo_form.errors
            return render(request, 'webAdminRadio/agregar_equipo.html', context)
        
        for i in range(len(request.POST.getlist('red_social_nombre'))):
            red_form = RedSocialForm({
                'nombre': request.POST.getlist('red_social_nombre')[i],
                'logo_red_social': request.POST.getlist('red_social_url')[i]
            })
            if not red_form.is_valid():
                context['error'] = red_form.errors
                return render(request, 'webAdminRadio/agregar_emisora.html', context)
        
        equipo_form.save()
        for i in range(len(request.POST.getlist('red_social_nombre'))):
            id = comprobarRedSocial(request.POST.getlist('red_social_nombre')[i])
            RedSocialEquipo.objects.create(
                id_equipo=Equipo.objects.order_by('-id')[0],
                id_red_social=id,
                link=request.POST.getlist('red_social_url')[i]
            )
        context['success'] = '¡La emisora ha sido registrada con éxito!'
    return render(request, 'webAdminRadio/agregar_equipo.html', context)


def comprobarRedSocial (nom):
    if len(RedSocial.objects.filter(nombre=nom))>0:
        return RedSocial.objects.get(nombre=nom)
    else:
        lowerNom=nom.lower()
        RedSocial.objects.create(
            nombre = nom,
            logo_red_social = 'fab fa-' + lowerNom
        )
        return RedSocial.objects.get(nombre=nom)

@login_required
def ver_equipo(request, id_equipo):
    equipo = Equipo.objects.get(id=id_equipo)
    redSociaEquipo = RedSocialEquipo.objects.filter(id_equipo=id_equipo)        
    context = {
        'title': 'Información del Equipo',
        'equipo': equipo,
        'redSociaEquipo': redSociaEquipo,
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
    red_social = RedSocialEquipo.objects.filter(id_equipo=id_equipo)
    context = {
        'title': 'Editar Equipo',
        'equipo': edit_equipo,
        'redsocial': json.dumps(list(red_social.values('id_red_social', 'link')), cls=DjangoJSONEncoder)
    }
    if request.POST:
        equipo = request.POST['equipo']
        ciudad = request.POST['ciudad']
        descripcion = request.POST['descripcion']
        imagen =  request.POST['imagen']
        equipo_form = EquipoForm({
            'equipo': equipo,
            'ciudad': ciudad,
            'descripcion': descripcion,
            'imagen': imagen,
        }, instance=edit_equipo)
        if not equipo_form.is_valid():
            context['error'] = equipo_form.errors
            return render(request, 'webAdminRadio/agregar_equipo.html', context)
        
        for i in range(len(request.POST.getlist('red_social_nombre'))):
            red_form = RedSocialForm({
                'nombre': request.POST.getlist('red_social_nombre')[i],
                'logo_red_social': request.POST.getlist('red_social_url')[i]
            })
            if not red_form.is_valid():
                context['error'] = red_form.errors
                return render(request, 'webAdminRadio/agregar_emisora.html', context)
        
        equipo_form.save()
        red_social.delete()
        for i in range(len(request.POST.getlist('red_social_nombre'))):
            id = comprobarRedSocial(request.POST.getlist('red_social_nombre')[i])
            RedSocialEquipo.objects.create(
                id_equipo=edit_equipo,
                id_red_social=id,
                link=request.POST.getlist('red_social_url')[i]
            )
        context['success'] = '¡La emisora ha sido registrada con éxito!'
    return render(request, 'webAdminRadio/editar_equipo.html', context)


#Torneos

@login_required
def torneos(request):
    list_torneos = Torneo.objects.all()
    context = { "title": "Torneos", "torneos": list_torneos }
    return render(request, 'webAdminRadio/torneos.html', context)

@login_required
def agregar_torneo(request):
    context = { "title": "Agregar Torneo" }

    if request.POST:
        torneo_form = TorneoForm(request.POST)
        if torneo_form.is_valid():
            error = torneo_form.save()
            context['success'] = '¡El torneo ha sido registrado!'
        else:
            context['error'] = torneo_form.errors

    return render(request, 'webAdminRadio/agregar_torneos.html', context)

@login_required
def modificar_torneo(request, id_torneo):
    torneo_modificacion = Torneo.objects.get(pk=id_torneo)
    context = { "title": "Editar Torneo", "torneo": torneo_modificacion }

    if request.POST:
        torneo_form = TorneoForm(request.POST, instance=torneo_modificacion)
        if torneo_form.is_valid():
            error = torneo_form.save()
            context['success'] = '¡Se ha guardado los cambios!'
        else:
            context['error'] = torneo_form.errors

    return render(request, 'webAdminRadio/editar_torneos.html', context)

@login_required
def eliminar_torneo(request, id_torneo):
    torneo_borrar = Torneo.objects.get(id=id_torneo)
    torneo_borrar.estado = False
    torneo_borrar.delete()
    messages.success(request, 'El torneo ha sido eliminado')
    return redirect('torneos')

# Partidos

@login_required
def partidos(request):
    context = {'title': 'Partidos'}
    return render(request, 'webAdminRadio/partidos.html', context)

@login_required
def ver_partido(request, id_partido):
    partido = PartidoTransmision.objects.get(pk=id_partido)
    context = {'title': 'Informacion del partido', 'partido': partido}
    return render(request, 'webAdminRadio/ver_partido.html', context)

@login_required
def agregar_partido(request):
    lista_equipos = Equipo.objects.filter(estado=True)
    lista_torneos = Torneo.objects.filter(estado=True)
    lista_emisoras = Emisora.objects.filter(estado=True)
    context = { 'title': 'Agregar Partido', 'equipos': lista_equipos, 'torneos': lista_torneos, 'emisoras': lista_emisoras }

    if request.POST:
        user_form = PartidoTransmisionForm(request.POST)

        if not user_form.is_valid():
            context['error'] = user_form.errors
            return render(request, 'webAdminRadio/agregar_partidos.html', context)

        for i in range(len(request.POST.getlist('emisora'))):
            red_form = PartidoTransmisionEmisoraForm({
                'id_emisora': request.POST.getlist('emisora')[i]
            })
            if not red_form.is_valid():
                context['error'] = red_form.errors
                return render(request, 'webAdminRadio/agregar_partidos.html', context)

        user_form.save()

        for i in range(len(request.POST.getlist('emisora'))):
            PartidoTransmisionEmisora.objects.create(
                id_partido=PartidoTransmision.objects.order_by('-id')[0],
                id_emisora=Emisora(request.POST.getlist('emisora')[i])
            )
        context['success'] = '¡El partido ha sido registrado!'
        return render(request, 'webAdminRadio/agregar_partidos.html', context)

    return render(request, 'webAdminRadio/agregar_partidos.html', context)

@login_required
def editar_partido(request, id_partido):
    lista_equipos = Equipo.objects.filter(estado=True)
    lista_torneos = Torneo.objects.filter(estado=True)
    lista_emisoras = Emisora.objects.filter(estado=True)
    partido_edicion = PartidoTransmision.objects.get(id=id_partido)
    partido_emisora_edicion = PartidoTransmisionEmisora.objects.filter(id_partido=id_partido)

    context = { 
        'title': 'Agregar Partido', 
        'equipos': lista_equipos, 
        'torneos': lista_torneos, 
        'emisoras': lista_emisoras,
        'partido_editar': partido_edicion,
    }

    if request.POST:
        user_form = PartidoTransmisionForm(request.POST, instance=partido_edicion)

        if not user_form.is_valid():
            context['error'] = user_form.errors
            return render(request, 'webAdminRadio/editar_partidos.html', context)

        for i in range(len(request.POST.getlist('emisora'))):
            red_form = PartidoTransmisionEmisoraForm({
                'id_emisora': request.POST.getlist('emisora')[i]
            })
            if not red_form.is_valid():
                context['error'] = red_form.errors
                return render(request, 'webAdminRadio/editar_partidos.html', context)

        user_form.save()
        partido_emisora_edicion.delete()

        for i in range(len(request.POST.getlist('emisora'))):
            PartidoTransmisionEmisora.objects.create(
                id_partido=PartidoTransmision.objects.order_by('-id')[0],
                id_emisora=Emisora(request.POST.getlist('emisora')[i])
            )
        context['success'] = '¡El partido ha sido modificado exitosamente!'

        return render(request, 'webAdminRadio/editar_partidos.html', context)

    return render(request, 'webAdminRadio/editar_partidos.html', context)

@login_required
def eliminar_partido(request, id_partido):
    partido_borrar = PartidoTransmision.objects.get(id=id_partido)
    partido_borrar.estado = False
    partido_borrar.delete()
    messages.success(request, 'El partido ha sido eliminado')
    return redirect('partidos')


# Programas

@login_required
def programas(request):
    list_emisoras = Emisora.objects.filter(estado=True)
    context = {'title': 'Programas', 'emisoras': list_emisoras}
    return render(request, 'webAdminRadio/programas.html', context)


@login_required
def agregar_programa(request):
    list_emisoras = Emisora.objects.filter(estado=True)
    context = {'title': 'Agregar Programa', 'emisoras': list_emisoras}
    if request.POST:
        programa_form = ProgramaForm(request.POST)
        if programa_form.is_valid():
            programa_form.save()
            emisoraid = request.POST['emisora']
            # Enlazar programa con emisora
            SegmentoEmisora.objects.create(
                emisora=Emisora.objects.get(id=emisoraid),
                segmento=Programa.objects.order_by('-id')[0]
            )
            if request.POST['dias']=='L':
                lista = ['Lunes','Martes','Miércoles','Jueves','Viernes']
                agregarHorario(lista, context, request)

            elif request.POST['dias']=='SD':
                fds = ['Sábado','Domingo']
                agregarHorario(fds, context, request)

            elif request.POST['dias']=='S':
                agregarHorario(['Sabado'], context, request)

            elif request.POST['dias']=='D':
                agregarHorario(['Domingo'], context, request)

            if 'error' not in context:
                context['success'] = '¡El programa ha sido creado con éxito!'
            else:
                context['error'] = programa_form.errors
        return render(request, 'webAdminRadio/agregar_programa.html', context)
    return render(request, 'webAdminRadio/agregar_programa.html', context)


def agregarHorario(lista, context, request):
    ini= request.POST['horainicio']
    fin= request.POST['horafin']
    progra = Programa.objects.order_by('-id')[0]
    for i in lista:
        # Creación del horario
        horario_form = HorarioForm({
            'programa': progra,
            'dia': i,
            'hora_inicio': ini,
            'hora_fin': fin,
        })
        if horario_form.is_valid():
            horario_form.save()
        else:
            context['error'] = horario_form.errors
            break