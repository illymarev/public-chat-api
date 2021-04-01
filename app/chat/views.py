from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from . import serializers
from . import models
# Create your views here.


class ChatMessageViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ChatMessageSerializer
    queryset = models.ChatMessage.objects.all()