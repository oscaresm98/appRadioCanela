from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from WebAdminRadio.models import *
from WebAdminRadio.forms import *


# Create your views here.


@login_required
def administrador(request):
    return render(request, 'webAdminRadio/administrador.html', {'title': 'Administrador'})




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
        # emisora_form = EmisoraForm(request.POST, request.FILES)
        # if not emisora_form.is_valid():
        #     context['error'] = emisora_form.errors
        #     return render(request, 'webAdminRadio/agregar_emisora.html', context)

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
def equipos(request):
    context = {'title': 'Equipos'}
    return render(request, 'webAdminRadio/equipos.html', context)


@login_required
def agregar_equipo(request):
    context = {'title': 'Agregar Equipo'}
    if request.POST:
        equipo = request.POST['equipo']
        ciudad = request.POST['ciudad']
        user_form = EquipoForm({
            'equipo': equipo,
            'ciudad': ciudad,
        }, request.FILES)

        if user_form.is_valid():
            user_form.save()
            context['success'] = '¡El equipo ha sido registrado!'
        else:
            context['error'] = user_form.errors
    return render(request, 'webAdminRadio/agregar_equipo.html', context)