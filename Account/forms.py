from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserSignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control text-center mt-2', 'placeholder': 'username'})
        self.fields['email'].widget.attrs.update({'class': 'form-control text-center mt-2', 'placeholder': 'email'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control text-center mt-2', 'placeholder': 'password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control text-center mt-2', 'placeholder': 'confrim password'})

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
