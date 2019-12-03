from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .authentication import EmailAuthBackend
from .forms import SignupForm


def signup(request):
    if request.method == 'POST':
        user_form = SignupForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password2'])
            new_user.save()
            login(request, new_user)
            return redirect('index')
    else:
        user_form = SignupForm()
    return render(request, 'signup.html', {'form': user_form})


def log_in(request):
    context = {}
    if request.method == 'POST':
        email_auth = EmailAuthBackend()
        user = email_auth.authenticate(
            email=request.POST.get('email'),
            password=request.POST.get('password')
        )
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('index')
            else:
                context = {
                    'err': 'Аккаунт отключен!',
                    'username': request.POST.get('username')
                }
        else:
            context = {
                'err': 'Неверный логин или пароль!',
                'username': request.POST.get('username')
            }
    return render(request, 'login.html', context)


def log_out(request):
    logout(request)
    return redirect('index')
