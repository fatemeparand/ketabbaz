from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class SignupPageTest(TestCase):
    username = 'new user'
    email = 'new user@gmail.com'

    def test_signup_url(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_signup_form(self):
        user = get_user_model().objects.create_user(
            self.username,
            self.email,
        )

        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
