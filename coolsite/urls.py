from cgitb import handler
from xml.dom.minidom import Document
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from coolsite import settings
from women.views import pageNotFound
from django.conf.urls.static import static

from .settings import MEDIA_ROOT


urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('', include('women.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound