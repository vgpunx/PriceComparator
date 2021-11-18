from django.shortcuts import render
from django.http import JsonResponse


APPEDIA_PRODUCTS = {
    '12345': {
        'price': '$5.67',
        'stock': 7
    },
    '56789': {
        'price': '$2.67',
        'stock': 0
    },
    '00000': {
        'price': '$1.50',
        'stock': 0
    }
}

MICROMAZON_PRODUCTS = {
    '12345': {
        'price': 4.56,
        'available': True
    },
    '56789': {
        'price': 4.56,
        'available': True
    },
    '00000': {
        'price': 1.50,
        'available': False
    }
}

GOOGDIT_PRODUCTS = {
    '12345': {
        'p': 234000000,
        'a': [
            {
                'l': 123,
                'q': 0
            },
            {
                'l': 234,
                'q': 5
            }
        ]
    },
    '56789': {
        'p': 999000000,
        'a': [
            {
                'l': 123,
                'q': 1
            },
            {
                'l': 234,
                'q': 5
            }
        ]
    },
    '00000': {
        'p': 150000000,
        'a': [
            {
                'l': 123,
                'q': 0
            },
            {
                'l': 234,
                'q': 0
            }
        ]
    }
}


def appedia(request):
    if 'upc' not in request.GET:
        return JsonResponse({})
    ret = APPEDIA_PRODUCTS.get(request.GET['upc'], {})
    return JsonResponse(ret)


def micromazon(request, upc):
    ret = MICROMAZON_PRODUCTS.get(upc, {})
    return JsonResponse(ret)


def googdit(request, upc):
    ret = GOOGDIT_PRODUCTS.get(upc, {})
    return JsonResponse(ret)
