from django.shortcuts import render, get_object_or_404

from django.shortcuts import render
from .models import *

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'webprog/post/list.html', {'posts': posts})

def post(request, year, month,day,post):
    post = get_object_or_404(Post,
                             slug=post,
                             created__year=year,
                             created__month=month,
                             created__day=day)
    return render(request,
                  'webprog/post/post.html',
                  {'post':post})