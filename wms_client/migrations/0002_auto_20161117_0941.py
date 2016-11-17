# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wms_client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wmsresource',
            name='attribution',
            field=models.TextField(help_text=b'Attribution of this layer', blank=True),
        ),
        migrations.AddField(
            model_name='wmsresource',
            name='east_west_center',
            field=models.FloatField(help_text=b'center of map in vertical', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='wmsresource',
            name='north_south_center',
            field=models.FloatField(help_text=b'center of map in horizontal', null=True, blank=True),
        ),
    ]
