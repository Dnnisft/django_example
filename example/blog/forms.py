#encoding:utf-8 
from django.forms import ModelForm
from django import forms
from blog.models import Post

class NoticiaForm(ModelForm):
    class Meta:
        model = Post
