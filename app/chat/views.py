from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.pagination import PageNumberPagination
from . import serializers
from . import models


# Create your views here.


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class MessageListViewSet(viewsets.GenericViewSet, ListModelMixin, CreateModelMixin):
    """Class to display list and add messages"""
    serializer_class = serializers.ChatMessageSerializer
    queryset = models.ChatMessage.objects.all()
    pagination_class = StandardResultsSetPagination


class SingleMessageViewSet(viewsets.GenericViewSet, RetrieveModelMixin, UpdateModelMixin):
    """Class to display and update a single message"""
    serializer_class = serializers.ChatMessageSerializer
    queryset = models.ChatMessage.objects.all()
