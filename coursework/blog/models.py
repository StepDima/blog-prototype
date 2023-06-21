from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True, verbose_name="Текст статті", null=False)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Час створення")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Час редагування")

    class Meta:
        verbose_name = 'Пости'
        verbose_name_plural = 'Пости'
        ordering = ['-time_create']


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, verbose_name="Пост")
    related_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL,
                                        verbose_name="Пов'язаний коментар")
    content = models.TextField(blank=True, verbose_name="Текст коментаря", null=False)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Час створення")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Час редагування")

    class Meta:
        verbose_name = 'Коментарі'
        verbose_name_plural = 'Коментарі'
        ordering = ['time_create']