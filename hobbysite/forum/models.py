from django.db import models
from django.urls import reverse
from django.conf import settings

from accounts.models import Profile

class ThreadCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return '{}'.format(self.name)
    
class Thread(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True
    )
    category = models.ForeignKey(
        ThreadCategory,
        on_delete=models.SET_NULL,
        related_name = "thread",
        null=True
    )
    entry = models.TextField()
    image = models.ImageField(
        upload_to='media/images/',
        null=True,
        blank=True,
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
        null=True
    )
    updated_on = models.DateTimeField(
        auto_now=True,
        null=True
    )

    def __str__(self):
        return '{}'.format(self.name)

class Comment(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='forum_comment'
    )
    thread = models.ForeignKey(
        Thread,
        on_delete=models.CASCADE,
        null=True,
        related_name='forum_comment'
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
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.title} - {self.entry}"
    
    def get_absolute_url(self):
        return reverse('forum:thread', args=[str(self.pk)])