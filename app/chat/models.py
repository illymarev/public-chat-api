from django.db import models
from .validators import validate_email


# Create your models here.
class ChatMessage(models.Model):
    """Model for a chat message"""
    author = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    text = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
