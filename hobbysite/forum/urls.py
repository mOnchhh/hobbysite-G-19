from django.urls import path

from .views import (ThreadListView, ThreadDetailView, ThreadUpdateView, ThreadDeleteView, 
                    ThreadCreateView, ThreadGalleryView)

urlpatterns = [
    path('wiki/articles', ThreadListView.as_view(), name='thread_page'),
    path('wiki/article/<int:pk>', ThreadDetailView.as_view(), name='thread'),
    path('wiki/article/<int:pk>/edit', ThreadUpdateView.as_view(), name='update'),
    path('wiki/article/add', ThreadCreateView.as_view(), name='create'),
    path('wiki/article/<int:pk>/delete', ThreadDeleteView.as_view(), name='delete'),
    path('wiki/article/gallery', ThreadGalleryView.as_view(), name='gallery'),
]

app_name = 'wiki'