from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from todo.models import Todo


class TodoAPITestCase(TestCase):

    def setUp(self):
        Todo.objects.create(task="First task to do")
        Todo.objects.create(task="Second task to do")

    def test_get_todos(self):
        url = reverse('api_todos')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('First task', str(response.content))
        self.assertIn('Second task', str(response.content))

    def test_post_todo_valid(self):
        url = reverse('api_todos')
        data = {'task': 'Third task to do'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Third task', str(response.content))

    def test_post_todo_invalid(self):
        url = reverse('api_todos')
        data = {'task': ''}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Please provide a task', str(response.content))
