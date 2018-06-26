#Djangoのメソッドと、アプリの全てのビューをインポート
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

#URLパターンを追加
#^$というパターンのURLをpost_listというビューに割り当てた
#^$は空文字
urlpatterns = [
    url(r'^$', views.image_list, name='image_list'),
    #form for image
    path('image_detail/<int:pk>', views.image_detail, name='image_detail'),
    url(r'^image/new/$', views.image_new, name='image_new'),
    #create viewを使った場合
    # url(r'^image/new/$', views.image_new.as_view(), name='image_new'),
    #post入れてみる
    path('post/<int:pk>', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

