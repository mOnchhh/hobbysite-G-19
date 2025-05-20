from django.contrib import admin

from .models import ThreadCategory, Thread, Comment

class ThreadInline(admin.StackedInline):
    model = Thread

class ThreadAdmin(admin.ModelAdmin):
    inlines = [ThreadInline]

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'thread', 'created_on')
    list_filter = ('created_on',)
    search_fields = ['author_username', 'thread_title']

admin.site.register(ThreadCategory, ThreadAdmin)
admin.site.register(Thread)
admin.site.register(Comment, CommentAdmin)