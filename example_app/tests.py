from django.http.request import HttpRequest
from django.test import Client, TestCase
from .views import TITLES, hello


class ViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_hello_with_empty_request(self):
        response = hello(HttpRequest())

        self.assertEquals(200, response.status_code)
        self.assertTrue(is_random_title_exist(str(response.content), TITLES))

    def test_hello_with_valid_request(self):
        request = HttpRequest()
        request.GET['name'] = 'Alice'

        response = hello(request)

        self.assertContains(response, status_code=200, text='Alice')
    
    def test_hello_with_invalid_request(self):
        request = HttpRequest()
        request.GET['stand'] = 'Star Platinum'

        response = hello(request)

        self.assertNotEquals(200, response.status_code)
        self.assertEquals(400, response.status_code)
    

def is_random_title_exist(content, titles):
    for title in titles:
        if title in content:
            return True
    
    return False