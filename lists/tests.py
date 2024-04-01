from django.test import TestCase
from django.urls import resolve
from lists.views import home_page #(1)

class SmokeTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEquals(found.func, home_page)

# Create your tests here.
