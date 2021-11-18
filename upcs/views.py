from django.shortcuts import render
from django.http import HttpResponse
import sys
from .parsers import merchant_parser
from .models import Merchant


def vendor_product(request):
    if 'upc' not in request.GET:
        return HttpResponse('Error: UPC missing from query')

    upc = request.GET['upc']
    min_price = sys.float_info.max

    merchants_list = Merchant.objects.all()

    for merchant in merchants_list:
        merch_name = merchant.__get_name__()

        # merch_api_url = merchant.__get_api_url__()
        merch_api_url = 'http://localhost:8000/'
        merch_query_fmt = merchant.__get_query_fmt__().replace('<upc>', upc)
        merch_item_url = f'{merch_api_url}{merch_query_fmt}'

        price = merchant_parser(merch_name, merch_item_url)

        if (price is not None) and (price != -1) and (price < min_price):
            min_price = price
            # min_url = merch_item_url
            ret = merchant.__get_api_url__() + merch_query_fmt
        elif price == -1:
            ret = 'Error: UPC invalid'
        elif price is None:
            ret = 'Item is not available at any merchant'

    return HttpResponse(ret)
