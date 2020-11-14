from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    username = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(required=True, label='', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.PasswordInput()

    class Meta:
        model = User
        fields = ("username",
                  "email", 
                  "password1",
                  "password2")


    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
