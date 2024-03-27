from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from todo.models import Todo


class TodoAPITestCase(TestCase):

    def setUp(self):
        Todo.objects.create(task="First task to do")
        Todo.objects.create(task="Second task to do")

    # Test method that gets all todos.
    def test_get_todos(self):
        url = reverse("api_todos")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("First task to do", str(response.content))
        self.assertIn("Second task to do", str(response.content))
        self.assertIn("Third task to do", str(response.content))

    # Test method that posts (adds) a single todo.
    def test_post_todo_valid(self):
        url = reverse("api_todos")
        data = {"task": "Fourth task to do"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Fourth task to do", str(response.content))

    # Test method that posts a single todo with an empty task.
    def test_post_todo_empty_invalid(self):
        url = reverse("api_todos")
        data = {"task": ""}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Please provide a task", str(response.content))

38     # TODO (experimental, need a review)
       # Test method to delete a single todo with its id.
39     def test_delete_todo_by_id(self):
40         # Create a todo to delete
41         create_url = reverse("api_todos")
42         data = {"task": "Task to delete"}
43         create_response = self.client.post(create_url, data, format="json")
44         todo_id = create_response.data['id']
45         
46         # Delete the created todo
47         delete_url = reverse("api_todo_detail", args=[todo_id])
48         delete_response = self.client.delete(delete_url, format="json")
49         self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)
50         
51         # Verify the todo is deleted
52         get_response = self.client.get(delete_url, format="json")
53         self.assertEqual(get_response.status_code, status.HTTP_404_NOT_FOUND)
