from django.shortcuts import render
from django.views.generic import ListView,DetailView
from.models import Post
# Create your views here.

class PostListView(ListView):
    template_name = 'blog/post_list.html'
    model=Post
    context_object_name='posts'

class PostDetailView(DetailView,):
    template_name = 'blog/post_detail.html'
    model=Post
    context_object_name='post'