from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Item

class ItemListTests(APITestCase):
    def setUp(self):
        Item.objects.create(name='Item 1', description='Description 1')
        Item.objects.create(name='Item 2', description='Description 2')

    def test_get_items(self):
        response = self.client.get('/api/items/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.assertIn('application/json', response['Content-Type'])

        self.assertIsInstance(response.json(), list)
        self.assertEqual(len(response.json()), 2)
