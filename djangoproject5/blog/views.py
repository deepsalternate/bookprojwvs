from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
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
    

class PostCreateView(CreateView):
    template_name = 'blog/post_create.html'
    model=Post
    fields=['title','body','author']


class PostUpdateView(UpdateView):
    template_name='blog/post_update.html'
    model=Post
    fields=['title','body','author']


class PostDeleteView(DeleteView):
    template_name='blog/post_delete.html'
    model=Post
    success_url='/'