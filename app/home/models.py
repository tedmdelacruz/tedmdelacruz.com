from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel

class HomePage(Page):
    intro_lead = models.CharField(blank=False, max_length=128, default="")
    intro_sub = models.CharField(blank=False, max_length=128, default="")
    intro_text = RichTextField(blank=True)

    skills = RichTextField(blank=True)
    currently_studying = RichTextField(blank=True)
    tools = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro_lead', classname="intro-lead"),
        FieldPanel('intro_sub', classname="intro-sub"),
        FieldPanel('intro_text', classname="full intro-content"),
        FieldPanel('skills', classname="full intro-content"),
        FieldPanel('currently_studying', classname="full intro-content"),
        FieldPanel('tools', classname="full intro-content"),
    ]
