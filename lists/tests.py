from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page
from lists.models import Item


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

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={"item_text": 'A new list item'})
        # self.assertIn('A new list item', response.content.decode())
        # self.assertTemplateUsed(response, 'home.html')
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def text_redirects_after_POST(self):
        response = self.client.post('/', data={"item_text": 'A new list item'})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_only_saves_items_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)

    def test_display_all_list_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        response = self.client.get('/')
        self.assertIn('itemey 1', response.content.decode())
        self.assertIn('itemey 2', response.content.decode())


class ItemModelTest(TestCase):
    def test_saving_and_retrieving_item(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

        # self.assertIn('A new list item', response.content.decode())
        # self.assertTemplateUsed(response, 'home.html')

        # first_item = Item()
        # first_item.text = 'The first list item'
        # first_item.save()
        #
        # second_item = Item()
        # second_item.text = 'Item the second'
        # second_item.save()
        #
        # saved_item = Item.objects.all()
        # self.assertEqual(saved_item.count(), 2)
        # first_saved_item = saved_item[0]
        # second_saved_item = saved_item[1]
        # self.assertEqual(first_saved_item.text, 'The first list item')
        # self.assertEqual(second_saved_item.text, 'Item the second')
