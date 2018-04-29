from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

def post_list(request):
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_list_at_order(request, order):
    #orderの場所から20post表示する
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[order:20]
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

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
    return render(request, 'blog/post_edit.html', {'form': form})
