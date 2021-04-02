from django.db import models
from .validators import validate_email, validate_text


# Create your models here.
class ChatMessage(models.Model):
    """Model for a chat message"""
    author = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, validators=[validate_email])
    text = models.TextField(validators=[validate_text])
    create_date = models.DateTimeField(auto_now_add=True, editable=False)
    updated_date = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f'{self.author} with email {self.email}'
