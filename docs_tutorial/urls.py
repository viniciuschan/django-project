from django.conf.urls import url, include
from django.contrib import admin

from intro import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('intro.urls')),
]
