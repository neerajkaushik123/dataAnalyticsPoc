from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def render_page(request):
    return render(request, 'Login Page Github.html')


def authenciate_view(request):
    username=request.POST.get('Samaksh')
    password= request.POST.get('pls work')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('authenticated')
    else:
        return render(request, 'Login Page Github.html', {'error':'invalid login'})
