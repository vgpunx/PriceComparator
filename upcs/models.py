from django.db import models
from django.core.validators import RegexValidator, URLValidator


class Merchant(models.Model):
    """The merchant Model stores merchant data that is parsed to test for lowest available price.
    New merchants can be added via the admin interface.
    When a new merchant is added, parser implementation should be written within .parsers
    """
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
