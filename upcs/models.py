from django.db import models


class Merchant(models.Model):
    name = models.CharField(default=None, max_length=200)
    api_url = models.CharField(default=None, max_length=200)
    query_fmt = models.CharField(default=None, max_length=50)

    def __get_name__(self):
        return self.name

    def __get_api_url__(self):
        return self.api_url

    def __get_query_fmt__(self):
        return self.query_fmt
