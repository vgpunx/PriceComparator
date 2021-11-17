from django.db import models
from django.core.validators import RegexValidator, URLValidator


class Merchant(models.Model):
    name = models.CharField(default=None, max_length=200)
    api_url = models.CharField(default=None, max_length=200,
                               validators=[URLValidator(message='Error: Please enter a URL')])
    query_fmt = models.CharField(default=None,
                                 max_length=50,
                                 validators=[RegexValidator('<upc>',
                                                            'Error: Please include <upc> in the query format')])

    def __get_name__(self):
        return self.name

    def __get_api_url__(self):
        return self.api_url

    def __get_query_fmt__(self):
        return self.query_fmt
