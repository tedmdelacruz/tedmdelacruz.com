# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-03 12:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('wagtailcore', '0040_page_draft_title'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('header', models.CharField(default='', max_length=128)),
                ('content', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('email', models.EmailField(default='', max_length=256)),
                ('github', models.CharField(default='', max_length=256)),
                ('linkedin', models.CharField(default='', max_length=256)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='PortfolioEntryPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('link', models.CharField(blank=True, default='', max_length=256)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='PortfolioIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('header', models.CharField(default='', max_length=128)),
                ('content', wagtail.wagtailcore.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AddField(
            model_name='homepage',
            name='currently_studying',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='intro_lead',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='homepage',
            name='intro_sub',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='homepage',
            name='intro_text',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='skills',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='tools',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]