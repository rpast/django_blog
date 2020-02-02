from django import forms
from myblog.models import Post, Comment
from django.db import models


class PostForm(forms.ModelForm):

    class Meta():
        model = Post

        fields = (
            'author',
            'title',
            'text'
        )

        # This dict links fields to widgets and define class names for css styling
        widgets = {
            'title': forms.TextInput(attrs={'class': 'editable textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }


class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = (
            'author',
            'text',
        )

        # This dict links fields to widgets and define class names for css styling
        widget = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }