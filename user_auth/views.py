from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import View
from user_auth.forms import LoginForm
from user_auth.forms import RegistrationForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.

def login_view(request):
    if request.method == "POST":
        auth_form = LoginForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(request, username = username, password = password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect("/home")
                else:
                    auth_form.add_error('__all__', "Учетная запись пользователя не активна(")
            else:
                auth_form.add_error('__all__', "Пользователя не существует")
    else:
        auth_form = LoginForm()
    context = {
        "form": auth_form,
    }
    return render(request, "auth/login.html", context=context)


def registration_view(request):
    if request.method == "POST":
        reg_form = RegistrationForm(request.POST)
        if reg_form.is_valid():
            username = reg_form.cleaned_data['username']
            existing_user = User.objects.get(username=username)
            if not existing_user:
                password = reg_form.cleaned_data['password']
                check_password = reg_form.cleaned_data['check_password']
                if password == check_password:
                    user = User.objects.create_user(username=username, password=password)
                    user.save()
                    return redirect("/auth/login/")
                else:
                    reg_form.add_error('__all__', "Пароли не совпадают")
            else:
                reg_form.add_error('__all__', "Пользователь с таким именем уже существует") 
        else:
            reg_form.add_error('__all__', "Некорректно введены данные")
    else:
        reg_form = RegistrationForm()
    context = {
        "form": reg_form,
    }
    return render(request, "auth/reg.html", context=context)


