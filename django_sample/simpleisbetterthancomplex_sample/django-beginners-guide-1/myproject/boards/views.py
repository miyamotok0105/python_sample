from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import Board, Topic, Post, Sample1
from .models import Board

def home(request):
    boards = Board.objects.all()
    boards_names = list()
    for board in boards:
        boards_names.append(board.name)
    response_html = '<br>'.join(boards_names)
    return HttpResponse(response_html)

def home2(request):
    boards = Board.objects.all()
    return render(request, 'home2.html', {'boards': boards})

def home3(request):
    boards = Board.objects.all()
    return render(request, 'home3.html', {'boards': boards})

def board_topics(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404
    return render(request, 'topics.html', {'board': board})

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        user = User.objects.first()  # TODO: get the currently logged in user
        topic = Topic.objects.create(
            subject=subject,
            board=board,
            starter=user
        )
        post = Post.objects.create(
            message=message,
            topic=topic,
            created_by=user
        )
        return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
    return render(request, 'new_topic.html', {'board': board})

def board_topics2(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})

def sample1(request):
    sample1_all = Sample1.objects.all()
    return render(request, 'sample1.html', {'sample1_all': sample1_all})

def new_sample1(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        sample1 = Sample1.objects.create(
            name=name,
            description=description
        )
        return redirect('sample1')
    return render(request, 'new_sample1.html')



