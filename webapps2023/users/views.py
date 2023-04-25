from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, EditProfileForm
# from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.views import generic
from django.urls import reverse_lazy


# Create your views here.
class UserEditView(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'users/edit_profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user

def home(request):
    return render(request, 'users/home.html')

# def base(request):
#     return render(request, 'users/base.html')

# def login(request):
#     return render(request, 'users/login.html')

def logout(request):
    # logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form':form})

@login_required()
def profile(request):
    return render(request, 'users/profile.html')



    