from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from user.models import User
from django import forms



class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите имя аккаунта',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите пароль'
    }))
    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите ваше имя',
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите вашу фамилию',
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите имя аккаунта',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите E-mail',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите пароль', 
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Повторите пароль', 
    }))
    class Meta:
        model = User
        fields =(
            'first_name', 'last_name', 'username',
            'email', 'password1', 'password2'
        )

class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    img = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}), required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }), disabled=True)
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
    }), disabled=True)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'img', 'username', 'email')