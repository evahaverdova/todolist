from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Task, TaskStatus

class TaskModelTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='testuser@example.com',
            password='testpass',
            username='testuser'
        )
        self.status = TaskStatus.objects.create(name='Pending', user=self.user)
        self.task = Task.objects.create(
            title='Test Task',
            description='This is a test task.',
            user=self.user
        )
        self.task.status.add(self.status)

    def test_task_creation(self):
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.description, 'This is a test task.')
        self.assertEqual(self.task.user.email, 'testuser@example.com')
        self.assertIn(self.status, self.task.status.all())

    def test_task_str(self):
        self.assertEqual(str(self.task), 'Test Task')

    def test_status_creation(self):
        self.assertEqual(self.status.name, 'Pending')
        self.assertEqual(self.status.user.email, 'testuser@example.com')

    def test_status_str(self):
        self.assertEqual(str(self.status), 'Pending')
from django.test import TestCase

# Create your tests here.
