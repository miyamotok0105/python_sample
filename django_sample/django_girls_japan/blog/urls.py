# coding: utf-8
#Djangoのメソッドと、blogアプリの全てのビューをインポート
from django.conf.urls import include, url
from django.urls import path
from . import views
#URLパターンを追加
#^$というパターンのURLをpost_listというビューに割り当てた
#^$は空文字
urlpatterns = [
    # url(r'^$', views.post_list, name='post_list'),
    path('', views.post_list, name='post_list'),
    # url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    path('post/<int:pk>', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    path('post_list_at_order/<int:order>', views.post_list_at_order, name='post_list_at_order'),
]
