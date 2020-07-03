from django.shortcuts import render
from .models import Category, Post

# Create your views here.

def detail_post(request, id):
    post_obj = Post.objects.get(id=id)
    context = {'post': post_obj}
    return render(request, 'blog/detail_post.html', context)


def category_by_list(request, ctg_name):
    ctg_obj = Category.objects.get(name=ctg_name)
    post_list = Post.objects.filter(category=ctg_obj)
    context = {'posts': post_list, 'category_name': ctg_name}
    return render(request, 'blog/post_by_category.html', context)