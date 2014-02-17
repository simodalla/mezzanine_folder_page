# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.test import TestCase
from ..models import FolderPage

FOLDER_NAME = 'Folder Test'
FOLDER_INTRO = """
<p>...</p>
<p><a class="btn btn-primary btn-lg" role="button">Learn more</a></p>
"""
FOLDER_CONTENT = ''.join(['<p>{}</p>'.format(row) for row in """
Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
Aenean commodo ligula eget dolor. Aenean massa.
Cum sociis natoque penatibus et magnis dis parturient montes,
nascetur ridiculus mus. Donec quam felis, ultricies nec,
pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim.
""".strip().split('\n')])


class FolderModelTest(TestCase):
    def setUp(self):
        self.folder_name = 'Folder Test'

    def test_save_folder(self):
        folder = FolderPage.objects.create(title=FOLDER_NAME,
                                           intro=FOLDER_INTRO,
                                           content=FOLDER_CONTENT,
                                           listing_children=True,
                                           intro_button_label='Go To',
                                           intro_button_href='#')
        self.assertEqual(folder.title, FOLDER_NAME)
        self.assertEqual(folder.intro, FOLDER_INTRO)
        self.assertEqual(folder.content, FOLDER_CONTENT)
        self.assertTrue(folder.listing_children, True)
        self.assertTrue(folder.intro_button_label, 'Go To')
        self.assertTrue(folder.intro_button_classes, 'btn-primary btn-lg')
        self.assertTrue(folder.intro_button_href, '#')

