from django.db import models
from django.urls import reverse
from datetime import datetime
from django.conf import settings

class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return '{}'.format(self.name)
    
class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
    )
    category = models.ForeignKey(
        ArticleCategory,
        on_delete=models.SET_NULL,
        related_name = "article",
        null=True
    )
    entry = models.TextField()
    header_image = models.ImageField(
        upload_to='media/images/',
        null=True,
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
        null=True
    )
    updated_on = models.DateTimeField(
        auto_now=True,
        null=True
    )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.title} - {self.entry}"
    
    def get_absolute_url(self):
        return reverse('wiki:article', args=[str(self.pk)])
    
    def get_create_url(self):
        return reverse('wiki:create', args=[str(self.pk)])
    
    def get_update_url(self):
        return reverse('wiki:update', args=[str(self.pk)])
    
    def get_delete_url(self):
        return reverse('wiki:delete', args=[str(self.pk)])
    
class Comment(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='wiki_comment'
    )
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        null=True,
        related_name='wiki_comment'
    )
    entry = models.TextField()
    created_on = models.DateTimeField(
        auto_now_add=True,
        null=True
    )
    updated_on = models.DateTimeField(
        auto_now=True,
        null=True
    )

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"{self.article.title} - {self.content}"
