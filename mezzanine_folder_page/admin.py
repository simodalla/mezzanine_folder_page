# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from copy import deepcopy
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
try:
    from mezzanine_page_auth.admin import PageAuthGroupAdmin as PageAdmin
except ImportError:
    from mezzanine.pages.admin import PageAdmin
from .models import FolderPage


class FolderPageAdmin(PageAdmin):
    fieldsets = (deepcopy(PageAdmin.fieldsets) +
                 ((_('Jumbotron Data'),
                   {'fields': (
                       'intro', 'content_info', 'listing_children',
                       'intro_button_label', 'intro_button_classes',
                       'intro_button_href')}),))


admin.site.register(FolderPage, FolderPageAdmin)

