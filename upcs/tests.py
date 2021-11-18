from django.test import TestCase, Client
from django.urls import reverse
from .views import vendor_product
from .parsers import merchant_parser, appedia_parser, micromazon_parser, googdit_parser

client = Client()


class PriceComparatorTests(TestCase):
    # Test the Price Comparator app with no input upc
    def test_no_query(self):
        resp = self.client.get(reverse('PRICE_COMPARATOR'))
        self.assertEqual(resp.content, b'Error: UPC missing from query')

    # Appedia Parser Tests
    def test_appedia_no_stock(self):
        ret = appedia_parser({'price': '$1.50', 'stock': 0})
        self.assertEqual(ret, None)

    def test_appedia_price_return(self):
        ret = appedia_parser({'price': '$1.50', 'stock': 1})
        self.assertEqual(ret, 1.50)

    # Micromazon Parser Tests
    def test_micromazon_no_stock(self):
        ret = micromazon_parser({'price': 1.50, 'available': False})
        self.assertEqual(ret, None)

    def test_micromazon_price_return(self):
        ret = micromazon_parser({'price': 1.50, 'available': True})
        self.assertEqual(ret, 1.50)

    # Googdit Parser Tests
    def test_googdit_no_stock(self):
        ret = googdit_parser({'p': 150000000, 'a': [{'l': 123, 'q': 0}, {'l': 234, 'q': 0}]})
        self.assertEqual(ret, None)

    def test_googdit_price_return(self):
        ret = googdit_parser({'p': 150000000, 'a': [{'l': 123, 'q': 1}, {'l': 234, 'q': 1}]})
        self.assertEqual(ret, 1.50)

    # Merchant Parser Tests
    def test_merchant_parser_no_upc(self):
        ret = merchant_parser('', None, {})
        self.assertEqual(ret, -1)

    # Merchant Parser -> Appedia Tests
    def test_merchant_parser_appedia_ret(self):
        ret = merchant_parser('Appedia', None, {'price': '$1.50', 'stock': 1})
        self.assertEqual(ret, 1.50)

    def test_merchant_parser_appedia_noitem(self):
        ret = merchant_parser('Appedia', None, {'price': '$1.50', 'stock': 0})
        self.assertEqual(ret, None)

    # Merchant Parser -> Micromazon Tests
    def test_merchant_parser_micromazon_ret(self):
        ret = merchant_parser('Micromazon', None, {'price': 1.50, 'available': True})
        self.assertEqual(ret, 1.50)

    def test_merchant_parser_micromazon_noitem(self):
        ret = merchant_parser('Micromazon', None, {'price': 1.50, 'available': False})
        self.assertEqual(ret, None)

    # Merchant Parser -> Googdit Tests
    def test_merchant_parser_googdit_ret(self):
        ret = merchant_parser('Googdit', None, {'p': 150000000, 'a': [{'l': 123, 'q': 1}, {'l': 234, 'q': 1}]})
        self.assertEqual(ret, 1.50)

    def test_merchant_parser_googdit_noitem(self):
        ret = merchant_parser('Googdit', None, {'p': 150000000, 'a': [{'l': 123, 'q': 0}, {'l': 234, 'q': 0}]})
        self.assertEqual(ret, None)
