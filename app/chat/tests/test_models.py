from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from chat import models

MESSAGES_URL = reverse('chat:chatmessage-list')


class ModelTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create_message_successful(self):
        """Create a test to successfully create a message"""
        params = {
            'author': 'TestAuthor',
            'email': 'test@gmail.com',
            'text': 'testtext22222'
        }

        chat_message = models.ChatMessage.objects.create(**params)

        self.assertEqual(chat_message.email, params['email'])

    def test_email_validation(self):
        """Test that email validation is working"""
        params = {
            'author': 'TestAuthor',
            'email': 'testsadassgmail.com',
            'text': 'testtext22222'
        }

        res = self.client.post(MESSAGES_URL, **params)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_text_blank(self):
        """Test that text validation is working"""
        params = {
            'author': 'TestAuthor',
            'email': 'test@gmail.com',
            'text': ''
        }

        res = self.client.post(MESSAGES_URL, **params)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_text_too_much_characters(self):
        """Test that text validation is working by providing >100 characters"""
        params = {
            'author': 'TestAuthor',
            'email': 'test@gmail.com',
            'text': 'ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss'
                    'ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss'
                    'ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss'
        }

        res = self.client.post(MESSAGES_URL, **params)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
