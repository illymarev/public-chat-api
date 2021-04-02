from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from chat import models

CHAT_MESSAGES_URL = reverse('chat:chatmessage-list')


def detail_url(message_id):
    """Return message detail url"""
    return reverse('chat:chatmessage-detail', args=[message_id])


class ChatMessagesTests(TestCase):
    """Tests for chat messages API"""

    def setUp(self):
        self.client = APIClient()

    def test_retrieving_single_message(self):
        """Test that /single/ option is working"""
        params = {
            'author': 'TestAuthor',
            'email': 'test@gmail.com',
            'text': 'testtext22222'
        }

        message = models.ChatMessage.objects.create(**params)
        url = detail_url(message.id)

        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_retrieving_list_of_messages(self):
        """Test that we can return a list of messages"""
        params = {
            'author': 'TestAuthor',
            'email': 'test@gmail.com',
            'text': 'testtext22222'
        }

        models.ChatMessage.objects.create(**params)
        models.ChatMessage.objects.create(**params)
        models.ChatMessage.objects.create(**params)

        res = self.client.get(CHAT_MESSAGES_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['count'], 3)
