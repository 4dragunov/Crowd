from django.contrib import admin
from django.urls import path, include
from .views import redirect_crowd


urlpatterns = [
    path("auth/", include("users.urls")),
    path("auth/", include("django.contrib.auth.urls")),
    path('', redirect_crowd, name='main_url'),
    path('admin/', admin.site.urls),
    path('challenges/', include('challenge.urls'))

]
