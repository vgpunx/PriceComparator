from django.test import TestCase, Client
from django.urls import reverse
from .views import merchant_view


client = Client()

class MerchantViewTests(TestCase):
    def test_merchant_view_no_args(self):
        response = self.client.get(reverse('MERCHANT'))
        self.assertContains(response, {})

    def test_appedia_merchant(self):
        response = self.client.get(reverse('MERCHANT') + '?merchant=appedia&upc=12345')
        self.assertEqual(response.json(), {'price': '$5.67', 'stock': 7})
