from django.test import TestCase
from django.shortcuts import reverse

class HomePageTest(TestCase):

    def test_get(self):
        #ToDO some sort of Test
        response = self.client.get(reverse('landing-page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'landing.html')

    
        


    