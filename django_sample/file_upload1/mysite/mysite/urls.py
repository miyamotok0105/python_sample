
# from django.contrib import admin
# from django.urls import path
# from django.conf.urls import include, url

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     url(r'', include('upload.urls')),
# ]


from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.urls import path

from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^upload/', include('upload.urls')),
    url(r'^$', RedirectView.as_view(url='/upload/list/', permanent=True)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


