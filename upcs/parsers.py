from django.http import JsonResponse
import urllib.request
import json


def merchant_parser(name, upc_query):
    resp = urllib.request.urlopen(upc_query).readline()
    body = json.loads(resp)
    if resp != JsonResponse({}):
        if name == 'Appedia':
            price = appedia_parser(body)
        elif name == 'Micromazon':
            price = micromazon_parser(body)
        elif name == 'Googdit':
            price = googdit_parser(body)
    else:
        # Flag for UPC does not exist
        return None

    return price


def appedia_parser(body):
    if body['stock'] <= 0:
        return None
    price = float(body['price'].strip('$'))
    return price


def micromazon_parser(body):
    if not body['available']:
        return None
    price = float(body['price'])
    return price


def googdit_parser(body):
    for location in body['a']:
        if location['q'] >= 0:
            price = float(body['p']) / 10e7
            return price
    return None
