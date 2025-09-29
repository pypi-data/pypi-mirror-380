# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl-3.0-standalone.html).

from odoo import fields, models


class HrSalaryContribution(models.Model):
    _name = "hr.salary_contribution"
    _inherit = [
        "mixin.master_data",
    ]
    _description = "Salary Contribution"

    partner_id = fields.Many2one(
        string="Partner",
        comodel_name="res.partner",
        ondelete="restrict",
    )
