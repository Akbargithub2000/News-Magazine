from django import forms
from django.contrib.auth.models import User
from authors.models import AuthorDetailsModel

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'})
        }

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=100)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    phone_no = forms.CharField(max_length=100)
    image = forms.FileField(required=False)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    username.widget.attrs.update({'class': 'form-control'})
    email.widget.attrs.update({'class': 'form-control'})
    first_name.widget.attrs.update({'class': 'form-control'})
    last_name.widget.attrs.update({'class': 'form-control'})
    phone_no.widget.attrs.update({'class': 'form-control'})
    image.widget.attrs.update({'class': 'form-control'})
    password.widget.attrs.update({'class': 'form-control'})
    confirm_password.widget.attrs.update({'class': 'form-control'})

class EditProfileForm(forms.Form):
    username = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=100)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    phone_no = forms.CharField(max_length=100)
    image = forms.FileField(required=False)

    username.widget.attrs.update({'class': 'form-control'})
    email.widget.attrs.update({'class': 'form-control'})
    first_name.widget.attrs.update({'class': 'form-control'})
    last_name.widget.attrs.update({'class': 'form-control'})
    phone_no.widget.attrs.update({'class': 'form-control'})
    image.widget.attrs.update({'class': 'form-control'})