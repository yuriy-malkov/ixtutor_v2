from django import forms
from .models import Users


class RegisterForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(label="password", required=True, max_length=255, widget=forms.PasswordInput())

    class Meta:
        model = Users
        fields = ["email", "password"]