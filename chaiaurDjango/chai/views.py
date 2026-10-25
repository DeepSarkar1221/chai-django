from django.shortcuts import render
from .models import Chaivariety
# Create your views here.

def all_chai(request):
    chais=Chaivariety.objects.all()
    return render(request,'chai/all_chai.html',{'chais':chais})