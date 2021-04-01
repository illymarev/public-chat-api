from django.test import TestCase
from chat import models


class ModelTests(TestCase):

    def test_create_message_successful(self):
        """Create a test to successfully create a message"""
        params = {
            'author': 'TestAuthor',
            'email': 'test@gmail.com',
            'text': 'testtext22222'
        }

        chat_message = models.ChatMessage.objects.create(**params)

        self.assertEqual(chat_message.email, params['email'])


