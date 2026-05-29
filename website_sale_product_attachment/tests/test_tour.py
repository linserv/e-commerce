# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl)
# Copyright 2021 Tecnativa - Víctor Martínez

from odoo.tests import HttpCase, tagged


@tagged("post_install", "-at_install")
class TestWebsiteSaleProductAttachmentTourl(HttpCase):
    def test_tour(self):
        self.skipTest("Requires demo data which is not loaded")
