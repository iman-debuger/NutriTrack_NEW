from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tracker.urls')),
    # Favicon
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('tracker/favicon.ico'))),
]

# Serve static files in production (WhiteNoise handles this, but this is a fallback)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)