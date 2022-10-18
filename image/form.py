from django import forms
from .models import Image
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields=["caption","image"]
class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2"]