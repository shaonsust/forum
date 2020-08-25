from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User

from ..forms import NewTopicForm
from ..views import home, board_topics, new_topic
from ..models import Board, Topic, Post


class HomeTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Write only about django here.')
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEqual(view.func, home)

    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url = reverse('board_topics', kwargs={'board_id': self.board.id})
        self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))


class BoardTopicsTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='You can write anything about django in here.')

    def test_board_topics_view_success_status_code(self):
        url = reverse('board_topics', kwargs={'board_id': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_board_topics_view_not_found_status_code(self):
        url = reverse('board_topics', kwargs={'board_id': 100})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/board_topics/1')
        self.assertEqual(view.func, board_topics)

    def test_board_topics_view_contain_navigation_links(self):
        home_page_url = reverse('home')
        new_topic_url = reverse('new_topic', kwargs={'board_id': self.board.id})
        board_topics_url = reverse('board_topics', kwargs={'board_id': self.board.id})

        response = self.client.get(board_topics_url)

        self.assertContains(response, 'href="{0}"'.format(home_page_url))
        self.assertContains(response, 'href="{0}"'.format(new_topic_url))


class NewTopicTests(TestCase):
    def setUp(self) -> None:
        self.board = Board.objects.create(name="Django", description="All about django")
        User.objects.create_user(username='shaon', email='shaon@admin.com', password='123456')

    def test_new_topic_view_success_status_code(self):
        url = reverse('board_topics', kwargs={'board_id': self.board.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_new_topic_view_not_found_status_code(self):
        url = reverse('board_topics', kwargs={'board_id': 100})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_new_topic_url_resolves_new_topic_view(self):
        view = resolve('/boards/new_topic/1')
        self.assertEqual(view.func, new_topic)

    def test_new_topic_view_contain_link_back_to_board_topics_view(self):
        new_topic_url = reverse('new_topic', kwargs={'board_id': self.board.id})
        board_topics_url = reverse('board_topics', kwargs={'board_id': self.board.id})
        response = self.client.get(new_topic_url)
        self.assertContains(response, 'href="{0}"'.format(board_topics_url))

    def test_csrf_token(self):
        url = reverse('new_topic', kwargs={'board_id': self.board.id})
        response = self.client.get(url)
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_new_topic_valid_post_data(self):
        url = reverse('new_topic', kwargs={'board_id': self.board.id})
        data = {
            'subject': "Django topic 1",
            'message': "This is test case 1 for topic 1."
        }

        response = self.client.post(url, data)
        self.assertTrue(Topic.objects.exists())
        self.assertTrue(Post.objects.exists())

    def test_new_topic_invalid_post_data(self):
        """
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        """
        url = reverse('new_topic', kwargs={'board_id': self.board.id})
        response = self.client.post(url, {})
        form = response.context.get('form')

        self.assertEqual(response.status_code, 200)
        self.assertTrue(form.errors)

    def test_new_topic_invalid_post_data_empty_field(self):
        """
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        """
        url = reverse('new_topic', kwargs={'board_id': self.board.id})
        data = {
            'subject': "",
            'message': ""
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Topic.objects.exists())
        self.assertFalse(Post.objects.exists())

    def test_new_topic_form(self):
        url = reverse('new_topic', kwargs={'board_id': self.board.id})
        response = self.client.get(url)
        form = response.context.get('form')
        self.assertIsInstance(form, NewTopicForm)