# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FolderPage',
            fields=[
                ('page_ptr', models.OneToOneField(primary_key=True, auto_created=True, to='pages.Page', parent_link=True, serialize=False)),
                ('intro', mezzanine.core.fields.RichTextField(blank=True, verbose_name='Intro')),
                ('content_info', mezzanine.core.fields.RichTextField(blank=True, verbose_name='Content Info')),
                ('listing_children', models.BooleanField(verbose_name='Listing Children', default=True)),
                ('intro_button_label', models.CharField(blank=True, max_length=40, verbose_name='Label (Intro Button)')),
                ('intro_button_classes', models.CharField(blank=True, max_length=250, default='btn-primary btn-lg', verbose_name='CSS Classes (Intro Button)')),
                ('intro_button_href', models.CharField(blank=True, max_length=500, verbose_name='Href (Intro Button)')),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Folder page',
                'verbose_name_plural': 'Folder pages',
            },
            bases=('pages.page',),
        ),
    ]
