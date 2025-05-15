from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Post, PostCategory
class PostListView(ListView):
    model = Post
    template_name = "post_page.html"

class PostDetailView(DetailView):
    model = Post
    template_name = "post.html"

def post_page(request):
    posts = Post.objects.all()
    ctx = { "posts": posts }
    return render(request, 'post_page.html', ctx)

def post(request, pk):
    ctx = { "post":Post.objects.get(pk=pk) }
    return render(request, 'post.html', ctx)
