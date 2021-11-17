from django.test import TestCase, Client
from django.urls import reverse

client = Client()


class PriceComparatorTests(TestCase):
    def test_no_query(self):
        resp = self.client.get(reverse('PRICE_COMPARATOR'))
        self.assertEqual(resp.content, b'Error: UPC missing from query')
