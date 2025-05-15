from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Article, ArticleCategory

class ArticleListView(ListView):
    model = Article
    template_name = "article_page.html"

class ArticleDetailView(DetailView):
    model = Article
    template_name = "article.html"

def article_page(request):
    articles = Article.objects.all()
    ctx = { "articles": articles }
    return render(request, 'article_page.html', ctx)

def article(request, pk):
    ctx = { "article":Article.objects.get(pk=pk) }
    return render(request, 'article.html', ctx)
