from django.urls import path
from .views import upc_view


urlpatterns = [
    path('', upc_view, name="UPC")
]
