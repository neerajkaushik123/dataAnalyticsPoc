from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


def login_user(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
    
        if user is not None:
            login(request, user)
            return redirect('Test')
        else:
         messages.success(request, 'Failed')
         return redirect('admin/')

    else:
        return render(request, 'Login Page Github.html')



