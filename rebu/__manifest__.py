# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "REBU",
    "summary": "Support to REBU in Odoo",
    "version": "13.0.1.0.0",
    "license": "AGPL-3",
    "author": "meigallo@meigallodixital",
    "category": "Purchase",
    "website": "https://github.com/meigallodixital/odoo-rebu",
    "depends": ["l10n_es"],
    "installable": True,
    'data': [
        'data/taxes_rebu.xml',
        'data/fiscal_position_rebu.xml',
        'data/fiscal_position_taxes_rebu.xml',
    ],
}
