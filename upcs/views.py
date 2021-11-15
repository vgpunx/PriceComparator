from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import sys
from .parsers import MERCHANTS


def vendor_product(request):
    if 'upc' not in request.GET:
        return HttpResponse('Error: UPC missing from query')

    upc = request.GET['upc']
    min_price = sys.float_info.max
    min_url = ''

    for merchant, config in MERCHANTS.items():
        price = config['function'](upc)
        if price is not None and price < min_price:
            min_price = price
            min_url = config['url']
            min_merchant = merchant

    if min_merchant == 'appedia':
        ret = str(min_url) + 'api/v1/itemdata?upc=' + str(upc)
    elif min_merchant == 'micromazon':
        ret = str(min_url) + str(upc) + "/productinfo"
    elif min_merchant == 'googdit':
        ret = str(min_url) + str(upc)

    return HttpResponse(ret)
