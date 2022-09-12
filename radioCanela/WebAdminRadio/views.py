from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def administrador(request):
    return render(request, 'webAdminRadio/administrador.html', {'title': 'Administrador'})
