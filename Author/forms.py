from django import forms
from Author.models import Post


class PostForms(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('Title', 'Genre', 'Description', 'Poster')
