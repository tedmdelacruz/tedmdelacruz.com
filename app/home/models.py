from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


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


class PortfolioIndexPage(Page):
    header = models.CharField(blank=False, max_length=128, default="")
    content = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('header'),
        FieldPanel('content'),
    ]

    def get_context(self, request):
        context = super(PortfolioIndexPage, self).get_context(request)
        context['portfolio_entries'] = PortfolioEntryPage.objects.child_of(self).live()
        return context


class PortfolioEntryPage(Page):
    link = models.CharField(blank=True, max_length=256, default="")
    description = RichTextField(blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('link'),
        FieldPanel('description'),
        ImageChooserPanel('image'),
    ]


class ContactPage(Page):
    header = models.CharField(blank=False, max_length=128, default="")
    content = RichTextField(blank=True)

    email = models.EmailField(blank=False, max_length=256, default="")
    github = models.CharField(blank=False, max_length=256, default="")
    linkedin = models.CharField(blank=False, max_length=256, default="")

    content_panels = Page.content_panels + [
        FieldPanel('header'),
        FieldPanel('content'),
        FieldPanel('email'),
        FieldPanel('github'),
        FieldPanel('linkedin'),
    ]
