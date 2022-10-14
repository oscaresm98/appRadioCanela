from pickle import TRUE
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from WebAdminRadio.models import *
from WebAdminRadio.forms import *
from django.contrib import messages
from django.core.serializers.json import DjangoJSONEncoder
import json
import pyrebase
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

# configuración de firebase
firebaseConfig = {
    "apiKey": "AIzaSyDr3NaNXjIt0IJQSPsQw-jZ2fJPVv-uGKs",
    "authDomain": "radiocanela-13416.firebaseapp.com",
    "databaseURL": "https://radiocanela-13416-default-rtdb.firebaseio.com",
    "projectId": "radiocanela-13416",
    "storageBucket": "radiocanela-13416.appspot.com",
    "messagingSenderId": "182045702474",
    "appId": "1:182045702474:web:b70eebc5f65ffcd320e9b3",
    "measurementId": "G-GPTM872CX8"
}
firebase = pyrebase.initialize_app(firebaseConfig)

# Definiendo el storage
storage = firebase.storage()

# Funcion para agregar archivo a Firebase Storage, retorna el URL donde se se guardo el archivo
# Toma como parametros: el request para obtener el archico del input, el nombre para modificar la parte inicial del nombre que se sube
# y por ultimo la capeta del storage donde se quiere subir el archivo
def agregarImagen(request, nombre, carpeta):
    img = request.FILES['archivo']
    destino = carpeta + nombre + img.name # Ej. si carpeta="imagenes/", nombre = "img" y img.name="redonda.jpg" -> destino="imagenes/imgredonda.jpg"
    storage.child(destino).put(img) # al storage se sube el archivo img en la carpeta imagenes con el nombre imgredonda.jpg
    return storage.child(destino).get_url(None)

# Create your views here.


@login_required
def administrador(request):
    return render(request, 'webAdminRadio/administrador.html', {'title': 'Administrador'})

@login_required
#@has_permission_decorator('emisoras')
def usuarios(request):
    #listaUsuarios= Usuario.objects.filter(activo=True)
    listaUsuarios= Usuario.objects.all()
    context = {'title': 'Usuarios', 'usuarios':listaUsuarios}
    #return render(request,"webAdminRadio/prueba.html")
    return render(request, 'webAdminRadio/usuarios.html', context)

def geValueCheckBox(request,inputName):
    condition=True
    try:
        condition=request.POST[inputName]=='on'
    except:
        condition=False
    return condition

@login_required
#@has_permission_decorator('emisoras')
def roles(request):
    listaroles= Rol.objects.filter(activo=True)
    context = {'title': 'Lista Roles', 'roles':listaroles}
    return render(request, 'webAdminRadio/roles.html', context)
@login_required
def agregar_rol(request):
    print("DENTRO DE LA FUNCIONA AREGRAE ROL")
    labels=['Emisora','Usuario','Programa','Torneo','Equipo','Partido','Rol']
    context = {'title': 'Agregar Rol','labels':labels}
    if request.POST:
        nombre=request.POST['nombre']
        activo=True
        rol_form = RolForm({
            'nombre':nombre,
            'activo':activo,
            'descripcion':nombre
            
        })
        if rol_form.is_valid():
            
            rol=rol_form.save()
            print("Rol exitoso: ",rol)
            context['success'] = '¡El Rol se ha registrado!'
            id=rol.id
            for label in labels:
                nombre=label
                ver=geValueCheckBox(request,label+"_ver")
                agregar=geValueCheckBox(request,label+"_agregar")
                actualizar=geValueCheckBox(request,label+"_actualizar")
                borrar=geValueCheckBox(request,label+"_borrar")
                agregar_permisos(context,id,nombre,ver,agregar,actualizar,borrar)
        else:
            context['error'] = rol_form.errors
    
    print("QUE OCURRIO: ",context)
    return render(request, 'webAdminRadio/agregar_rol.html', context)

