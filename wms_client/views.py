# coding=utf-8
"""Views."""

from django.shortcuts import render
from django.http import HttpResponse

from wms_client.models import WMSResource


def map(request, slug):
    """Index page which renders a WMS map.

    :param request: A django request object.
    :type request: request

    :param slug: Slug


    :returns: Response will be a nice looking map page.
    :rtype: HttpResponse
    """
    wms = WMSResource.objects.get(slug=slug)
    return render(
        request,
        'wms_client/map.html',
        {'wms': wms})
