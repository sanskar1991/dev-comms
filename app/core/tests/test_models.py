from django.test import TestCase
from django.contrib.auth import get_user_model


class UserModelTests(TestCase):
    """Testing the user model"""

    def test_user_model(self):
        """Check if user is created by email or not"""
        email = "test@root.com"
        password = "test@root"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
            )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Checks if the user's email is normalized or not"""
        email = 'test@ROOT.com'
        password = 'rest@root'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
            )

        self.assertEqual(user.email, email.lower())

    def test_valid_user_email(self):
        """Checks if the user has an email or not"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test@root')

    def test_is_superuser(self):
        """Checks for creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'admin@root.com',
            'admin@root'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
