from django import forms
from utils.mixins import CustomSimpleForm


class YoutubeDownloaderForm(CustomSimpleForm):
    url = forms.URLField(required=True)
