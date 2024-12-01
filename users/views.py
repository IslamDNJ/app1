from django.shortcuts import render

def login(request):
    context = {
        'title': 'Home - Авторизация'
    }
    return render(request, '', context)

def registration(request):
    context = {
        'title': 'Home - Регистрация'
    }
    return render(request, '', context)

def profile(request):
    context = {
        'title': 'Home - Кабинет'
    }
    return render(request, '', context)

def logout(request):
    ...