from django import forms
from .models import *


class ShortUrlForm(forms.ModelForm):

    class Meta:
        model = ShortUrl
        fields = ('id', 'url', 'short')
