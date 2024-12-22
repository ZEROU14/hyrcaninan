from django.shortcuts import render
from django.views import generic
# Create your views here.

def homepage(request):
    return render(request,'home.html')

def aboutus(request):
    return render(request,'pages/aboutus.html')