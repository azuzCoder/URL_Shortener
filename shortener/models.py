from django.db import models


class ShortUrl(models.Model):
    url = models.URLField()
    short = models.CharField(max_length=255)
