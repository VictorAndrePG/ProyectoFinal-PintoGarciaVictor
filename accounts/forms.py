from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User as UserModel
from django import forms

from accounts.models import Avatar


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = UserModel  # Cambiado de User a UserModel
        fields = ("username", "email")

class UserUpdateForm(UserChangeForm):
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = UserModel  # Cambiado de User a UserModel
        fields = ("username", "email", "password")


class AvatarUpdateForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ("imagen",)