from django import forms
from .models import Tweet


class AddTweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'class': 'form-control'})
        }


class AddTweetModelForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'class': 'form-control'})
        }