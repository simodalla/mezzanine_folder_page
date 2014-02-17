# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.db import models
from django.utils.translation import gettext_lazy as _
from mezzanine.pages.models import Page
from mezzanine.core.fields import RichTextField


class FolderPage(Page):
    """
    Implements content type FolderPage.
    """
    intro = RichTextField(_('Intro'), blank=True)
    content = RichTextField(_('Content'), blank=True)
    listing_children = models.BooleanField(default=True)
    intro_button_label = models.CharField(
        _('Label (Intro Button)'), max_length=40, blank=True)
    intro_button_classes = models.CharField(
        _('Classes (Intro Button)'), max_length=250, blank=True,
        default='btn-primary btn-lg')
    intro_button_href = models.URLField(
        _('Href (Intro Button)'), blank=True)

    search_fields = ('intro', 'content',)

    class Meta:
        verbose_name = _('Folder page')
        verbose_name_plural = _('Folder pages')




