from django.forms import ModelForm
from django import forms
from .models import NewsPost, Comment


class EditorForm(ModelForm):
    class Meta:
        model = NewsPost
        fields = ['category', 'title', 'caption', 'image', 'details']
        widgets = {
            'category': forms.Select(attrs={"class": "form-control"}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'caption': forms.Textarea(attrs={'class': 'form-control'}),
            'details': forms.Textarea(attrs={'class': 'form-control'}),

        }


class UpdateForm(ModelForm):
    class Meta:
        model = NewsPost
        fields = ['category', 'title', 'caption', 'image', 'details']
        widgets = {
            'category': forms.Select(attrs={"class": "form-control"}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'cols':'5'}),
            'caption': forms.Textarea(attrs={'class': 'form-control', }),
            'details': forms.Textarea(attrs={'class': 'form-control'}),

        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
