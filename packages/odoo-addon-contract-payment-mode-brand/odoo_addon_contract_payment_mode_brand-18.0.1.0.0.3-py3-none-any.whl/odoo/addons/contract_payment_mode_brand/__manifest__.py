# Copyright 2020 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Contract Payment Mode Brand",
    "summary": """
        This addon limits payment mode selection in contract to the brand's allowed.""",
    "version": "18.0.1.0.0",
    "license": "AGPL-3",
    "author": "ACSONE SA/NV," "Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/brand",
    "depends": [
        "contract_brand",
        "contract_payment_mode",
        "account_payment_mode_brand",
    ],
    "data": ["views/contract_contract.xml"],
}
