from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.utils import timezone
from django.views.generic import CreateView, UpdateView

from .forms import ImageForm
from .models import Image

from .forms import PostForm
from .models import Post


def image_list(request):
    image_list = Image.objects.order_by('created_date')
    print(image_list)
    return render(request, 'upload_image/image_list.html', {'image_list': image_list})

def image_detail(request, pk):
    image = get_object_or_404(Image, pk=pk)
    print(Image)
    return render(request, 'upload_image/image_detail.html', {'image': image})

def image_new(request):
    print("request", request)
    if request.method == "POST":
        print("post")
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            print("is valid")
            image = form.save(commit=False)
            image.save()
            return redirect(image_detail, pk=image.pk)
        else:
            print("not valid")
    else:
        print("get")
        form = ImageForm()
    return render(request, 'upload_image/image_edit.html', {'form': form})


# def image_new(request):
#     form = ImageForm(request.GET or None)
#     if form.is_valid():
#         message = 'データ検証に成功しました'
#     else:
#         message = 'データ検証に失敗しました'
#     # d = {
#     #     'form': form,
#     #     'message': message,
#     # }
#     return render(request, 'upload_image/image_edit.html', {'form': form})


#create viewを使用した方法
# class image_new(CreateView):
#     model = Image
#     form_class = ImageForm
#     template_name = "upload_image/image_edit.html"
#     sucuess_url = "/"


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'upload_image/post_detail.html', {'post': post})

def post_new(request):
    #formを使う時はpostとgetでview側で分けてあげる
    if request.method == "POST":
        form = PostForm(request.POST)
        #バリデーションチェック。
        if form.is_valid():
            post = form.save(commit=False)
            #modelにauthorがあるが、フォームにないのでこの処理が必須
            # post.author = request.user
            post.save()
            #詳細画面にリダイレクト
            return redirect(post_detail, pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'upload_image/post_edit.html', {'form': form})

