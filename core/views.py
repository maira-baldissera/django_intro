from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse('Hello, World')

def soma(request, int_1, int_2):
    return HttpResponse(int(int_1)+int(int_2))