# Copyright 2025 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class CalendarEvent(models.Model):
    _inherit = "calendar.event"

    action_done = fields.Boolean()

    @api.depends("action_done", "name")
    def _compute_display_name(self):
        res = super()._compute_display_name()
        for rec in self.filtered("action_done"):
            rec.display_name = f"✅ {rec.name}"
        return res
