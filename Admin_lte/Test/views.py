from django.http import HttpResponse, request
from django.shortcuts import render


def render_page(request):
    return render(request, 'Login Page Github.html')
