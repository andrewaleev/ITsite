from django.shortcuts import render, get_object_or_404
from .forms import CommentForm
from django.shortcuts import render
from .models import *
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    posts = Post.objects.all().filter(author=request.user)

    return render(request,
    'webprog/dashboard.html',
    {'section': 'dashboard',
     'posts':posts})
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'webprog/post/list.html', {'section':'list','posts': posts})


def post(request, year, month, day, post):
    post = get_object_or_404(Post,
                             slug=post,
                             created__year=year,
                             created__month=month,
                             created__day=day)
    # Список активных комментариев к этому посту
    comments = post.comments.filter(active=True)
    # Форма для комментирования пользователям
    form = CommentForm()
    return render(request,
                  'webprog/post/post.html',
                  {'post': post,
                   'comments': comments,
                   'form': form})



@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post,
                             id=post_id)
    comment = None
    # Комментарий был отправлен


    form = CommentForm(data=request.POST)
    if form.is_valid():
        # Создать объект класса Comment, не сохраняя его в базе данных
        comment = form.save(commit=False)
        # Назначить пост комментарию
        comment.post = post
        comment.author = request.user
        # Сохранить комментарий в базе данных
        comment.save()
        return render(request, 'webprog/post/comment.html',
              {'post': post,
               'form': form,
               'comment': comment})
