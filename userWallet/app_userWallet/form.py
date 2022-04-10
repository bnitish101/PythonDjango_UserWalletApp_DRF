from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User
# from django.contrib.auth.models import User

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']