from django.http import HttpResponse


def home(request):
    return HttpResponse('Hello from chai code home')

def about(request):
    return HttpResponse('Hello from chai code about')

def contact(request):
    return HttpResponse('Hello from chai code contact')