@login_required
def editar_rol(request,id_rol):
    # Termianar este request
    labels=['Emisora','Usuario','Programa','Torneo','Equipo','Partido','Rol']
    edit_rol = Rol.objects.get(id=id_rol)
    permisos_list=Permisos.objects.filter(id_rol=id_rol)
    context = {
        'title': 'Editar Usuario',
        'rol': edit_rol,
        'permisos':permisos_list
    }
    
    if request.POST:
        # Actualizar los roles
        for permiso in permisos_list:
            editar_permisos(request,permiso,context,id_rol,permiso.nombre,permiso.ver,
            permiso.agregar,permiso.actualizar,permiso.borrar)
            labels.remove(permiso.nombre)
            # Para los elementos y permisos nuevois agregados
        for label in labels:
            nombre=label
            ver=geValueCheckBox(request,label+"_ver")
            agregar=geValueCheckBox(request,label+"_agregar")
            actualizar=geValueCheckBox(request,label+"_actualizar")
            borrar=geValueCheckBox(request,label+"_borrar")
            agregar_permisos(context,id,nombre,ver,agregar,actualizar,borrar)
        context['success'] = '¡El Rol se ha actualizado!'
    else:
            context['error'] = 'Ocurrio un error al editar los  roles'
    
    return render(request,"webAdminRadio/editar_rol.html",context)
def agregar_permisos(context,id_rol,nombre,ver,agregar,actualizar,borrar):
    permisos_form=PermisosForm({
        'id_rol':id_rol,
        'nombre':nombre,
        'ver':ver,
        'agregar':agregar,
        'actualizar':actualizar,
        'borrar':borrar,
        'activo':True
    })
    if permisos_form.is_valid():
        permiso=permisos_form.save()
        print("Permisos exitoso: ",permiso)
        context['permiso_success'] = '¡El Permiso se ha registrado!'
    else:
        context['permiso_error'] = permisos_form.errors

def editar_permisos(request,intance_permiso,context,id_rol,nombre,ver,agregar,actualizar,borrar):
    permisos_form=PermisosForm({
        'id_rol':id_rol,
        'nombre':nombre,
        'ver':ver,
        'agregar':agregar,
        'actualizar':actualizar,
        'borrar':borrar,
        'activo':True
    }, request.FILES, instance=intance_permiso)
    if permisos_form.is_valid():
        permiso=permisos_form.save()
        print("Permisos exitoso: ",permiso)
        context['permiso_success'] = '¡El Permiso se ha actualizado!'
    else:
        context['permiso_error'] = permisos_form.errors

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
        #rol = request.POST['rol']
        #foto = request.POST['foto']
        descripcion=request.POST['descripcion']
        activo=geValueCheckBox(request,'activo')
        
        user_form = UsuarioForm({
            'username':username,
            'first_name':first,
            'last_name':last,
            'sexo':sexo,
            'email':email,
            'cedula':cedula,
            'fechaNacimiento':nacimiento,
            'telefono':telefono,
            #'rol':rol,
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
    print("-----PASSWORD: ",edit_usuario.password)
    print("-----HASH: ",make_password("1234"))
    print("EQUALS: ",edit_usuario.password==make_password("1234"))
    print("---SECOND EQUALS: ",check_password('1234', edit_usuario.password))
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
        #rol = request.POST['rol']
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
            #'rol':rol,
            'descripcion':descripcion,
            'activo':activo,
            #'foto':foto,
        }, request.FILES, instance=edit_usuario)
        if user_form.is_valid():
            user2=user_form.save()
            print("DATOS USUARIO FORM: ",user2.id)
            context['success'] = '¡El usuario ha sido modificado exitosamente!'
        else:
            context['error'] = user_form.errors
    return render(request,"webAdminRadio/editar_usuario.html",context)

@login_required
def borrar_rol(request, id_rol):
    delete_rol = Rol.objects.get(id=id_rol)
    delete_rol.activo = False
    delete_rol.delete()
    messages.success(request, 'El Rol ha sido eliminado')
    return redirect('lista_roles')

