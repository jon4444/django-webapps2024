from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2',
        ]

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    firstname = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    lastname = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = [
            'username', 'email', 'password', 'firstname', 'lastname',
        ]