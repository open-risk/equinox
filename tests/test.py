from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse

from equinox import views


# ATTN internationalization strings are not captured

class HomePageTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('start:Front'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('start:Front'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'start/front.html')

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, '<h4>How does it work?</h4>')
