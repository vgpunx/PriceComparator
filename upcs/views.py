from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import sys
from .parsers import MERCHANTS


def upc_view(request):
    if 'upc' not in request.GET:
        return HttpResponse('Please input UPC using ?upc=XXXXX')

    upc = request.GET['upc']
    min_price = sys.float_info.max
    min_url = ''

    for merchant, config in MERCHANTS.items():
        price = config['function'](upc)
        if price is not None and price < min_price:
            min_price = price
            min_url = config['url']

    return HttpResponse(str(min_url))
