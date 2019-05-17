from django import forms

from .models import Post, Artes, Usuario

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class PostForm(forms.ModelForm):

    class Meta:
        model = Artes
        fields = ('titulo', 'descricao',)

class PostForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ('nome',)