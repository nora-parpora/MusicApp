from django import forms
from django.core.validators import MinValueValidator

from Music_App_v2.main_app.models import Profile, Album
from Music_App_v2.main_app.validators import validate_age_has_only_positive_integers


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age', )

        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username'
                }),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Email'}),
            'age': forms.TextInput(

                attrs={
                    'placeholder': 'Age'
                }),
        }




class AddAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('album_name', 'artist', 'genre', 'description', 'image_url', 'price',)

        widgets = {
            'album_name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name'}),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist'}),
            # 'genre': forms.TextInput(
            #     attrs={
            #         'placeholder': 'Genre'}),
            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Description'}),
            'image_url': forms.TextInput(
                attrs={
                    'placeholder': 'Image URL'}),
            'price': forms.TextInput(
                attrs={
                    'placeholder': 'Price'}),
        }


class EditAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'


class DeleteAlbumForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for v in self.fields.values():
            v.disabled = True

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Album
        fields = '__all__'


class DeleteProfileForm(forms.ModelForm):

    def save(self, commit=True):
        Album.objects.all().delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()

