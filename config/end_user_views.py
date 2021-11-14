from django.views.generic import View, TemplateView
from django.shortcuts import render
from django.contrib import messages

# # -------------------------------------------------------------------
# #                           Home Page
# # -------------------------------------------------------------------

# class HomePageView(TemplateView):
#     template_name = 'user_panel/pages/index.html'
    
#     def get_context_data(self, **kwargs):
#         context = super(HomePageView, self).get_context_data(**kwargs)
#         context['meta_description'] = "snippetshub.com: A sophisticated web application containing a number of useful snippets. Services we provide like youtube video downloader, video converter, pdf converter, doc file converter, powerpoint file converter, image/video compressor, file resizer, fake data api and so on."
#         context['meta_keywords'] = "youtube video downloader, file converter, image converter, file resizer, image resizer, fake data, fake api, free api, file compressor, video downloader, python, django, seo, youtube, facebook, facebook video downloader, web snippets, snippetshub"
#         context["meta_author"] = "Numan Ibn Mazid"
#         return context

class HomePageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "user_panel/pages/index.html")
    
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['meta_description'] = "snippetshub.com: A sophisticated web application containing a number of useful snippets. Services we provide like youtube video downloader, video converter, pdf converter, doc file converter, powerpoint file converter, image/video compressor, file resizer, fake data api and so on."
        context['meta_keywords'] = "youtube video downloader, file converter, image converter, file resizer, image resizer, fake data, fake api, free api, file compressor, video downloader, python, django, seo, youtube, facebook, facebook video downloader, web snippets, snippetshub"
        context["meta_author"] = "Numan Ibn Mazid"
        return context