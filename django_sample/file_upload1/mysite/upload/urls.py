# from django.conf.urls import include, url
# from django.conf import settings
# from django.conf.urls.static import static
# from django.views.generic import RedirectView

# from django.contrib import admin

# urlpatterns = [
#     url(r'^upload/', include('upload.urls')),
#     url(r'^$', RedirectView.as_view(url='/upload/list/', permanent=True)),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.urls import path
from .views import list

urlpatterns = [
    url(r'^list/$', list, name='list')
]

