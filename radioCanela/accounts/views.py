from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

# Login del usuario


def login_user(request):
    print(request.method, "<<<<<<<<<<")
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        print(user)

        if user is not None:
            if user.is_active:
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('administrador')
                    # return render(request, 'webAdminRadio/administrador.html', {'title': 'Administrador', 'usuario': username})
            else:
                messages.error(request, 'Esta cuenta ha sido desactivada')
                return redirect('login')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrecto')
            return redirect('login')
    return render(request, 'accounts/login.html', {'title': 'Login'})

# Logout del usuario


def logout_user(request):
    if request.POST:
        logout(request)
        return redirect('login')
