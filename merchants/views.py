from django.shortcuts import render
from django.http import JsonResponse


APPEDIA_PRODUCTS = {
    '12345': {
        'price': '$5.67',
        'stock': 7
    }
}

MICROMAZON_PRODUCTS = {
    '12345': {
        'price': 4.56,
        'available': True
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
