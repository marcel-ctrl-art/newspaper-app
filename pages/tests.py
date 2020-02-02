from django.contrib.auth import get_user_model
from django.test import SimpleTestCase, TestCase
from django.urls import reverse


class IndexPageTest(SimpleTestCase):

    def test_index_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        

class SignUpPage(TestCase):

    username = 'test_name'
    email = 'test_name@email.com'
    
    def test_signup_page_status_code(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)
        
    def test_signup_page_view(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        
    def test_correct_template(self):
        response = self.client.get(reverse('signup'))
        self.assertTemplateUsed(response, 'signup.html')
        self.assertEqual(response.status_code, 200)


