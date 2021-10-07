from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """
        """
        email = "ketul@gmail.com"
        password = "1234"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ test the email is normalized
        """
        email = 'ketul@GMAIL.COM'
        user = get_user_model().objects.create_user(email, '1234')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalids_email(self):
        """ Test creating user with no email raise error
        """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '1234')

    def test_create_new_superuser(self):
        """ test creating new super user
        """
        user = get_user_model().objects.create_superuser(
            'k2l@gmail.com',
            '1234'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
