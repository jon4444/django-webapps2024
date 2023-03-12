from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request, 'users/home.html')

def base(request):
    return render(request, 'users/base.html')

def login(request):
    return render(request, 'users/login.html')

def logout(request):
    # logout(request)
    return redirect('home')

def register(request):
    form = UserCreationForm()
    return render(request, 'users/register.html', {'form':form})
    