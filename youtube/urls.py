from django.urls import path
from .views import YoutubeDownloaderView


urlpatterns = [
    # Youtube Services URL Patterns
    path("downloader/", YoutubeDownloaderView.as_view(), name="youtube_downloader"),
]