# Copyright 2025 Binhex <https://www.binhex.cloud>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class Partner(models.Model):
    _inherit = "res.partner"

    sale_order_template_id = fields.Many2one(
        "sale.order.template",
        string="Quotation Template",
    )
