from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import DeleteView, CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from .models import Thread, ThreadCategory, Comment
from .forms import ThreadForm, CommentForm 

class ThreadListView(ListView):
    model = Thread
    template_name = "thread_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['selected_category'] = int(self.request.GET.get('category', 0))
        context['is_main'] = True
        context['category'] = Thread.objects.all()
        context['form'] = ThreadForm()

        return context
    
    def post(self, request, *args, **kwargs):
        if 'reset' in request.GET:
            return self.get(request, *args, **kwargs, selected_category=0)
        else:
            threads = Thread()
            threads.title = request.POST['thread_title']
            threads.author = request.user
            threads.entry = request.POST.get('thread_entry')
            threads.category = ThreadCategory.objects.get(pk=request.POST['category'])
            threads.header_image = request.POST.get('image')
            threads.save()

            return self.get(request, *args, **kwargs)

class ThreadDetailView(DetailView):
    model = Thread
    template_name = "thread.html"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['is_main'] = False
        context['comment'] = Comment.objects.all()
        context['form'] = CommentForm()

        return context
    
    def post(self, request, *args, **kwargs):
        comments = Comment()
        comments.author = request.user
        comments.entry = request.POST.get('entry')
        comments.article = self.get_object()
        comments.save()

        return self.get(request, *args, **kwargs)

class ThreadCreateView(CreateView):
    model = Thread
    form_class = ThreadForm
    template_name = 'thread_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['selected_category'] = int(self.request.GET.get('category', 0))
        context['is_main'] = False
        context['category'] = ThreadCategory.objects.all()
        context['form'] = ThreadForm()
        return context
    
    def post(self, request, *args, **kwargs):
        if 'reset' in request.GET:
            return self.get(request, *args, **kwargs, selected_category=0)
        
        else:
            threads = Thread()
            threads.title = request.POST['thread_title']
            threads.author = request.user
            threads.entry = request.POST.get('thread_entry')
            threads.category = ThreadCategory.objects.get(pk=request.POST.get('category'))
            threads.image = request.POST.get('image')
            threads.save()

            return self.get(request, *args, **kwargs)
        
class ThreadUpdateView(UpdateView):
    model = Thread
    form_class = ThreadForm
    template_name = 'thread_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_main'] = False

        return context
    
class ThreadDeleteView(DeleteView):
    model = Thread

    def get_success_url(self):
        return reverse_lazy('forum:thread_page')

class ThreadGalleryView(ListView):
    model = Thread
    form_class = ThreadForm
    template_name = 'thread_gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_main'] = False
        context['threads'] = Thread.objects.all()

        return context