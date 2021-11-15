from django.shortcuts import render
from django.http import JsonResponse


def upc_view(request):
    # TODO: Edit this view to provide the output of the PriceComparator
    if 'upc' not in request.GET:
        return JsonResponse({})

    ret = {}
    return JsonResponse(ret)

