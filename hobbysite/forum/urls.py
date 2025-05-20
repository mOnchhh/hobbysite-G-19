from django.urls import path

from .views import (ThreadListView, ThreadDetailView, ThreadUpdateView, ThreadDeleteView, 
                    ThreadCreateView, ThreadGalleryView)

urlpatterns = [
    path('forum/threads', ThreadListView.as_view(), name='thread_page'),
    path('forum/thread/<int:pk>', ThreadDetailView.as_view(), name='thread'),
    path('forum/thread/<int:pk>/edit', ThreadUpdateView.as_view(), name='update'),
    path('forum/thread/add', ThreadCreateView.as_view(), name='create'),
    path('forum/thread/<int:pk>/delete', ThreadDeleteView.as_view(), name='delete'),
    path('forum/thread/gallery', ThreadGalleryView.as_view(), name='gallery'),
]

app_name = 'forum'