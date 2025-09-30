# Copyright 2025 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging
from datetime import date

from odoo.tests.common import TransactionCase


class TestCalendarActivityEventDone(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        activity_type = cls.env.ref("mail.mail_activity_data_meeting")
        cls.calendar_event = cls.env["calendar.event"].create(
            {
                "name": "Test Event",
            }
        )
        cls.demo_user = cls.env.ref("base.user_demo")
        cls.activity = cls.env["mail.activity"].create(
            {
                "activity_type_id": activity_type.id,
                "res_id": cls.env.ref("base.res_partner_1").id,
                "res_model_id": cls.env["ir.model"]._get("res.partner").id,
                "user_id": cls.demo_user.id,
                "date_deadline": date.today(),
                "calendar_event_id": cls.calendar_event.id,
            }
        )

    def test_calendar_activity_event_done(self):
        self.assertFalse(self.calendar_event.action_done)
        self.assertFalse("✅" in self.calendar_event.display_name)

        logging.error(self.calendar_event)
        logging.error(self.activity)
        logging.error(self.activity.calendar_event_id)

        self.activity._action_done()

        self.assertTrue(self.calendar_event.action_done)
        self.assertTrue("✅" in self.calendar_event.display_name)
