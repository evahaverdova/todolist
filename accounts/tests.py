from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='testuser@example.com',
            password='testpass',
            username='testuser'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.email, 'testuser@example.com')
        self.assertTrue(self.user.check_password('testpass'))
        self.assertEqual(self.user.username, 'testuser')

    def test_user_str(self):
        self.assertEqual(str(self.user), 'testuser@example.com')
from django.test import TestCase

# Create your tests here.
