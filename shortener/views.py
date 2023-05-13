from django.shortcuts import render, redirect
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.db.models import QuerySet

from .forms import *
from .utils import is_valid_url, get_url, make_short_url
from .models import ShortUrl


def index_page(request):
    return render(request, 'index.html')


def shortener(request):
    if request.method == 'POST':
        url = request.POST.get('url', '')
        if is_valid_url(url):
            short_url = get_url(url)
            if short_url is None:
                h = PBKDF2PasswordHasher()
                enc = h.encode(url, '1')
                short_url = ShortUrl(url=url, short=enc.split('$')[-1])
                short_url.save()
            return render(request, 'index.html', context={'short_url': make_short_url(request, short_url.short)})
        else:
            return render(request, 'index.html', context={'invalid_url': 'Invalid url'})
    return redirect('home')


def short(request, short_token):
    print(short_token)
    short_url = ShortUrl.objects.filter(short=short_token)
    if short_url.exists():
        short_url = short_url.first()
    else:
        return redirect('home')
    return redirect(short_url.url)
