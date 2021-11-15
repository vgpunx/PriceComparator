import urllib.request
import json


def appedia_parser(upc):
    resp = urllib.request.urlopen(f'http://localhost:8000/api/v1/itemdata?upc={upc}').readline()
    body = json.loads(resp)
    if body['stock'] <= 0:
        return None
    price = float(body['price'].strip('$'))
    return price


def micromazon_parser(upc):
    resp = urllib.request.urlopen(f'http://localhost:8000/{upc}/productinfo').readline()
    body = json.loads(resp)
    if not body['available']:
        return None
    price = float(body['price'])
    return price


def googdit_parser(upc):
    resp = urllib.request.urlopen(f'http://localhost:8000/{upc}').readline()
    body = json.loads(resp)
    for location in body['a']:
        if location['q'] >= 0:
            price = float(body['p']) / 10e7
            return price
    return None


MERCHANTS = {
    'appedia': {
        'url': 'appedia.fake/',
        'function': appedia_parser,
    },
    'micromazon': {
        'url': 'micromazon.lol/',
        'function': micromazon_parser,
    },
    'googdit': {
        'url': 'googdit.nop/',
        'function': googdit_parser,
    },
}
