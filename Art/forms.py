from django import forms

from .models import Post, Artes, Usuario

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class ArteForm(forms.ModelForm):

    class Meta:
        model = Artes
        fields = ('titulo', 'descricao', 'imagem')

class UserForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ('nome',)