from django.contrib import admin

from .models import ArticleCategory, Article

class ArticleInline(admin.StackedInline):
    model = Article

class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleInline]

admin.site.register(ArticleCategory, ArticleAdmin)
admin.site.register(Article)
