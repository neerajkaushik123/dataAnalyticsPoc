from django.http import HttpResponse
from django.shortcuts import render


def say_cute(request):
    return HttpResponse('Hii, if this works you are a god')
    
