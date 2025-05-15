from django.db import models
from django.urls import reverse

class PostCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return '{}'.format(self.name)
    
class Post(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        PostCategory,
        on_delete=models.SET_NULL,
        related_name = "post",
        null=True
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
        return reverse('forum:post', args=[str(self.pk)])