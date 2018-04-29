from django import forms

from .models import Post

#PostモデルのformをPostFormにする。
#forms.ModelFormを継承する
class PostForm(forms.ModelForm):

    #Metaクラスを作りどのモデルからこのフォームを作成するべきかを指定します(model = Post)
    class Meta:
        model = Post
        #どのフィールドをこのフォームで使用するかを指定
        fields = ('title', 'text',)
