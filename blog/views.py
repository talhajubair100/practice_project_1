from django.shortcuts import render
from .models import Category, Post

# Create your views here.

def detail_post(request, id):
    post_obj = Post.objects.get(id=id)
    context = {'post': post_obj}
    return render(request, 'blog/detail_post.html', context)