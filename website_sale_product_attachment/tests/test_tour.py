# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl)
# Copyright 2021 Tecnativa - Víctor Martínez

from odoo.tests import HttpCase, tagged


@tagged("post_install", "-at_install")
class TestWebsiteSaleProductAttachmentTourl(HttpCase):
    def test_tour(self):
        attachment = self.env.ref("website.library_image_11")
        product_categ_id = self.env["product.category"].create({
            "name": "Test Category",
            "parent_id": self.env.ref("product.product_category_all").id,
        })
        product = self.env["product.template"].create({
            "name": "Test Tour Product",
            "categ_id": product_categ_id.id,
            "standard_price": 500.0,
            "list_price": 750.0,
            "detailed_type": "consu",
            "weight": 0.01,
            "uom_id": self.env.ref("uom.product_uom_unit").id,
            "uom_po_id": self.env.ref("uom.product_uom_unit").id,
            "description_sale": "160x80cm, with large legs.",
        })
        product.website_attachment_ids = [(6, 0, [attachment.id])]
        self.start_tour("/shop", "website_sale_product_attachment_tour", login="demo")
