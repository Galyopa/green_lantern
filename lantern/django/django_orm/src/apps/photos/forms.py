from django.forms import ModelForm
from django import forms
from apps.photos.models import Photo


class PhotosForm(ModelForm):
    class Meta:
        model = Photo
        fields = "__all__"
        widgets = {
            'image': forms.ClearableFileInput(attrs={'multiple': True}),
        }
