from rest_framework import serializers
from .models import ChatMessage


class ChatMessageSerializer(serializers.ModelSerializer):
    """Serializing the ChatMessageSerializer"""

    class Meta:
        model = ChatMessage
        fields = ('author', 'email', 'text')
