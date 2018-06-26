from django import forms

from .models import Image
from .models import Post

class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        # fields = ('image_path', 'created_date')
        fields = ('image_id', 'image_path', 'created_date', )
        # exclude = ('image_id', )
        widgets = {
            'created_date': forms.DateTimeInput(attrs={'class': 'datetime-input'}),
            # 'face_id':forms.HiddenInput(),
        }

# class ImageForm(forms.Form):
#     image_path = forms.FileField(required=True)

class PostForm(forms.ModelForm):

    #Metaクラスを作りどのモデルからこのフォームを作成するべきかを指定します(model = Post)
    class Meta:
        model = Post
        #どのフィールドをこのフォームで使用するかを指定
        fields = ('title', 'text','image_id', 'image_path', )
        
