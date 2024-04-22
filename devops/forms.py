

from django import forms
from .models import PostIt

class PostItForm(forms.ModelForm):
    class Meta:
        model = PostIt
        fields = ['name', 'subject', 'details']
