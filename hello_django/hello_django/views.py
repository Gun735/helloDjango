from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    a = 'HELLO'
    return render(request, 'about.html', {'gretting': a})


def home(request):
    return HttpResponse('This is my home')