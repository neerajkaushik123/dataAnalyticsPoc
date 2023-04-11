
from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import UserEmail

def yt_vid(request):
    return render(request, 'ytvideo.html')



def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user_email = UserEmail(email=email)
        user_email.save()
    return render(request, 'password.html')


#def password_page(request):
# return render(request,'password.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        if username and password == 'admin':
            user = authenticate(request, username=username, password=password)
            #login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('yt/')
        else:
            messages.error(request, 'Invalid login credentials.')
            return redirect('login')
    else:
            return render(request, 'Login Page Github.html')
    









