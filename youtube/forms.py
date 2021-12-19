from django import forms

class YoutubeDownloaderForm(forms.Form):
    youtube_url = forms.URLField(required=True)
