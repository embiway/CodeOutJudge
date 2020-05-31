from django.db import models
from django import forms
from Problems.models import Blogs , Comments

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = [
            'title',
            'content',
        ]

        widgets = {
            'title' : forms.TextInput(
                attrs = {
                    'class' : 'form-control'
                }
            ),
            'content' : forms.Textarea(
                attrs = {
                    'class' : 'form-control'
                }
            ),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments

        labels = {
            'content' : 'Write Comment'
        }
        fields = [
            'content'
        ]

        widgets = {
            'content' : forms.Textarea(
                attrs = {
                    'class' : 'form-control'
                }
            )
        }