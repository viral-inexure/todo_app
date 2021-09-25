from .models import User, Todo, Category
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms
from django.contrib.auth.forms import UserCreationForm
from constants import (EMAIL, USERNAME)


class LoginForm(forms.ModelForm):
    username = UsernameField(label='Username/Email')

    class Meta:
        model = User
        fields = [USERNAME, 'password']


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(required=False)
    mobile_number = forms.IntegerField(required=False)

    class Meta:
        model = User
        fields = [USERNAME, EMAIL, 'mobile_number', 'password1', 'password2']


class TodoListCreate(forms.ModelForm):
    category = Category.category_name
    deadline_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Todo
        fields = ['category', 'title', 'description', 'deadline_time', 'is_important', 'is_completed']