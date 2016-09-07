# coding=utf-8
"""URI Routing configuration for this apps."""
from django.conf.urls import patterns, url
from mezzanine.conf import settings

_slash = "/" if settings.APPEND_SLASH else ""

urlpatterns = [
    url(r"^(?P<slug>.*)%s$" % _slash, 'wms_client.views.map', name='wms_map'),
]
