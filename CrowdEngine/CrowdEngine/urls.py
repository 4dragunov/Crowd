from django.contrib import admin
from django.urls import path, include
from .views import redirect_crowd
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path("auth/", include("users.urls")),
    path("auth/", include("django.contrib.auth.urls")),
    path('', redirect_crowd, name='main_url'),
    path('admin/', admin.site.urls),
    path('challenges/', include('challenge.urls')),
    path('about/', about_us, name="about"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
