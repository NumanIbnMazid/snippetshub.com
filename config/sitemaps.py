from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.contrib.auth import get_user_model


class StaticSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.8
    protocol = 'http'

    def items(self):
        return ['home']

    def location(self, item):
        return reverse(item)


class UserSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'http'

    def items(self):
        return get_user_model().objects.all()

    def lastmod(self, obj):
        return obj.updated_at

    # def location(self, obj):
    #     # default get_absolute_url()
    #     return '/user/%s' % (obj.slug)
