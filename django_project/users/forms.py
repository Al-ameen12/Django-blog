from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# since working with the profile model, import
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User  #...
        fields = ['username', 'email', 'password1', 'password2']

# create model form, it updates the user model
class UserUpdateForm(forms.ModelForm):
    email =  forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

# create profile form
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']