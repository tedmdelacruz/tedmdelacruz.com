# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-03 13:05
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20180303_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioentrypage',
            name='description',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]
