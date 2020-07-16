from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import redirect_crowd


urlpatterns = [
    path('', redirect_crowd, name='main_url'),
    path('admin/', admin.site.urls),
    path('challenges/', include('challenge.urls'))

]
