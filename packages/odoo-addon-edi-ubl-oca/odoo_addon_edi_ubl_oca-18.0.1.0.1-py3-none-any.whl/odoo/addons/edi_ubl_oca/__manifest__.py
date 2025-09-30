# Copyright 2021 Camptocamp SA
# @author: Simone Orsi <simone.orsi@camptocamp.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "EDI UBL",
    "summary": """Define EDI backend type for UBL.""",
    "version": "18.0.1.0.1",
    "development_status": "Alpha",
    "license": "AGPL-3",
    "website": "https://github.com/OCA/edi-framework",
    "author": "Camptocamp,Odoo Community Association (OCA)",
    "maintainers": ["simahawk"],
    "depends": ["edi_core_oca"],
    "data": [
        "data/edi_backend_type.xml",
    ],
    "demo": [
        "demo/edi_backend_demo.xml",
    ],
}
