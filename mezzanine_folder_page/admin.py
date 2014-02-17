# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from copy import deepcopy
from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import FolderPage


class FolderPageAdmin(PageAdmin):
    fieldsets = deepcopy(PageAdmin.fieldsets) + ((None, {'fields': ('intro',)}),)


admin.site.register(FolderPage, FolderPageAdmin)

