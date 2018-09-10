import unittest
from django.test.client import RequestFactory
from views import getFirstName
class UrlcacheTest(unittest.TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_only_specified_urls_are_cached(self):
        request = self.factory.get('/user/firstname') 
        response = getFirstName(request)
        self.assertEqual(response.status_code, 200)