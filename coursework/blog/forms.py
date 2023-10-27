from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import Post, Comment
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Ім'я користувача",
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )
    class Meta:
        fields = ("username", "password")
        labels = {
            'username': "Ім'я користувача",
            'password': "Пароль",
        }


class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        label="Ім'я користувача",
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )
    password2 = forms.CharField(
        label="Повторіть пароль",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )

    class Meta:
        model = User
        fields = ("username", "password1", "password2")
        labels = {
            'username': "Ім'я користувача",
            'password1': "Пароль",
            'password2': "Повторіть пароль",
        }




class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('content',)
        labels = {
            'content': 'Текст поста',
        }
        widgets = {
            'content': forms.Textarea(
                attrs={
                    'cols': None,
                    'rows': None,
                    'class': 'custom-input text-lg p-2 w-100 ',
                    'placeholder': 'Чим ви хотіли поділитися?',
                    }),
        }


class CommentForm(forms.ModelForm):

    class Meta:

        model = Comment
        fields = ['content']
        labels = {'content': 'Текст коментаря'}
        widgets = {
            'content': forms.Textarea(
                attrs={
                    'cols': None,
                    'rows': None,
                    'class': 'bg-white custom-input text-lg p-2 w-100',
                    'placeholder': 'Що ви вважаєте потрібним сказати?',
                }),
        }
