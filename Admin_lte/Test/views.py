from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages



def yt_vid(request):
    return render(request, 'ytvideo.html')

def login_user(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        if username == "admin" and password =="admin":
            messages.success(request, 'Working')
            return redirect('yt/')

        
        else:
            messages.error(request, 'Invalid login credentials.')
            return redirect('login')
    else:
        return render(request, 'Login Page Github.html')

