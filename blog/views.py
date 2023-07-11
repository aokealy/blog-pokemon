from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def core(request):
    return HttpResponse('core page')

def about(request):
    return HttpResponse('about page')    
