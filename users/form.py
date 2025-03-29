from django import forms
from django.contrib.auth import authenticate

from .models import User


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password',)

    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            if not authenticate(username = username, password = password):
                raise forms.ValidationError(f"Invalid username or password")
    