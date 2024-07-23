# forms.py
from django import forms
from .models import Album, Photo

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['name', 'description']

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['album', 'image', 'description']
