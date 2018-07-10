from django.conf.urls import url
from django.contrib import admin

from boards import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home2/', views.home2, name='home2'),
    url(r'^home3/', views.home3, name='home3'),
    url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    url(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    url(r'^boards2/(?P<pk>\d+)/$', views.board_topics2, name='board_topics2'),
    url(r'^admin/', admin.site.urls),
]
