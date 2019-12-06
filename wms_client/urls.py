# coding=utf-8
"""URI Routing configuration for this apps."""
from django.conf.urls import url
from mezzanine.conf import settings
from .views import map

_slash = "/" if settings.APPEND_SLASH else ""

urlpatterns = [
    url(r"^(?P<slug>.*)%s$" % _slash, map, name='wms_map'),
]
