from django import forms
from django.test import TestCase

from .forms import AddTweetForm


class FormImportTests(TestCase):
    def test_add_tweet_form_is_available(self):
        self.assertTrue(issubclass(AddTweetForm, forms.ModelForm))
