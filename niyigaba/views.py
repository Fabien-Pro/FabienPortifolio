from urllib import request
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html',{});

def skills(request):
    return render(request, 'skills.html', {});

def login(request):
    return render(request, 'login.html', {});
def register(request):
    return render(request,'register.html',{});
    
    