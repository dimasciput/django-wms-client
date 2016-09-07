# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='WMSPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'WMS',
                'verbose_name_plural': 'WMS',
            },
            bases=('pages.page', models.Model),
        ),
        migrations.CreateModel(
            name='WMSResource',
            fields=[
                ('slug', models.SlugField(unique=True, serialize=False, primary_key=True)),
                ('name', models.CharField(help_text=b'A name for the WMS map.', unique=True, max_length=100)),
                ('uri', models.CharField(help_text=b'URI for the WMS resource', max_length=100)),
                ('layers', models.TextField(help_text=b'The layers to be included in the map. Separate with commas, no spaces between the commas. If left blank the top of the layer list tree will be used by default.', blank=True)),
                ('description', models.TextField(help_text=b'Description for the map. If left blank, the WMS abstract text will be used.', blank=True)),
                ('preview', models.ImageField(help_text=b'Preview image for this WMS Resource.', upload_to=b'wms_preview', blank=True)),
                ('zoom', models.IntegerField(help_text=b'Default zoom level (1-19) for this map.', blank=True, validators=[django.core.validators.MaxValueValidator(19), django.core.validators.MinValueValidator(0)])),
                ('min_zoom', models.IntegerField(blank=True, help_text=b'Default minimum zoom level (0-19) for this map.', null=True, validators=[django.core.validators.MaxValueValidator(19), django.core.validators.MinValueValidator(0)])),
                ('max_zoom', models.IntegerField(default=19, help_text=b'Default minimum zoom level (0-19) for this map. Defaults to 19', null=True, blank=True, validators=[django.core.validators.MaxValueValidator(19), django.core.validators.MinValueValidator(0)])),
                ('north', models.FloatField(help_text=b'Northern boundary in decimal degrees. Will default to maxima of all layers.', null=True, blank=True)),
                ('east', models.FloatField(help_text=b'Eastern boundary in decimal degrees. Will default to maxima of all layers.', null=True, blank=True)),
                ('south', models.FloatField(help_text=b'Southern boundary in decimal degrees. Will default to minima of all layers.', null=True, blank=True)),
                ('west', models.FloatField(help_text=b'Western boundary in decimal degrees. Will default to minima of all layers.', null=True, blank=True)),
            ],
            options={
                'verbose_name': 'WMS Resource',
                'verbose_name_plural': 'WMS Resource',
            },
        ),
        migrations.AddField(
            model_name='wmspage',
            name='resources',
            field=models.ManyToManyField(related_name='WMSResource', to='wms_client.WMSResource'),
        ),
    ]
