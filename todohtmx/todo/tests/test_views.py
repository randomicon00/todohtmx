from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from todo.models import Todo


class TodoAPITestCase(TestCase):

    def setUp(self):
        self.todo1 = Todo.objects.create(task="First task to do")
        self.todo2 = Todo.objects.create(task="Second task to do")
        self.todo_url = reverse("api_todos")

    def assertTaskInResponse(self, task, response_content):
        """Helper method to check if a task is in the response content."""
        self.assertIn(task, str(response_content))

    def test_get_todos(self):
        """Test that GET request returns all todos."""
        response = self.client.get(self.todo_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTaskInResponse(self.todo1.task, response.content)
        self.assertTaskInResponse(self.todo2.task, response.content)

    def test_post_todo_valid(self):
        """Test that a valid POST request creates a new todo."""
        data = {"task": "Fourth task to do"}
        response = self.client.post(self.todo_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTaskInResponse("Fourth task to do", response.content)

    def test_post_todo_empty_invalid(self):
        """Test that a POST request with an empty task is invalid."""
        data = {"task": ""}
        response = self.client.post(self.todo_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Please provide a task", str(response.content))

    def test_delete_todo_by_id(self):
        """Test that a DELETE request deletes a todo by its ID."""
        data = {"task": "Task to delete"}
        create_response = self.client.post(self.todo_url, data, format="json")
        todo_id = create_response.data["id"]

        delete_url = reverse("api_todo_detail", args=[todo_id])
        delete_response = self.client.delete(delete_url, format="json")
        self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)

        get_response = self.client.get(delete_url, format="json")
        self.assertEqual(get_response.status_code, status.HTTP_404_NOT_FOUND)
