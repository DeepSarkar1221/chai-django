from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse('Hello from chai code home')
    return render(request,'index.html')

def about(request):
    return HttpResponse('Hello from chai code about')

def contact(request):
    return HttpResponse('Hello from chai code contact')

