import urllib.request
import json


# Master merchant parser
def merchant_parser(name, upc_query, test_query=None):
    if test_query is None:
        resp = urllib.request.urlopen(upc_query).readline()
        body = json.loads(resp)
    else:
        body = test_query

    # When a new merchant is added, add the merchant name to this list of statements and
    # call the appropriate merchant parser function as indicated below.
    # The name should exactly match the name given in the Merchant model.
    if body != {}:
        if name == 'Appedia':
            price = appedia_parser(body)
        elif name == 'Micromazon':
            price = micromazon_parser(body)
        elif name == 'Googdit':
            price = googdit_parser(body)
    else:
        return None

    return price


# -==================================================-
#           Merchant Parsers
#   When a new merchant is added, a new parser
#   should be appended to handle the new merchant's
#   specific JsonResponse implementation.
# -==================================================-
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
        if location['q'] > 0:
            price = float(body['p']) / 10e7
            return price
    return None
