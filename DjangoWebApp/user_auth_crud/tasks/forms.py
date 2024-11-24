from django import forms
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields =['title', 'description']


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    # Custom password validation
    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        # Minimum password length check
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        return password

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']