from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from upload.views import image_upload


site_title_header_display = f"{settings.SITE_DISPLAY_SETTINGS.get('PROJECT_NAME')} - {settings.SITE_DISPLAY_SETTINGS.get('ENVIRONMENT')}"


admin.site.site_header = site_title_header_display
admin.site.site_title = site_title_header_display


urlpatterns = [
    path("", include("common.urls")),
    path("", image_upload, name="upload"),
    path("admin/", admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls"))]
