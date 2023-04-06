from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


def login_user(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        if username == "admin" and password =="admin":
            messages.success(request, 'Working')
            return redirect('login')

        
       # user = authenticate(request, username=username, password=password)
    
        # if user is not None:
        #     login(request, user)
        #     messages.success(request, 'Working')
        #     return redirect('')
        # else:
        #  messages.success(request, 'Failed')
        #  return redirect('admin/')

    else:
        return render(request, 'Login Page Github.html')



