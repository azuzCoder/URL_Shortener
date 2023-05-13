from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index_page, name='home'),
    path('short', shortener, name='short'),
    # path('<str:short_token>', short),
    re_path(r'^(?P<short_token>[a-zA-Z0-9!@#$%&*\-/+=]{1,})', short)
]
