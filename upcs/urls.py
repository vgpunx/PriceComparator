from django.urls import path
from .views import vendor_product


urlpatterns = [
    path('price-comparator', vendor_product, name='PRICE_COMPARATOR')
]
