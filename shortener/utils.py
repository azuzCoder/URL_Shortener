from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

from .models import *


def is_valid_url(url: str):
    validate_url = URLValidator()

    try:
        validate_url(url)
    except ValidationError:
        return False

    return True


def get_url(url: str):
    short_url = ShortUrl.objects.filter(url=url)
    if short_url.exists():
        return short_url.first()
    return None


def make_short_url(request, short):
    return request.get_host() + '/' + short
