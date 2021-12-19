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


# class YoutubeDownloaderView(FormView):
#     template_name = 'youtube/downloader.html'
#     form_class = YoutubeDownloaderForm
#     plus_context = dict()
    
#     def get_success_url(self):
#         return reverse('youtube:youtube_downloader')


#     def form_valid(self, form):
#         video_url = form.cleaned_data.get("url")
        
#         # validate if url is valid youtube url
#         regex = r'^(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/.+'
#         if not re.match(regex, video_url):
#             form.add_error(
#                 "url", forms.ValidationError(
#                     "Enter a valid youtube url!"
#                 )
#             )
#             return super().form_invalid(form)
        
        
#         ydl_opts = {}
#         with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#             meta = ydl.extract_info(video_url, download=False)
            
#         video_audio_streams = []
#         for m in meta['formats']:
#             file_size = m['filesize']
#             if file_size is not None:
#                 file_size = f'{filesizeformat(file_size)} mb'

#             resolution = 'Audio'
#             if m['height'] is not None:
#                 resolution = f"{m['height']}x{m['width']}"
#             video_audio_streams.append({
#                 'resolution': resolution,
#                 'extension': m['ext'],
#                 'file_size': file_size,
#                 'video_url': m['url']
#             })
#         video_audio_streams = video_audio_streams[::-1]
        
#         youtube_dl_context = {
#             'form': form,
#             'title': meta.get('title', None),
#             'streams': video_audio_streams,
#             'description': meta.get('description'),
#             'likes': f'{int(meta.get("like_count", 0)):,}',
#             'dislikes': f'{int(meta.get("dislike_count", 0)):,}',
#             'thumb': meta.get('thumbnails')[3]['url'],
#             'duration': round(int(meta.get('duration', 1))/60, 2),
#             'views': f'{int(meta.get("view_count")):,}'
#         }
        
#         self.plus_context.update(youtube_dl_context)
        
#         messages.add_message(
#             self.request, messages.SUCCESS, "Success!"
#         )
#         return super().form_valid(form)
    
#     def get_context_data(self, **kwargs):
#         context = super(YoutubeDownloaderView, self).get_context_data(**kwargs)
#         context['page_title'] = "Youtube Downloader"
#         context['meta_description'] = "Youtube Helper Services. Youtube Video Downloader, Youtube Audio Downloader, Youtube Downloader"
#         context['meta_keywords'] = "youtube video downloader, snippetshub"
#         context['additional_context'] = self.plus_context
#         return context


class YoutubeDownloaderView(View):
    form_class = YoutubeDownloaderForm
    
    def get_success_url(self):
        return reverse('youtube:youtube_downloader')
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, "youtube/downloader.html", context=context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        try:
            if self.request.method == "POST":
                youtube_url = request.POST.get("youtube_url")
                
                # validate if url is valid youtube url
                regex = r'^(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/.+'
                if not re.match(regex, youtube_url):
                    return JsonResponse({"message": "Invalid url!"}, status=400)
                
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

                youtube_dl_context = {
                    'title': meta.get('title', None),
                    'streams': video_audio_streams,
                    'description': meta.get('description'),
                    'likes': f'{int(meta.get("like_count", 0)):,}',
                    'dislikes': f'{int(meta.get("dislike_count", 0)):,}',
                    'thumb': meta.get('thumbnails')[3]['url'],
                    'duration': round(int(meta.get('duration', 1))/60, 2),
                    'views': f'{int(meta.get("view_count")):,}'
                }
                
                result = {
                    "data": youtube_dl_context
                }
                return JsonResponse(result, status=200)
                
        except Exception as e:
            print(f"*** Exception: {e} ***")
            return JsonResponse({"message": str(e)}, status=400)
        
        return render(request, "youtube/downloader.html", context=context)
        
    
    def get_context_data(self, **kwargs):
        context = {}
        context['page_title'] = "Youtube Downloader"
        context['meta_description'] = "Youtube Helper Services. Youtube Video Downloader, Youtube Audio Downloader, Youtube Downloader"
        context['meta_keywords'] = "youtube video downloader, snippetshub"
        context['form'] = YoutubeDownloaderForm
        return context
