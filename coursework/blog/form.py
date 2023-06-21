from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import Post, Comment
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Ім'я користувача")
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)

    class Meta:
        fields = ("username", "password")
        labels = {
            'username': "Ім'я користувача",
            'password': "Пароль",
        }


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label="Ім'я користувача")
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Повторіть пароль", widget=forms.PasswordInput)

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
                    'rows': 3,
                    'class': 'post bg-white',
                    'style': "height: 100%; width: 100%; border: none; resize:none;"}),
        }


class CommentForm(forms.ModelForm):

    class Meta:

        model = Comment
        fields = ['content']
        labels = {'content': 'Текст комментария'}
        widgets = {
            'content': forms.Textarea(
                attrs={
                    'rows': 3,
                    'class': 'post bg-white',
                    'style': "height: 100%; width: 100%;border-radius: 20px; border: none; resize:none;"}),
        }
