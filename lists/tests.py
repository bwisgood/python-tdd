from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page


class SmokeTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)


class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        # request = HttpRequest()
        # response = home_page(request)
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
        # html = response.content.decode('utf-8')
        # self.assertTrue(html.startswith('<html>'))
        # self.assertIn('<title>To-do lists</title>', html)
        # self.assertTrue(html.endswith("</html>"))
        # expect_html = render_to_string('home.html')
        # self.assertEqual(html, expect_html)
