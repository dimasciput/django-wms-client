# coding=utf-8
"""Model Admin Class."""

from django.contrib import admin

from mezzanine.pages.admin import PageAdmin
from .models import WMSPage, WMSResource


class WMSPageAdmin(PageAdmin):
    filter_horizontal = ('resources',)


admin.site.register(WMSPage, WMSPageAdmin)


class WMSResourceAdmin(admin.ModelAdmin):
    """Admin Class for WMSResource Model."""
    exclude = ('slug',)
    list_display = ('name', 'uri')
    list_filter = ['name', 'uri']
    search_fields = ['name', 'description']


admin.site.register(WMSResource, WMSResourceAdmin)
