from django.db import models


class Blog(models.Model):
    """
    this is a model for this Blog app
    """
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
