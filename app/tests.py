from django.test import TestCase

from .models import Todo

from rest_framework.test import APIClient


class TodoCreateTestCase(TestCase):

    def test_create_todo(self):
        """
        Test that a new todo can be created.
        """
        todo = Todo.objects.create(title="Test todo")
        self.assertEqual(todo.title, "Test todo")


class TodoUpdateTestCase(TestCase):

    def test_update_todo(self):
        """
        Test that a todo can be updated.
        """
        todo = Todo.objects.create(title="Test todo")
        todo.title = "Updated test todo"
        todo.save()
        self.assertEqual(todo.title, "Updated test todo")


class TodoDeleteTestCase(TestCase):

    def test_delete_todo(self):
        """
        Test that a todo can be deleted.
        """
        todo = Todo.objects.create(title="Test todo")
        todo.delete()
        self.assertEqual(Todo.objects.count(), 0)


class TodoListTestCase(TestCase):

    def test_todo_list(self):
        """
        Test that the todo list view returns all todos.
        """
        todo1 = Todo.objects.create(title="Test todo 1")
        todo2 = Todo.objects.create(title="Test todo 2")
        response = self.client.get('/todo/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, todo1.title)
        self.assertContains(response, todo2.title)


class TodoListAPITestCase(TestCase):

    def test_todo_list_api(self):
        """
        Test that the todo list API endpoint returns all todos.
        """
        todo1 = Todo.objects.create(title="Test todo 1")
        todo2 = Todo.objects.create(title="Test todo 2")
        client = APIClient()
        response = client.get('/api/todo/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['title'], todo1.title)
        self.assertEqual(response.data[1]['title'], todo2.title)


class TodoCreateAPITestCase(TestCase):

    def test_todo_create_api(self):
        """
        Test that the todo create API endpoint creates a new todo.
        """
        client = APIClient()
        data = {'title': 'Test todo'}
        response = client.post('/api/todo/create/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertEqual(Todo.objects.get().title, 'Test todo')


class TodoUpdateAPITestCase(TestCase):

    def test_todo_update_api(self):
        """
        Test that the todo update API endpoint updates a todo.
        """
        todo = Todo.objects.create(title="Test todo")
        client = APIClient()
        data = {'title': 'Updated test todo'}
        response = client.put('/api/todo/{}/update/'.format(todo.id), data, format='json')
        self.assertEqual(response.status_code, 200)
        todo.refresh_from_db()
        self.assertEqual(todo.title, 'Updated test todo')


class TodoDeleteAPITestCase(TestCase):

    def test_todo_delete_api(self):
        """
        Test that the todo delete API endpoint deletes a todo.
        """
        todo = Todo.objects.create(title="Test todo")
        client = APIClient()
        response = client.delete('/api/todo/{}/delete/'.format(todo.id))
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Todo.objects.count(), 0)