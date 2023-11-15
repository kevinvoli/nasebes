from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


# La classe pour l'inscription

class UserRegisterForm(UserCreationForm):

    email=forms.EmailField()

    class Meta:
        model = User
        fields =['username','email','password1', 'password2']

# La classe pour la connexion

class LoginForms(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields =['username','password']
  