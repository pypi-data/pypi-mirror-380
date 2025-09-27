# Copyright 2023 ForgeFlow S.L. (http://www.forgeflow.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "EDI Product",
    "summary": """
       EDI framework configuration and base logic for products and products packaging""",
    "version": "16.0.1.1.1",
    "license": "AGPL-3",
    "author": "ForgeFlow, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/edi-framework",
    "depends": [
        "product",
        "edi_oca",
    ],
    "data": [
        "views/product_views.xml",
        "views/product_packaging_views.xml",
    ],
}
