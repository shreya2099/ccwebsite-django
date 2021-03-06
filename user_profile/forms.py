from django import forms
from django.contrib.auth.models import User
# from PIL import Image
from django.core.files import File

# Imported Models
from .models import UserProfile


class AvatarUploadForm(forms.ModelForm):
    # Form to upload profile picture
    class Meta:
        model = UserProfile
        fields = ('avatar',)


# Tried to crop image:
# class PhotoForm(forms.ModelForm):
#     x = forms.FloatField(widget=forms.HiddenInput())
#     y = forms.FloatField(widget=forms.HiddenInput())
#     width = forms.FloatField(widget=forms.HiddenInput())
#     height = forms.FloatField(widget=forms.HiddenInput())
#
#     class Meta:
#         model = UserProfile
#         fields = ('avatar', 'x', 'y', 'width', 'height', )
#
#     def save(self):
#         photo = super(PhotoForm, self).save()
#
#         x = self.cleaned_data.get('x')
#         y = self.cleaned_data.get('y')
#         w = self.cleaned_data.get('width')
#         h = self.cleaned_data.get('height')
#
#         image = Image.open(photo.avatar)
#         cropped_image = image.crop((x, y, w+x, h+y))
#         resized_image = cropped_image.resize((200, 200), Image.ANTIALIAS)
#         resized_image.save(photo.avatar.path)
#
#         return photo
