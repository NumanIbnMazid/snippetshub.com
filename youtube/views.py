from django.shortcuts import render
from django.urls import reverse
from django.views.generic import View, CreateView
import re
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django import forms
from django.contrib import messages
from django.template.defaultfilters import filesizeformat
from django.views.generic.edit import FormView
from .forms import YoutubeDownloaderForm
# youtube_dl
import youtube_dl


class YoutubeDownloaderView(View):
    form_class = YoutubeDownloaderForm
    
    def get_success_url(self):
        return reverse('youtube:youtube_downloader')
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, "youtube/downloader.html", context=context)

    def post(self, request, *args, **kwargs):
        context = {}
        try:
            if self.request.method == "POST":
                youtube_url = request.POST.get("youtube_url")
                
                # validate if url is valid youtube url
                regex = r'^(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/.+'
                if not re.match(regex, youtube_url):
                    print("exception in youtube_url ***********")
                    return render(request, "snippets/handlers/response-error.html", context={"message": "Invalid URL!"})
                
                ydl_opts = {}
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    meta = ydl.extract_info(youtube_url, download=False)

                video_audio_streams = []
                for m in meta['formats']:
                    file_size = m['filesize']
                    if file_size is not None:
                        file_size = f'{filesizeformat(file_size)} mb'

                    resolution = 'Audio'
                    if m['height'] is not None:
                        resolution = f"{m['height']}x{m['width']}"
                    video_audio_streams.append({
                        'resolution': resolution,
                        'extension': m['ext'],
                        'file_size': file_size,
                        'video_url': m['url']
                    })
                video_audio_streams = video_audio_streams[::-1]

                context = {
                    'title': meta.get('title', None),
                    'streams': video_audio_streams,
                    'description': meta.get('description'),
                    'likes': f'{int(meta.get("like_count", 0)):,}',
                    'dislikes': f'{int(meta.get("dislike_count", 0)):,}',
                    'thumb': meta.get('thumbnails')[3]['url'],
                    'duration': round(int(meta.get('duration', 1))/60, 2),
                    'views': f'{int(meta.get("view_count")):,}'
                }
                return render(request, "youtube/response-data.html", context=context)
        except Exception as e:
            print(f"*** Exception: {e} ***")
        
        return render(request, "snippets/handlers/response-error.html", context={"message": f"Something went wrong! {str(e)}"})
        
    
    def get_context_data(self, **kwargs):
        context = {}
        context['page_title'] = "Youtube Downloader"
        context['meta_description'] = "Youtube Helper Services. Youtube Video Downloader, Youtube Audio Downloader, Youtube Downloader"
        context['meta_keywords'] = "youtube video downloader, snippetshub"
        context['form'] = YoutubeDownloaderForm
        return context
