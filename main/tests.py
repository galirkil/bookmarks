from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse


class MainIndexViewTestCase(TestCase):

    def setUp(self) -> None:
        self.path = reverse('index')

    def test_main_index_get(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Bookmarks - Главная')
        self.assertTemplateUsed(response, 'main/index.html')


class MainBookmarksListViewTestCase(TestCase):

    def setUp(self) -> None:
        self.path = reverse('main:my-bookmarks')

    def test_main_bookmarks_list_get(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertTemplateUsed(response, 'main/bookmarks.html')
