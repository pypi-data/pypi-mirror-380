# Copyright 2025 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class MailActivity(models.Model):
    _inherit = "mail.activity"

    def _action_done(self, feedback=False, attachment_ids=None):
        for rec in self.filtered("calendar_event_id"):
            rec.calendar_event_id.write({"action_done": True})
        return super()._action_done(feedback, attachment_ids)