@login_required
def borrar_usuario(request, id_usuario):
    delete_usuario = Usuario.objects.get(id=id_usuario)
    delete_usuario.estado = False
    delete_usuario.delete()
    messages.success(request, 'El usuario ha sido eliminado')
    return redirect('lista_usuarios')


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
    context = {'title': 'Agregar Emisora', 'radios': listaRadios}

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
    # edit_radio = Radio.objects.get(id=id_emisora,estado=True)
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
        equipo_form = EquipoForm(request.POST)
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
        # Se sube la imagen a Firebase Storage y se asigna el url
        equipo = Equipo.objects.order_by('-id')[0]
        url = agregarImagen(request, str(equipo.id), 'imagenes/')
        equipo.imagen=url
        equipo.save()
        aumento=0
        for i in range(len(request.POST.getlist('red_social_nombre'))):
            if request.POST.getlist('red_social_nombre')[i] == 'Otra':
                id = comprobarRedSocial(request.POST.getlist('otra_red_social')[aumento])
                aumento=aumento+1
            else:
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
    delete_equipo.save()
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
    nombre_redes=[]
    for red in red_social:
      nombre_redes.append(red.id_red_social.nombre)
    context['nomredes']=json.dumps(list(nombre_redes), cls=DjangoJSONEncoder)
    
    if request.POST:
        equipo_form = EquipoForm(request.POST, instance=edit_equipo)
        if not equipo_form.is_valid():
            context['error'] = equipo_form.errors
            return render(request, 'webAdminRadio/agregar_equipo.html', context)
        print(len(request.POST.getlist('red_social_nombre')))
        print(request.POST.getlist('red_social_nombre'))
        print(range(len(request.POST.getlist('red_social_nombre'))))
        for i in range(len(request.POST.getlist('red_social_nombre'))):
            red_form = RedSocialForm({
                'nombre': request.POST.getlist('red_social_nombre')[i],
                'logo_red_social': request.POST.getlist('red_social_url')[i]
            })
            if not red_form.is_valid():
                context['error'] = red_form.errors
                return render(request, 'webAdminRadio/agregar_emisora.html', context)
        
        equipo_form.save()
        if(request.FILES.get('archivo', 'no') != 'no'): # Comprobando si hay un archivo nuevo para subir
                url = agregarImagen(request, str(edit_equipo.id), 'imagenes/')
                edit_equipo.imagen=url
                edit_equipo.save()
        red_social.delete()
        aumento=0
        for i in range(len(request.POST.getlist('red_social_nombre'))):
            if request.POST.getlist('red_social_nombre')[i] == 'Otra':
                id = comprobarRedSocial(request.POST.getlist('otra_red_social')[aumento])
                aumento=aumento+1
            else:
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
    list_locutores = Locutor.objects.filter(estado=True)
    context = {'title': 'Agregar Programa', 'emisoras': list_emisoras, 'locutores': list_locutores}
    
    if request.POST:
        programa_form = ProgramaForm(request.POST)
        if programa_form.is_valid():
            programa_form.save()
            # Se sube el archivo a Firebase Storage y se asigna el url
            programa = Programa.objects.order_by('-id')[0]
            url = agregarImagen(request, str(programa.id), 'imagenes/')
            programa.imagen=url
            programa.save()
            # Enlazar programa con emisora
            emisoraid = request.POST['emisora']
            SegmentoEmisora.objects.create(
                emisora=Emisora.objects.get(id=emisoraid),
                segmento=Programa.objects.order_by('-id')[0]
            )

            for i in range(len(request.POST.getlist('locutor'))):
                SegmentoLocutor.objects.create(
                    id_segmento = Programa.objects.order_by('-id')[0],
                    id_locutor = Locutor.objects.get(id=request.POST.getlist('locutor')[i])
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

@login_required
def ver_programa(request, id_programa):
    programa = Programa.objects.get(id=id_programa)
    segmentoEmisora = SegmentoEmisora.objects.get(segmento=id_programa)
    locutores = SegmentoLocutor.get_locutores(id_programa)
    
    context = {
        'title': 'Información del programa',
        'programa': programa,
        'segemntoEmisora': segmentoEmisora,
        'locutores': locutores
    }
    return render(request, 'webAdminRadio/ver_programa.html', context)

@login_required
def modificar_programa(request, id_programa):
    edit_segmento = Programa.objects.get(id=id_programa, estado=True)
    horarios = Horario.objects.filter(id_programa=id_programa)
    list_emisoras = Emisora.objects.filter(estado=True)
    segmentoEmisora = SegmentoEmisora.objects.get(segmento=id_programa)
    list_locutores = Locutor.objects.filter(estado=True)
    list_locutoresPrograma = SegmentoLocutor.objects.filter(id_segmento = id_programa)
    
    context = {
        'title': 'Editar Programa',
        'segmento': edit_segmento,
        'emisoras': list_emisoras,
        'segmentoEmisora': segmentoEmisora,
        'horarios': json.dumps(list(horarios.values('dia', 'hora_inicio', 'hora_fin')), cls=DjangoJSONEncoder),
        'locutores': list_locutores,
        'locutoresPrograma': list_locutoresPrograma
    }
    if request.POST:
        programa_form = ProgramaForm(request.POST, instance=edit_segmento)
        if programa_form.is_valid():
            programa_form.save()
            horarios.delete()
            if(request.FILES.get('archivo', 'no') != 'no'): # Comprobando si hay un archivo nuevo para subir
                url = agregarImagen(request, str(edit_segmento.id), 'imagenes/')
                edit_segmento.imagen=url
                edit_segmento.save()
            # Enlazar programa con emisora
            segmentoEmisora.emisora = Emisora.objects.get(id=request.POST['emisora'])
            segmentoEmisora.segmento = edit_segmento
            segmentoEmisora.save()

            list_locutoresPrograma.delete()
            for i in range(len(request.POST.getlist('locutor'))):
                SegmentoLocutor.objects.create(
                    id_segmento = Programa.objects.order_by('-id')[0],
                    id_locutor = Locutor.objects.get(id=request.POST.getlist('locutor')[i])
                )
            
            if request.POST['dias']=='L':
                lista = ['Lunes','Martes','Miércoles','Jueves','Viernes']
                modificarHorario(lista, context, request)

            elif request.POST['dias']=='SD':
                fds = ['Sábado','Domingo']
                modificarHorario(fds, context, request)

            elif request.POST['dias']=='S':
                modificarHorario(['Sabado'], context, request)

            elif request.POST['dias']=='D':
                modificarHorario(['Domingo'], context, request)

            if 'error' not in context:
                context['success'] = '¡El programa ha sido editado con éxito!'
            else:
                context['error'] = programa_form.errors
        return render(request, 'webAdminRadio/editar_programa.html', context)
    return render(request, 'webAdminRadio/editar_programa.html', context)


def modificarHorario(lista, context, request):
    ini= request.POST['horainicio']
    fin= request.POST['horafin']
    progra = context['segmento']
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

@login_required
def borrar_programa(request, id_programa):
    delete_segmento = Programa.objects.get(id=id_programa)
    delete_segmento.estado = False
    delete_segmento.delete()
    messages.success(request, 'El segmento ha sido eliminado')
    return redirect('programas')


# Locutores
@login_required
def locutores(request):
    context = {'title': 'Locutores'}
    return render(request, 'webAdminRadio/locutores.html', context)

@login_required
def ver_locutor(request, id_locutor):
    locutor = Locutor.objects.get(pk=id_locutor)
    redSocialLocutor = RedSocialLocutor.objects.filter(id_locutor=id_locutor)
    context = {'title': 'Informacion del Locutor', 'locutor': locutor, 'redSocialLocutor': redSocialLocutor}
    return render(request, 'webAdminRadio/ver_locutor.html', context)

@login_required
def eliminar_locutor(request, id_locutor):
    delete_locutor = Locutor.objects.get(id=id_locutor)
    delete_locutor.estado = False
    delete_locutor.delete()
    messages.success(request, 'El Locutor ha sido eliminado.')
    return redirect('locutores')

@login_required
def agregar_Locutor(request):
    context = {'title': 'Agregar Locutor'}
    if request.POST:
        locutor_form = LocutorForm(request.POST)
        print(locutor_form)
        if not locutor_form.is_valid():
            context['error'] = locutor_form.errors
            return render(request, 'webAdminRadio/agregar_locutor.html', context)
        
        for i in range(len(request.POST.getlist('red_social_nombre'))):
            red_form = RedSocialForm({
                'nombre': request.POST.getlist('red_social_nombre')[i],
                'logo_red_social': request.POST.getlist('red_social_url')[i]
            })
            if not red_form.is_valid():
                context['error'] = red_form.errors
                return render(request, 'webAdminRadio/agregar_locutor.html', context)
        
        locutor_form.save()
        for i in range(len(request.POST.getlist('red_social_nombre'))):
            id = comprobarRedSocial(request.POST.getlist('red_social_nombre')[i])
            RedSocialLocutor.objects.create(
                id_locutor=Locutor.objects.order_by('-id')[0],
                id_red_social=id,
                username = request.POST.getlist('red_social_username')[i],
                link = request.POST.getlist('red_social_url')[i]
            )
        context['success'] = '¡El/La locutor/a ha sido agregado/a con éxito!'
    return render(request, 'webAdminRadio/agregar_locutor.html', context)

@login_required
def editar_locutor(request, id_locutor):
    edit_locutor = Locutor.objects.get(id=id_locutor)
    red_social = RedSocialLocutor.objects.filter(id_locutor=id_locutor)
    context = {
        'title': 'Editar Locutor',
        'locutor': edit_locutor,
        'redsocial': json.dumps(list(red_social.values('id_red_social', 'link', 'username')), cls=DjangoJSONEncoder)
    }
    if request.POST:
        locutor_form = LocutorForm(request.POST, instance=edit_locutor)
        if not locutor_form.is_valid():
            context['error'] = locutor_form.errors
            return render(request, 'webAdminRadio/editar_locutor.html', context)
        
        for i in range(len(request.POST.getlist('red_social_nombre'))):
            red_form = RedSocialForm({
                'nombre': request.POST.getlist('red_social_nombre')[i],
                'logo_red_social': request.POST.getlist('red_social_url')[i]
            })
            if not red_form.is_valid():
                context['error'] = red_form.errors
                return render(request, 'webAdminRadio/editar_locutor.html', context)
        
        locutor_form.save()
        red_social.delete()
        for i in range(len(request.POST.getlist('red_social_nombre'))):
            id = comprobarRedSocial(request.POST.getlist('red_social_nombre')[i])
            RedSocialLocutor.objects.create(
                id_locutor = edit_locutor,
                id_red_social = id,
                username = request.POST.getlist('red_social_username')[i],
                link = request.POST.getlist('red_social_url')[i]
            )

        context['success'] = '¡El/La locutor/a ha sido modificado/a con éxito!'

        return render(request, 'webAdminRadio/editar_locutor.html', context)

    return render(request, 'webAdminRadio/editar_locutor.html', context)


# Publicidad
@login_required
def publicidad(request):
    list_radios = Radio.objects.filter(estado=True)
    list_programas = Programa.objects.filter(estado=True)
    context = {
        'title': 'Publicidad',
        'programas': list_programas,
        'radios': list_radios,
    }
    return render(request, 'webAdminRadio/publicidad.html', context)

@login_required
def agregar_publicidad(request):
    list_radios = Radio.objects.filter(estado=True)
    context = {
        'title': 'Agregar Publicidad',
        'radios': list_radios
        }
    if request.POST:
        publicidad_form = PublicidadForm(request.POST)
        if publicidad_form.is_valid():
            publicidad_form.save()
            # Se sube el archivo a Firebase Storage y se asigna el url
            publi = Publicidad.objects.order_by('-id')[0]
            url = agregarImagen(request, str(publi.id), 'imagenes/')
            publi.imagen=url
            publi.save()
            context['success'] = '¡El registro de la publicidad se ha sido creado con éxito!'
        else:
            context['error'] = publicidad_form.errors
    return render(request, 'webAdminRadio/agregar_publicidad.html', context)

@login_required
def ver_publicidad(request, id_publicidad):
    publicidad = Publicidad.objects.get(id=id_publicidad)
    context = {
        'title': "Informacion de la publicidad",
        'publicidad':publicidad,
    }
    return render(request, 'webAdminRadio/ver_publicidad.html', context)

@login_required
def modificar_publicidad(request, id_publicidad):
    edit_publicidad = Publicidad.objects.get(id=id_publicidad)
    list_radios = Radio.objects.all()
    fechainicio = str(edit_publicidad.fecha_inicio)[0:10]
    fechafin = str(edit_publicidad.fecha_fin)[0:10]
    context = {
        'title': 'Editar Publicidad',
        'publicidad': edit_publicidad,
        'radios': list_radios,
        'fechainicio': fechainicio,
        'fechafin': fechafin,
    }
    if request.POST:
        publicidad_form = PublicidadForm(request.POST, instance=edit_publicidad)
        if publicidad_form.is_valid():
            publicidad_form.save()
            if(request.FILES.get('archivo', 'no') != 'no'): # Comprobando si hay un archivo nuevo para subir
                url = agregarImagen(request, str(edit_publicidad.id), 'imagenes/')
                edit_publicidad.imagen=url
                edit_publicidad.save()
            context['success'] = '¡El registro ha sido modificado con éxito!'
        else:
            context['error'] = publicidad_form.errors
    return render(request, 'webAdminRadio/editar_publicidad.html', context)


@login_required
def borrar_publicidad(request, id_publicidad):
    delete_publicidad = Publicidad.objects.get(id=id_publicidad)
    delete_publicidad.estado = False
    delete_publicidad.save()
    messages.success(request, 'La publicidad ha sido eliminada con exito')
    return redirect('publicidad')

# Noticia
@login_required
def noticia(request):
    list_emisoras = Emisora.objects.filter(estado=True)
    context = {
        'title': 'Noticias y Tips',
        'emisoras': list_emisoras,
    }
    return render(request, 'webAdminRadio/noticias.html', context)


@login_required
def agregar_noticia(request):
    list_emisoras = Emisora.objects.filter(estado=True)
    context = {
        'title': 'Agregar Noticia/Tips',
        'emisoras': list_emisoras
        }
    if request.POST:
        noticia_form = NoticiaForm(request.POST)
        if noticia_form.is_valid():
            noticia_form.save()
            # Se sube el archivo a Firebase Storage y se asigna el url
            noticia = NoticiasTips.objects.order_by('-id')[0]
            url = agregarImagen(request, str(noticia.id), 'imagenes/')
            noticia.imagen=url
            noticia.save()
            context['success'] = '¡El registro de la publicidad se ha sido creado con éxito!'
        else:
            context['error'] = noticia_form.errors
    return render(request, 'webAdminRadio/agregar_noticia.html', context)

@login_required
def ver_noticia(request, id_noticia):
    noticia = NoticiasTips.objects.get(id=id_noticia)
    context = {
        'title': "Informacion de la noticia",
        'noticia': noticia,
    }
    return render(request, 'webAdminRadio/ver_noticia.html', context)

@login_required
def modificar_noticia(request, id_noticia):
    edit_noticia = NoticiasTips.objects.get(id=id_noticia)
    list_emisoras = Emisora.objects.filter(estado=True)
    fechasubida = str(edit_noticia.fecha_subida)[0:10]
    context = {
        'title': 'Editar Noticia o Tip',
        'noticia': edit_noticia,
        'emisoras': list_emisoras,
        'fechasubida': fechasubida,
    }
    if request.POST:
        noticia_form = NoticiaForm(request.POST, instance=edit_noticia)
        if noticia_form.is_valid():
            noticia_form.save()
            if(request.FILES.get('archivo', 'no') != 'no'): # Comprobando si hay un archivo nuevo para subir
                url = agregarImagen(request, str(edit_noticia.id), 'imagenes/')
                edit_noticia.imagen=url
                edit_noticia.save()
            context['success'] = '¡El registro ha sido modificado con éxito!'
        else:
            context['error'] = noticia_form.errors
    return render(request, 'webAdminRadio/editar_noticia.html', context)

@login_required
def borrar_noticia(request, id_noticia):
    delete_noticia = NoticiasTips.objects.get(id=id_noticia)
    delete_noticia.estado = False
    delete_noticia.save()
    messages.success(request, 'La noticia/tip ha sido eliminada con exito')
    return redirect('noticia')