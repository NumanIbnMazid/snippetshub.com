from django.conf import settings
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
import debug_toolbar
from .sitemaps import StaticSitemap, UserSitemap
from .end_user_views import HomePageView
from .admin_views import DashboardView


sitemaps = {
    'static': StaticSitemap,
    'user': UserSitemap,
}

THIRD_PARTY_URL_PATTERNS = [
    # Third Party URL Patterns
]

END_USER_URL_PATTERNS = [
    path('', HomePageView.as_view(), name='home'),
    # ==============================*** Youtube URLS ***==============================
    path("youtube/", include(("youtube.urls", "youtube"), namespace="youtube")),
]

ADMIN_URL_PATTERNS = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    # ==============================*** UTILS URLS ***==============================
    path("utils/", include(("utils.urls", "utils"), namespace="utils")),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
] + THIRD_PARTY_URL_PATTERNS + END_USER_URL_PATTERNS + ADMIN_URL_PATTERNS


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        # Django Debug Toolbar
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
