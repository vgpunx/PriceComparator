from django.test import TestCase, Client
from django.urls import reverse

client = Client()


class MerchantViewTests(TestCase):
    # Appedia tests
    def test_appedia_no_args(self):
        response = self.client.get(reverse('APPEDIA'))
        self.assertEqual(response.status_code, 200)

    def test_appedia_upc_test(self):
        response = self.client.get(reverse('APPEDIA') + '?upc=12345')
        self.assertEqual(response.json(), {'price': '$5.67', 'stock': 7})

    # Micromazon tests
    def test_micromazon_upc_test(self):
        response = self.client.get(reverse('MICROMAZON', kwargs={'upc': 12345}))
        self.assertEqual(response.json(), {"price": 4.56, "available": True})

    # Googdit tests
    def test_googdit_upc_test(self):
        response = self.client.get(reverse('GOOGDIT', kwargs={'upc': 12345}))
        self.assertEqual(response.json(), {"p": 234000000, "a": [{"l": 123, "q": 0}, {"l": 234, "q": 5}]})

