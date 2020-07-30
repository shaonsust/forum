from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import resolve, reverse

from ..views import signup
from ..forms import SignUpForm


class SignupTest(TestCase):
    def setUp(self) -> None:
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_status_code(self) -> None:
        self.assertEqual(self.response.status_code, 200)

    def test_signup_url_resolves_signup_view(self) -> None:
        view = resolve('/signup/')
        self.assertEqual(view.func, signup)

    def test_csrf(self) -> None:
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self) -> None:
        form = self.response.context.get('form')
        self.assertIsInstance(form, SignUpForm)

    def test_signup_form_inputs(self):
        """
        The view must contain five inputs: csrf, username,
        email, password1, password2
        """
        self.assertContains(self.response, '<input', 5)
        self.assertContains(self.response, 'type="text"', 1)
        self.assertContains(self.response, 'type="email"', 1)
        self.assertContains(self.response, 'type="password"', 2)


class SuccessfulSignupTestCase(TestCase):
    def setUp(self) -> None:
        url = reverse('signup')
        data = {
            'username': 'zunaid',
            'email': 'zunaid@admin.com',
            'password1': 'asdfgh63',
            'password2': 'asdfgh63'
        }

        self.response = self.client.post(url, data)
        self.home_url = reverse('home')

    def test_redirection(self) -> None:
        """
        A valid submission should return user to the home page.
        """
        self.assertRedirects(self.response, self.home_url)

    def test_user_creation(self) -> None:
        self.assertTrue(User.objects.exists())

    def test_user_authentication(self) -> None:
        """
        Create a new request to an arbitrary page.
        The resulting response should now have a `user` to its context,
        after a successful sign up.
        """
        response = self.client.get(self.home_url)
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)


class InvalidSignupTest(TestCase):
    def setUp(self) -> None:
        url = reverse('signup')
        self.response = self.client.post(url, {})

    def test_signup_status_code(self):
        """
        An invalid form submission should return to the same page.
        """
        self.assertEqual(self.response.status_code, 200)

    def test_failed_user_creation(self):
        self.assertFalse(User.objects.exists())

    def test_form_error(self):
        form = self.response.context.get('form')
        self.assertTrue(form.errors)
