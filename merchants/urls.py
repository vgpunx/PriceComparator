from django.urls import path
from .views import appedia, micromazon, googdit


urlpatterns = [
    path('itemdata', appedia, name='APPEDIA'),
    path('<upc>/productinfo', micromazon, name='MICROMAZON'),
    path('<upc>', googdit, name='GOOGDIT')
]
