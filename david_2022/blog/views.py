from django.shortcuts import render
from .models import Post, Comment


def blog_index(request):
    posts = Post.objects.all()
    context = {
        "posts": posts.order_by("created_on")
    }
    return render(request, "blog_index.html", context)


def blog_detail(request):
    comments = Comment.objects.all()
    context = {
        "comments": comments.order_by("created_on")
    }
    return render(request, "blog_detail.html", context)
