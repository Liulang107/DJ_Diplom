from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .authentication import EmailAuthBackend


def log_in(request):
    if request.method == 'POST':
        email_auth = EmailAuthBackend()
        user = email_auth.authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('index')
            else:
                return render(request, 'login.html',
                              {'err': 'Аккаунт отключен!',
                               'username': request.POST['username']
                               })
        else:
            return render(request, 'login.html',
                          {'err': 'Неверный логин или пароль!',
                           'username': request.POST['username']
                           })
    return render(request, 'login.html')


def log_out(request):
    logout(request)
    return redirect('index')
