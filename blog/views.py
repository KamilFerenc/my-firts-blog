from django.shortcuts import render
from .models import Post
from django.utils import timezone


def post_list(requeste):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(requeste, 'blog/post_list.html', {'posts': posts})
